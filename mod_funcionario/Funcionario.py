from pydantic import BaseModel

class Funcionario(BaseModel):
    id_funcionario: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None

    {
        "nome" : "Abc da Silva ljlsadfjlksdjf",
        "matricula" : "12345",
        "cpf" : "01923874656",
        "telefone" : "49988234567",
        "grupo" : 1,
        "senha" : "bolinhas"
    }