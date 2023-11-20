import pytest
from services.business_logic import calculer_npi

def test_addition():
    assert calculer_npi("3 4 +") == 7

def test_soustraction():
    assert calculer_npi("10 5 -") == 5

def test_multiplication():
    assert calculer_npi("6 7 *") == 42

def test_division():
    assert calculer_npi("8 4 /") == 2

def test_combinaison():
    assert calculer_npi("3 4 + 2 *") == 14

def test_entree_invalide():
    with pytest.raises(Exception):
        calculer_npi("a b +")
