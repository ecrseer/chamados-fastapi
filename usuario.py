from dados_falsos import dados_usuarios


class Usuario:

  def __init__(self, idU):
    self.idU = idU


class UsuarioSQL:
  cursor = None
  conn = None

  def initSqlOp(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  def createUsuarioSQLTable(self, conn):
    self.initSqlOp(conn)
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS usuarios (
      idU INTEGER PRIMARY KEY,
      nome TEXT,dataDeNascimento TEXT,
      Departamento INTEGER       
      )
  ''')
    self.populaUsuarios()

  def populaUsuarios(self):
    for usuar in dados_usuarios:
      
      self.cursor.execute('SELECT idU FROM usuarios WHERE idU = ?',
                          (usuar['idU'], ))
      idExistente = self.cursor.fetchone()

      if idExistente is None:
        self.cursor.execute(
          '''
              INSERT INTO usuarios (nome,dataDeNascimento,Departamento)
              VALUES (?, ?, ?)
          ''',
          (usuar['Nome'], usuar['DataDeNascimento'], usuar['Departamento']))
      else:
        print(
          f"Usuario com idU {usuar['idU']} já cadastrado. Ignorando inserção.")

  def getUsuarios(self, conn):
    self.initSqlOp(conn)
    self.cursor.execute(
      'SELECT idU,nome,dataDeNascimento,Departamento FROM usuarios')
    usuarios = self.cursor.fetchall()
    json_usuarios = []
    for usuario in usuarios:
      idU, nome, dataDeNascimento, Departamento = usuario
      json_usuarios.append({
        "idU": idU,
        "nome": nome,
        "dataDeNascimento": dataDeNascimento,
        "Departamento": Departamento
      })

    return json_usuarios
