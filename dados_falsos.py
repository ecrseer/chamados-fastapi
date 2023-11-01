cabecalhos = {
  "usuarios": ["idU", "Nome", "DataDeNascimento", "Departamento"],
  "departamentos": ["idD", "Nome", "SalarioMedio"],
  "chamados": ["ChamadoID", "UsuarioID", "Titulo", "Descricao", "Prioridade"]
}
dados_usuarios = [{
  "idU": 1,
  "Nome": "Carla silva",
  "DataDeNascimento": "2000-08-19",
  "Departamento": 1
}, {
  "idU": 2,
  "Nome": "Adalberto silva",
  "DataDeNascimento": "1980-08-19",
  "Departamento": 2
}, {
  "idU": 3,
  "Nome": "Danila souza",
  "DataDeNascimento": "2002-08-19",
  "Departamento": 3
}, {
  "idU": 4,
  "Nome": "Gabriela souza",
  "DataDeNascimento": "1992-08-19",
  "Departamento": 4
}, {
  "idU": 5,
  "Nome": "Amilton couto",
  "DataDeNascimento": "1992-08-19",
  "Departamento": 5
}, {
  "idU": 6,
  "Nome": "Nilson souza",
  "DataDeNascimento": "2002-08-19",
  "Departamento": 1
}, {
  "idU": 7,
  "Nome": "Mariana Rodrigues",
  "DataDeNascimento": "2004-08-19",
  "Departamento": 3
}, {
  "idU": 8,
  "Nome": "Patricia Ferreira",
  "DataDeNascimento": "1986-08-19",
  "Departamento": 5
}, {
  "idU": 9,
  "Nome": "Fernando Martins",
  "DataDeNascimento": "1975-08-19",
  "Departamento": 2
}, {
  "idU": 10,
  "Nome": "Vanessa Sousa",
  "DataDeNascimento": "1994-08-19",
  "Departamento": 4
}]

dados_departamentos = [{
  "idD": 1,
  "Nome": "Vendas",
  "SalarioMedio": 5000
}, {
  "idD": 2,
  "Nome": "Tecnologia",
  "SalarioMedio": 8000
}, {
  "idD": 3,
  "Nome": "RH",
  "SalarioMedio": 4500
}, {
  "idD": 4,
  "Nome": "Contabilidade",
  "SalarioMedio": 5500
}, {
  "idD": 5,
  "Nome": "Marketing",
  "SalarioMedio": 6000
}]

dados_chamados = [{
  "ChamadoID": 1,
  "UsuarioID": 1,
  "Titulo": "Problema de conexão com a Internet",
  "Descricao":
  "Estou enfrentando dificuldades para me conectar à internet em minha estação de trabalho.",
  "Prioridade": "Normal",
  "dataAbertura": "2022-05-15T00:00:00"
}, {
  "ChamadoID": 2,
  "UsuarioID": 1,
  "Titulo": "Erro ao iniciar o software de edição",
  "Descricao":
  "Quando tento iniciar o software de edição de imagem, recebo uma mensagem de erro inesperado.",
  "Prioridade": "Alta",
  "dataAbertura": "2022-06-16T00:00:00"
}, {
  "ChamadoID": 3,
  "UsuarioID": 2,
  "Titulo": "Problema com impressora não reconhecida",
  "Descricao":
  "Minha impressora não está sendo reconhecida pelo computador quando tento imprimir documentos.",
  "Prioridade": "Baixa",
  "dataAbertura": "2023-03-10T09:30:00"
}, {
  "ChamadoID": 4,
  "UsuarioID": 3,
  "Titulo": "Solicitação de acesso a uma pasta compartilhada",
  "Descricao":
  "Preciso de acesso à pasta compartilhada 'Recursos Comuns' para colaborar em um projeto.",
  "Prioridade": "Normal",
  "dataAbertura": "2023-03-15T14:15:00"
}, {
  "ChamadoID": 5,
  "UsuarioID": 3,
  "Titulo": "Atualização de software pendente",
  "Descricao":
  "Recebi uma notificação sobre uma atualização de software pendente. Como posso proceder?",
  "Prioridade": "Baixa",
  "dataAbertura": "2023-05-01T16:45:00"
}, {
  "ChamadoID": 6,
  "UsuarioID": 4,
  "Titulo": "E-mail não está sendo sincronizado no aplicativo de e-mail",
  "Descricao":
  "Meus e-mails não estão sendo sincronizados corretamente no aplicativo de e-mail do computador.",
  "Prioridade": "Normal",
  "dataAbertura": "2023-05-08T08:00:00"
}, {
  "ChamadoID": 7,
  "UsuarioID": 5,
  "Titulo": "Problema ao acessar a VPN da empresa",
  "Descricao":
  "Ao tentar acessar a VPN da empresa, recebo um erro de autenticação.",
  "Prioridade": "Alta",
  "dataAbertura": "2023-05-10T11:20:00"
}, {
  "ChamadoID": 8,
  "UsuarioID": 6,
  "Titulo": "Lentidão no sistema após a última atualização",
  "Descricao":
  "Após a última atualização do sistema, notei uma significativa lentidão na execução das tarefas.",
  "Prioridade": "Normal",
  "dataAbertura": "2023-05-13T14:30:00"
}, {
  "ChamadoID": 9,
  "UsuarioID": 7,
  "Titulo": "Backup automático não está funcionando",
  "Descricao":
  "Meu backup automático de arquivos não tem sido executado conforme programado.",
  "Prioridade": "Baixa",
  "dataAbertura": "2023-05-20T10:10:00"
}, {
  "ChamadoID": 10,
  "UsuarioID": 3,
  "Titulo": "Perda de acesso ao sistema CRM",
  "Descricao":
  "Não consigo acessar o sistema CRM da empresa, o que está afetando meu trabalho.",
  "Prioridade": "Alta",
  "dataAbertura": "2023-05-25T16:00:00"
}]

dados_ativos_inventariado = [{
  "idAtivo": 1,
  "Tipo": "Computador",
  "NomeAtivo": "PC01",
  "NumeroSerie": "SN123456",
  "SistemaOperacional": "Windows 10",
  "DepartamentoFK": 1
}, {
  "idAtivo": 2,
  "Tipo": "Impressora",
  "NomeAtivo": "Impressora01",
  "NumeroSerie": "SN789012",
  "SistemaOperacional": "Não se aplica",
  "DepartamentoFK": 2
}, {
  "idAtivo": 3,
  "Tipo": "Servidor",
  "NomeAtivo": "Servidor01",
  "NumeroSerie": "SN345678",
  "SistemaOperacional": "Windows Server 2019",
  "DepartamentoFK": 3
}, {
  "idAtivo": 4,
  "Tipo": "Computador",
  "NomeAtivo": "PC02",
  "NumeroSerie": "SN654321",
  "SistemaOperacional": "macOS Catalina",
  "DepartamentoFK": 4
}, {
  "idAtivo": 5,
  "Tipo": "Impressora",
  "NomeAtivo": "Impressora02",
  "NumeroSerie": "SN987654",
  "SistemaOperacional": "Não se aplica",
  "DepartamentoFK": 5
}, {
  "idAtivo": 6,
  "Tipo": "Servidor",
  "NomeAtivo": "Servidor02",
  "NumeroSerie": "SN234567",
  "SistemaOperacional": "Linux CentOS 7",
  "DepartamentoFK": 1
}, {
  "idAtivo": 7,
  "Tipo": "Computador",
  "NomeAtivo": "PC03",
  "NumeroSerie": "SN543210",
  "SistemaOperacional": "Windows 11",
  "DepartamentoFK": 2
}, {
  "idAtivo": 8,
  "Tipo": "Impressora",
  "NomeAtivo": "Impressora03",
  "NumeroSerie": "SN456789",
  "SistemaOperacional": "Não se aplica",
  "DepartamentoFK": 3
}, {
  "idAtivo": 9,
  "Tipo": "Servidor",
  "NomeAtivo": "Servidor03",
  "NumeroSerie": "SN456123",
  "SistemaOperacional": "Ubuntu Server 20.04",
  "DepartamentoFK": 4
}, {
  "idAtivo": 10,
  "Tipo": "Computador",
  "NomeAtivo": "PC04",
  "NumeroSerie": "SN321654",
  "SistemaOperacional": "Windows 10",
  "DepartamentoFK": 5
}]
