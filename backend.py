import sqlite3
import datetime


class BancoDeDados():

    def __init__(self):
        self.conn = sqlite3.connect('vendas.db')
        self.cursor = self.conn.cursor()

    def criandoBD(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS vendas(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT(30) NOT NULL,
                            preco REAL NOT NULL,
                            dia DATE NOT NULL DEFAULT CURRENT_DATE,
                            pagamento TEXT(10) NOT NULL,
                            produto TEXT(30) NOT NULL,
                            quantidade NUMBER NOT NULL
                            )''',
                            )
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fiado(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT(30) NOT NULL,
                            preco REAL NOT NULL,
                            dia DATE NOT NULL DEFAULT CURRENT_DATE
                            )''',
                            )
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT(30) NOT NULL,
                            preco REAL NOT NULL,
                            estoque NUMBER NOT NULL
                            )''')
        self.conn.commit()
        self.cursor.close()
        self.conn.close()



class Backend(BancoDeDados):
    
    def __init__(self):
        super().__init__()
        self.criandoBD()
    
    def InserirDadosVendas(self, nome, preco, pagamento, Nomeproduto, quantidade, idProduto):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO vendas(nome, preco, pagamento, produto, quantidade) VALUES (?, ?, ?, ?, ?)",(nome, preco, pagamento, Nomeproduto, quantidade))
                cursor.execute("SELECT estoque FROM produtos WHERE id = ?",(idProduto,))
                resultado = cursor.fetchone()
                if resultado is None:
                    return False
                quantidadeEstoque = resultado[0]
                quantidadeAtual = quantidadeEstoque - quantidade
                cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?",(quantidadeAtual, idProduto))
                conn.commit()
                return True
        except Exception as e:
            return False
    
    def PreenchendoTabelaOpcaoVenda(self):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT nome, preco, estoque FROM produtos")
                dados = cursor.fetchall()
                return dados
        except:
            return []
    
    def InserindoProduto(self, nome, preco, estoque):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO produtos(nome,preco, estoque) VALUES(?, ?, ?)", (nome, preco, estoque))
                conn.commit()
                return True
        except Exception as e:
            return False
        
    def AlterandoEstoqueProduto(self, quantidade, id):
        print(quantidade, id)
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute('''UPDATE produtos SET estoque = ? WHERE id = ?''', (quantidade, id))
                conn.commit()
                return True
        except:
            return False
     
    def TabelaAlterarEstoque(self):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT rowid, nome, preco, estoque FROM produtos")
                return cursor.fetchall()
        except Exception as e:
            print("ERRO:", e)
            return []
        
    def ListaDeProduto(self):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id,nome FROM produtos")
                produtos = cursor.fetchall()
                return produtos
        except Exception as e:
            print(e)
            return []
    
    ###### criar o backend de dados para
    #### uma tabela que mostra todas as vendas e uma tabela
    ##### que mostra as ultimas 10 vendas
    def DadosTodasVendas(self):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM vendas")
                todasVendas = cursor.fetchall()
                return todasVendas
        except:
            return []
    
    def DadosUltimosDez(self):
        try:
            with sqlite3.connect("vendas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM vendas ORDER BY id DESC LIMIT 10")
                ultimasDezVendas = cursor.fetchall()
                return ultimasDezVendas
        except Exception as e:
            print("Erro Ultimos 10: ", e)
            return []