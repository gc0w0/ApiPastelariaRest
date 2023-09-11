# fiz esse tbm baseado no funcionario.py hehe
from pydantic import BaseModel 

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str = None
    compra_fiado: int
    dia_fiado: int
    senha: str = None

    {
        "nome" : "Abc da Silva ljlsadfjlksdjf",
        "cpf" : "01923874656",
        "telefone" : "49988234567",
        "compra_fiado" : 1,
        "dia_fiado" : "01092023",
        "senha" : "bolinhas"
    }