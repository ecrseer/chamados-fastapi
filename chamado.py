from dados_falsos import dados_chamados
from datetime import datetime

class Chamado:

    def __init__(self, chamado_id, usuario_id, titulo, descricao, prioridade, data_abertura):
        self.chamado_id = chamado_id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.data_abertura = data_abertura

class ChamadoSQL:

    cursor = None
    conn = None

    def initSqlOp(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def createChamadoSQLTable(self, conn):
        self.initSqlOp(conn)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chamados (
                ChamadoID INTEGER PRIMARY KEY,
                UsuarioID INTEGER,
                Titulo TEXT,
                Descricao TEXT,
                Prioridade INTEGER,
                DataAbertura DATE
            )
        ''')
        self.populaChamados()

    def populaChamados(self):
        for chamado_data in dados_chamados:
            self.cursor.execute('SELECT ChamadoID FROM chamados WHERE ChamadoID = ?',
                                (chamado_data['ChamadoID'],))
            existing_chamado = self.cursor.fetchone()

            if existing_chamado is None:
                self.cursor.execute(
                    '''
                    INSERT INTO chamados (UsuarioID, Titulo, Descricao, Prioridade, DataAbertura)
                    VALUES (?, ?, ?, ?, ?)
                    ''',
                    (chamado_data['UsuarioID'], chamado_data['Titulo'],
                     chamado_data['Descricao'], chamado_data['Prioridade'], chamado_data['dataAbertura']))
            else:
                print(
                    f"Chamado com ChamadoID {chamado_data['ChamadoID']} já cadastrado. Ignorando inserção."
                )

    def getChamados(self, conn):
        self.initSqlOp(conn)
        self.cursor.execute(
            'SELECT ChamadoID, UsuarioID, Titulo, Descricao, Prioridade, DataAbertura FROM chamados'
        )
        chamados = self.cursor.fetchall()
        json_chamados = []
        for chamado in chamados:
            ChamadoID, UsuarioID, titulo, descricao, prioridade, data_abertura = chamado
            json_chamados.append({
                "ChamadoID": ChamadoID,
                "UsuarioID": UsuarioID,
                "titulo": titulo,
                "descricao": descricao,
                "prioridade": prioridade,
                "dataAbertura": data_abertura
            })

        return json_chamados
