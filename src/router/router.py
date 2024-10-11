from fastapi import APIRouter

class RouterPrototype:
    def __init__(self, prefix:str = "", tags: list = None, dependencies: list = None) -> None:
        self.prefix = prefix
        self.tags = tags if tags else []
        self.dependencies = dependencies if dependencies else []
    
    def clone(self, new_prefix:str = None, new_tagss: list = None) -> APIRouter:
        clone_router = APIRouter(
            prefix= new_prefix if new_prefix else self.prefix,
            tags= new_tagss if new_tagss else self.tags,
            dependencies= self.dependencies
        )

        return clone_router
