from dados_falsos import dados_departamentos


class Departamento:

  def __init__(self, idD):
    self.idD = idD


class DepartamentoSQL:
  cursor = None
  conn = None

  def initSqlOp(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  def createDepartamentoSQLTable(self, conn):
    self.initSqlOp(conn)
    self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS departamentos (
          idD INTEGER PRIMARY KEY,
          nome TEXT,
          salarioMedio REAL
      )
  ''')
    self.populaDepartamentos()

  def populaDepartamentos(self):
    for dpto in dados_departamentos:
      
      self.cursor.execute('SELECT idD FROM departamentos WHERE idD = ?',
                          (dpto['idD'], ))

      
      existing_matricula = self.cursor.fetchone()

      if existing_matricula is None:
        self.cursor.execute(
          '''
              INSERT INTO departamentos (nome, salarioMedio)
              VALUES (?, ?)
          ''', (dpto['Nome'], dpto['SalarioMedio']))
      else:
        print(
          f"Departamento com idD {dpto['idD']} já cadastrado. Ignorando inserção."
        )

  def getDepartamentos(self, conn):
    self.initSqlOp(conn)
    self.cursor.execute('SELECT idD,nome,salarioMedio  FROM departamentos')
    dptos = self.cursor.fetchall()

    json_dptos = []
    for dpto in dptos:
      idD, nome, salarioMedio = dpto
      json_dptos.append({
        "idD": idD,
        "nome": nome,
        "salarioMedio": salarioMedio
      })

    return json_dptos

    return dptos
