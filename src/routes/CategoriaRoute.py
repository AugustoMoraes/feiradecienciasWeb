from fastapi import APIRouter
from src.repository.CategoriaRepository import listar_todas_categorias
router = APIRouter(prefix="/categoria")

@router.get('/categorias')
def get_categorias():
    
    try:
        categorias = listar_todas_categorias()
        return categorias
    except Exception as e:
        print(f"Error: {e}")
