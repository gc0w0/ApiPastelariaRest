from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    foto: bytes = None
    valor_unitario: str
    
    {
        "nome" : "boneca inflavel",
        "descricao" : "util para todas as situacoes",
        "valor_unitario" : "10,00"
    }