from src.router.router import RouterPrototype
from src.seed.seed import seed

prototype_router = RouterPrototype(prefix="/router")
router = prototype_router.clone(new_prefix="/seed")

@router.get('/')
def create_seed():
    seed()
    return {"message": "Seed created"}