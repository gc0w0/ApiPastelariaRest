from fastapi import APIRouter
from mod_funcionario.Funcionario import Funcionario
router = APIRouter()

#import da persistencia
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get todos executado"}, 200

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(f: Funcionario):
    return {"msg": "post executado", "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 200

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, f: Funcionario):
    return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 201

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 201

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(FuncionarioDB).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        
        dados = FuncionarioDB(None, corpo.nome, corpo.matricula,
        
        corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)
        
        session.add(dados)
        
        session.commit()
        
        return {"id": dados.id_funcionario}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario == id).one()
        
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo

        session.add(dados)
        session.commit()

        return {"id": dados.id_funcionario}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()


@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session()
        
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one()
        session.delete(dados)
        session.commit()
        
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

