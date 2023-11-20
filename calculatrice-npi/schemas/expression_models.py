from pydantic import BaseModel


class ExpressionModel(BaseModel):
    """
    ExpressionModel: 
        - utilise Pydantic pour la validation des données. 
        - structurer l'entrée des données pour l'API.
    """
    expression: str
