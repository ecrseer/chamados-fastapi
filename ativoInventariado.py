from dados_falsos import dados_ativos_inventariado  


class AtivoInventariado:

  def __init__(self, idAtivo, tipo, nome, numeroSerie, sistemaOperacional,
               departamentoFK):
    self.idAtivo = idAtivo
    self.tipo = tipo
    self.nome = nome
    self.numeroSerie = numeroSerie
    self.sistemaOperacional = sistemaOperacional
    self.departamentoFK = departamentoFK


class AtivoInventariadoSQL:

  cursor = None
  conn = None

  def initSqlOp(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  def createAtivoInventariadoSQLTable(self, conn):
    self.initSqlOp(conn)
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ativos_inventariados (
                idAtivo INTEGER PRIMARY KEY,
                tipo TEXT,
                nome TEXT,
                numeroSerie TEXT,
                sistemaOperacional TEXT,
                departamentoFK INTEGER
            )
        ''')
    self.populaAtivosInventariados()

  def populaAtivosInventariados(self):
    for ativo_data in dados_ativos_inventariado:      
      self.cursor.execute(
        'SELECT idAtivo FROM ativos_inventariados WHERE idAtivo = ?',
        (ativo_data['idAtivo'], ))
      existing_ativo = self.cursor.fetchone()

      if existing_ativo is None:
        self.cursor.execute(
          '''
                    INSERT INTO ativos_inventariados (tipo, nome, numeroSerie, sistemaOperacional, departamentoFK)
                    VALUES (?, ?, ?, ?, ?)
                ''',
          (ativo_data['Tipo'], ativo_data['NomeAtivo'],
           ativo_data['NumeroSerie'], ativo_data['SistemaOperacional'],
           ativo_data['DepartamentoFK']))
      else:
        print(
          f"Ativo com idAtivo {ativo_data['idAtivo']} já cadastrado. Ignorando inserção."
        )

  def getAtivosInventariados(self, conn):
    self.initSqlOp(conn)
    self.cursor.execute(
      'SELECT idAtivo, tipo, nome, numeroSerie, sistemaOperacional, departamentoFK FROM ativos_inventariados'
    )
    ativos_inventariados = self.cursor.fetchall()

    json_ativos_inventariados = []
    for ativo in ativos_inventariados:
      idAtivo, tipo, nome, numeroSerie, sistemaOperacional, departamentoFK = ativo
      json_ativos_inventariados.append({
        "idAtivo": idAtivo,
        "tipo": tipo,
        "nome": nome,
        "numeroSerie": numeroSerie,
        "sistemaOperacional": sistemaOperacional,
        "departamentoFK": departamentoFK
      })

    return json_ativos_inventariados
