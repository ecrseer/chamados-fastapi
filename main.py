from fastapi import FastAPI
import sqlite3
from departamento import DepartamentoSQL
from usuario import UsuarioSQL
from chamado import ChamadoSQL
from ativoInventariado import AtivoInventariadoSQL

app = FastAPI()

conn = sqlite3.connect('chamadosDb.db')
dptoSql = DepartamentoSQL()
dptoSql.createDepartamentoSQLTable(conn)

usuariosSql = UsuarioSQL()
usuariosSql.createUsuarioSQLTable(conn)

chamadosSql = ChamadoSQL()
chamadosSql.createChamadoSQLTable(conn)

ativoInventariadoSql = AtivoInventariadoSQL()
ativoInventariadoSql.createAtivoInventariadoSQLTable(conn)


# Default root endpoint
@app.get("/")
async def root():
  return {"message": "populado..."}


@app.get("/usuarios")
async def getUsuarios():
  return usuariosSql.getUsuarios(conn)


@app.get("/departamentos")
async def getDepartamentos():
  return dptoSql.getDepartamentos(conn)


@app.get("/chamados")
async def getChamados():
  return chamadosSql.getChamados(conn)


@app.get("/ativosInventariado")
async def getAtivosInventariado():
  return ativoInventariadoSql.getAtivosInventariados(conn)


