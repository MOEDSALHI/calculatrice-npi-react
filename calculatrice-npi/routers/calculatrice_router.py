from fastapi import APIRouter, Response, HTTPException
from services.business_logic import (
    calculate_and_save,
    export_calculations,
)
from models.models import Calcul
from schemas.expression_models import ExpressionModel
from database.db_session import Session
import csv
import io

router = APIRouter()


@router.post("/calculer/")
async def calculer(data: ExpressionModel):
    """
    Route pour calculer le résultat d'une expression mathématique.

    Args :
        data : expression sous forme de modèle Pydantic.

    Return:
        resultat d'évaluation
    """
    try:
        return calculate_and_save(data.expression)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/export/")
async def export_csv():
    """
    Route pour exporter les calculs en format CSV.

    Args :
        data : expression sous forme de modèle Pydantic.

    Retrun:
        response avec un fichier csv
    """
    csv_data = export_calculations()
    response = Response(content=csv_data, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=calculs.csv"
    return response
