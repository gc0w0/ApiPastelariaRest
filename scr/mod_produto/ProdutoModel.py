import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer, BLOB #esse ultimo o querido geferson me ajudou

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(CHAR(10), nullable=False)
    foto = Column(BLOB, nullable=True) #ver se vai dar certo // teve que ser colocado o LargeBinary pq não tem bytes
    valor_unitario = Column(VARCHAR(200), nullable=False)

    def __init__(self, id_produto, nome, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario
        