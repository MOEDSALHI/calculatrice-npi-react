from database.db_session import Session
from models.models import Calcul
import io
import csv

def calculer_npi(expression):
    """
    Calcule le résultat d'une expression mathématique en notation polonaise inversée.

    Args:
        expression (str): Expression mathématique en NPI à calculer.

    Returns:
        float: Résultat du calcul de l'expression.
    """
    pile = []
    for token in expression.split():
        if token in ["+", "-", "*", "/"]:
            b = pile.pop()
            a = pile.pop()
            if token == '+':
                pile.append(a + b)
            elif token == '-':
                pile.append(a - b)
            elif token == '*':
                pile.append(a * b)
            elif token == '/':
                pile.append(a / b)
        else:
            pile.append(float(token))
    return pile.pop()


def calculate_and_save(expression):
    """
    Calcule le résultat d'une expression en notation polonaise inversée et le sauvegarde dans la base de données.

    Args:
        expression (str): Expression mathématique en NPI à calculer.

    Returns:
        dict: Dictionnaire contenant l'expression et le résultat calculé.
    """
    resultat = calculer_npi(expression)
    session = Session()
    calcul = Calcul(expression=expression, resultat=resultat)
    session.add(calcul)
    session.commit()
    return {"expression": expression, "resultat": resultat}

def export_calculations():
    """
    Récupère tous les calculs de la base de données et les exporte au format CSV.

    Returns:
        str: Chaîne de caractères au format CSV représentant les calculs.
    """
    session = Session()
    query = session.query(Calcul).all()
    session.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Expression', 'Résultat'])

    for calcul in query:
        writer.writerow([calcul.id, calcul.expression, calcul.resultat])

    return output.getvalue()