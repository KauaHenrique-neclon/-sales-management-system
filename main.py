import customtkinter
import sqlite3
import tkinter
from tkinter import ttk
import psycopg2
from backend import Backend


class MainInterface(Backend):

    def __init__(self):
        super().__init__()
        self.ConfigCores()
        self.config()

    def config(self):
        self.janela = customtkinter.CTk()
        self.janela.geometry('800x650')
        self.janela.title('Menu')
        self.janela.minsize(800,600)
        self.janela.grid_columnconfigure(0, weight=1)
        self.janela.grid_rowconfigure(0, weight=1)
        self.backend = Backend()

        # frame q fica none
        self.frameConteudo = None
        self.frameInserirDados = None
        self.frameAviso = None
        self.frameCadastrarProduto = None
        self.frameTabelaVenda = None
        self.frameAlterandoEstoque = None


        self.limparJanela()
        self.menu()
        #self.InserirDados()
        #self.CadastrarProduto()
        #self.AlterandoEstoqueProduto()
        #self.TabelaDeVenda()
    
    def ConfigCores(self):
        self.CorButton = "#2563EB"
        self.corFundo = "#F8FAFC"
        self.corButtonHouver = "#1D4ED8"
        self.corFundoEscuro = "#111827"
        self.buttonEscoru = "#0078D4"
        self.corVerde = "#0E6310"
        self.corvermelha = "#800000"


    def limparJanela(self):
        if self.frameConteudo is not None:
            self.frameConteudo.destroy()

    def login(self):
        self.frameConteudo = customtkinter.CTkFrame(self.janela, corner_radius=20, fg_color=("#FFFFFF"))
        self.frameConteudo.grid(row=0, column=0, sticky="nswe", padx=30, pady=30)
        self.frameConteudo.grid_columnconfigure(0, weight=1)
        self.frameConteudo.grid_rowconfigure((0, 1, 2, 3), weight=1)

        tituloFrame = customtkinter.CTkLabel(self.frameConteudo, text="Sistema de Vendas", font=("Arial bold", 22), text_color=("#000000", "#008AFF"))
        tituloFrame.grid(row=0, column=0, pady=(10, 5))

        self.senha = customtkinter.CTkEntry(self.frameConteudo, corner_radius=12, placeholder_text="Digite sua senha", width=360, show="*",  fg_color=("#FFFFFF", "#1f111a"), border_color=("#000000", "#008AFF"))
        self.senha.grid(row=1, column=0,  pady=(5, 5))

        buttonEntry = customtkinter.CTkButton(self.frameConteudo, corner_radius=12, text="Entrar", text_color="#FFFFFF", width=250, fg_color="#C800FF", border_color=("#BB00FF","#8C00FF"), hover_color=("#db2777", "#be185d"), command=self.verificarLogin)
        buttonEntry.grid(row=2, column=0, pady=(5,5))


    

    def verificarLogin(self):
        senha = self.senha.get()
        usuarios = {'5115':'kauã'}
        if senha in usuarios:
            self.limparJanela()
            self.menu()
        else:
            pass


    def menu(self):
        self.frameConteudo = customtkinter.CTkFrame(self.janela, corner_radius=20, fg_color=("#FFFFFF"))
        self.frameConteudo.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)
        self.frameConteudo.grid_columnconfigure(0, weight=1)
        self.frameConteudo.grid_rowconfigure(1, weight=1)
        self.frameConteudo.grid_rowconfigure(2, weight=0)
        
        frameButton = customtkinter.CTkFrame( self.frameConteudo, corner_radius=20, fg_color="transparent")
        frameButton.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        #botões
        buttonInserir = customtkinter.CTkButton(frameButton, text="Inserir", text_color="#FFFFFF", fg_color=self.CorButton, hover_color=self.corButtonHouver, command=self.ChamandoFrameInserir)
        buttonInserir.grid( row=0, column=0, sticky="n")
        buttonTabela = customtkinter.CTkButton(frameButton, text="Tabela", text_color="#FFFFFF",  fg_color=self.CorButton, hover_color=self.corButtonHouver, command=self.ChamandoFrameTabelaAlteraEstoque)
        buttonTabela.grid( row=0, column=2,padx=10,  sticky="n")
        buttonCadastroProduto = customtkinter.CTkButton(frameButton, text="Cadastro Produto", text_color="#FFFFFF",fg_color=self.CorButton, hover_color=self.corButtonHouver, command=self.ChamandoFrameCadastroProduto)
        buttonCadastroProduto.grid( row=0, column=3, padx=10, sticky="n")
        buttonTabelasVendas = customtkinter.CTkButton(frameButton, text="Tabela Vendas",text_color="#FFFFFF",fg_color=self.CorButton, hover_color=self.corButtonHouver, command= self.ChamandoFrameTabelaVenda)
        buttonTabelasVendas.grid( row=0, column=4, padx=10, sticky="n")

        #self.frameAbas = customtkinter.CTkFrame(self.frameConteudo, corner_radius=0, fg_color='transparent')
        #self.frameAbas.grid( row=1, column=0, sticky="nsew")
    

    def AvisoMensagens(self, cor, titulo, txtPequeno):
        #cor = "#0E6310"
        self.frameAviso = customtkinter.CTkFrame(self.frameConteudo, width=500, height=100, corner_radius=20, fg_color=cor)
        self.frameAviso.grid( row=2, column=0, padx=20, pady=10, sticky="nsew")
        tituloAviso = customtkinter.CTkLabel(self.frameAviso, width=400, height=30, text=titulo, fg_color="transparent", text_color="#FFFFFF")
        tituloAviso.pack(pady=(20, 20))
        msgPequena = customtkinter.CTkLabel(self.frameAviso, width=400, height=30, text=txtPequeno,text_color="#FFFFFF", fg_color="transparent")
        msgPequena.pack(pady=(40, 15))

    
    def InserirDados(self):
        self.frameInserirDados = customtkinter.CTkFrame(self.frameConteudo, corner_radius=15, fg_color="transparent")
        self.frameInserirDados.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        tituloFrame = customtkinter.CTkLabel( self.frameInserirDados,text="Inserir Venda",font=("Arial", 20, "bold"))
        tituloFrame.pack(pady=(10, 15))

        nomeCliente = customtkinter.CTkEntry(self.frameInserirDados, placeholder_text="Nome do Cliente", width=400, height=30)
        nomeCliente.pack(pady=8)
        precoCliente = customtkinter.CTkEntry( self.frameInserirDados, placeholder_text="Valor da Venda", width=400, height=30)
        precoCliente.pack(pady=8)
        self.pagamento = customtkinter.StringVar(value="pix")

        option_pagamento = customtkinter.CTkOptionMenu( self.frameInserirDados, variable=self.pagamento, values=["pix", "dinheiro", "cartao"], width=400)
        option_pagamento.pack(pady=8)

        listaProduto = self.backend.ListaDeProduto()
        dadosProduto = [f"{id} - {nome}" for id, nome in listaProduto]
        produtoComprado = customtkinter.StringVar(value="produto")
        optionProduto = customtkinter.CTkOptionMenu( self.frameInserirDados, variable=produtoComprado, values=dadosProduto, width=400)
        optionProduto.pack(pady=8)
        quantidadeVendida = customtkinter.CTkEntry( self.frameInserirDados, placeholder_text="Quantos item vendidos", width=400, height=30)
        quantidadeVendida.pack(pady=8)

        buttonSubmit = customtkinter.CTkButton( self.frameInserirDados, text="Inserir Venda", width=200, height=30, corner_radius=20, command=lambda: self.VerificarDadosInserirVenda(nomeCliente,precoCliente,self.pagamento,produtoComprado, quantidadeVendida))
        buttonSubmit.pack(pady=(20, 15))
    

    def CadastrarProduto(self):
        self.frameCadastrarProduto = customtkinter.CTkFrame( self.frameConteudo, corner_radius=15, fg_color="transparent")
        self.frameCadastrarProduto.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        tituloFrame = customtkinter.CTkLabel( self.frameCadastrarProduto,text="Cadastrar Produto",font=("Arial", 20, "bold"))
        tituloFrame.pack(pady=(20, 15))

        nomeDoProduto = customtkinter.CTkEntry(self.frameCadastrarProduto, placeholder_text="Nome do Produto", width=400, height=40, corner_radius=10)
        nomeDoProduto.pack(pady=8, fill="x", padx=130)
        precoDoProduto = customtkinter.CTkEntry(self.frameCadastrarProduto, placeholder_text="Preço do Produto", width=400, height=40, corner_radius=10)
        precoDoProduto.pack(pady=10, fill="x", padx=130)
        quantidadeEstoque = customtkinter.CTkEntry(self.frameCadastrarProduto, placeholder_text="Quantidade no estoque", width=400, height=40, corner_radius=10)
        quantidadeEstoque.pack(pady=10, fill="x", padx=130)
        buttonSubmit = customtkinter.CTkButton(self.frameCadastrarProduto, text="Cadastrar Produto", width=200, height=30, corner_radius=10, hover_color="#295EFB", command=lambda: self.VerificarCadastroDeProduto(nomeDoProduto, precoDoProduto, quantidadeEstoque))
        buttonSubmit.pack(pady=(20, 15))
    
    def AlterandoEstoqueProduto(self):
        self.frameAlterandoEstoque = customtkinter.CTkFrame( self.frameConteudo, corner_radius=15, fg_color="transparent")
        self.frameAlterandoEstoque.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        tituloFrame = customtkinter.CTkLabel( self.frameAlterandoEstoque,text="Alterar Estoque",font=("Arial", 20, "bold"))
        tituloFrame.pack(pady=(20, 15))

        # tabela
        self.tabelaAlterarEstoque = ttk.Treeview( self.frameAlterandoEstoque, columns=("rowid", "nome", "preco", "quantidade_estoque"),show="headings")
 
        self.tabelaAlterarEstoque.heading("rowid", text="ID")
        self.tabelaAlterarEstoque.heading("nome", text="Nome")
        self.tabelaAlterarEstoque.heading("preco", text="Preço")
        self.tabelaAlterarEstoque.heading("quantidade_estoque", text="Qtd. Estoque")

        self.tabelaAlterarEstoque.column("rowid", width=50, anchor="center")
        self.tabelaAlterarEstoque.column("nome", width=220)
        self.tabelaAlterarEstoque.column("preco", width=100, anchor="center")
        self.tabelaAlterarEstoque.column("quantidade_estoque", width=100, anchor="center")
        self.tabelaAlterarEstoque.bind("<Double-1>", self.AlterandoEstoque)

        self.tabelaAlterarEstoque.pack(fill="both", expand=True)
        self.PreenchendoTabelaAlterarEstoque()
    



    def TabelaDeVenda(self):
        self.frameTabelaVenda = customtkinter.CTkFrame( self.frameConteudo, corner_radius=15, fg_color="transparent")
        self.frameTabelaVenda.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.frameTabelaVenda.grid_rowconfigure(2, weight=1)
        self.frameTabelaVenda.grid_columnconfigure(0, weight=1)
        tituloFrame = customtkinter.CTkLabel( self.frameTabelaVenda,text="Historico de Vendas",font=("Arial", 20, "bold"))
        tituloFrame.grid(row=0, column=0, pady=(20, 10))
        frameBotoes = customtkinter.CTkFrame(self.frameTabelaVenda, fg_color="transparent")
        frameBotoes.grid(row=1, column=0, pady=(10, 15))
        buttonUltimos10 = customtkinter.CTkButton(frameBotoes, text="Ultimas Vendas", text_color="#FFFFFF", fg_color=self.CorButton, hover_color=self.corButtonHouver, command=self.CarregarUltimosDez)
        buttonUltimos10.grid(row=0, column=0, padx=10)
        buttonTotalVendas = customtkinter.CTkButton(frameBotoes, text="Todas Vendas", text_color="#FFFFFF", fg_color=self.CorButton, hover_color=self.corButtonHouver, command=self.CarregarTodasVendas) 
        buttonTotalVendas.grid(row=0, column=1, padx=10)
        self.criar_tabela()

    def criar_tabela(self):
        self.tabelaVendas = ttk.Treeview( self.frameTabelaVenda, columns=("rowid", "nome", "preco", "data", "pagamento", "produto", "quantidade"),
                                         show="headings")

        self.tabelaVendas.heading("rowid", text="ID")
        self.tabelaVendas.heading("nome", text="Nome")
        self.tabelaVendas.heading("preco", text="Preço")
        self.tabelaVendas.heading("data", text="Data")
        self.tabelaVendas.heading("pagamento", text="Pagamento")
        self.tabelaVendas.heading("produto", text="Produto")
        self.tabelaVendas.heading("quantidade", text="Qtd")

        self.tabelaVendas.column("rowid", width=50, anchor="center")
        self.tabelaVendas.column("nome", width=180)
        self.tabelaVendas.column("preco", width=80, anchor="center")
        self.tabelaVendas.column("data", width=100, anchor="center")
        self.tabelaVendas.column("pagamento", width=100, anchor="center")
        self.tabelaVendas.column("produto", width=100)
        self.tabelaVendas.column("quantidade", width=50, anchor="center")
        self.tabelaVendas.grid(row=2, column=0, sticky="nsew")




    ###################################################
    ###### tudo verificação de dados

    # verificar dados de entrada do Inserir Vendas
    def VerificarDadosInserirVenda(self, Nome, Preco, Pagamento, produtoComprado, Quantidade):
        nome = Nome.get()
        preco = Preco.get()
        pagamento = Pagamento.get()
        produto = produtoComprado.get()
        idProduto = int(produto.split(" - ")[0])
        nomeDoProduto = produto.split(" - ")[1].strip()
        #print("Nome do produto: ", nomeDoProduto)
        #print("Id do produto: ", idProduto)
        quantidade = int(Quantidade.get())
        if not nome and preco and pagamento:
            self.AvisoMensagens(self.corvermelha,"Dados Incompleto","Preencha todos os campos disponivel")
        if len(nome) < 2:
            self.AvisoMensagens(self.corvermelha,"Nome Pequeno","Nome precisa de pelo menos 2 caracteres")
        precoFloat = float(preco.replace(",", "."))
        if precoFloat <= 0:
            self.AvisoMensagens(self.corvermelha,"Preencha o Preço","Não foi preenchido o campo preço")
        if len(pagamento) < 3:
            self.AvisoMensagens(self.corvermelha,"Pagamento","Selecione o tipo de pagamento")
        if len(produto) <= 1:
            self.AvisoMensagens(self.corvermelha,"Pagamento","Selecione o produto vendido")
        if quantidade <= 0:
            self.AvisoMensagens(self.corvermelha,"Pagamento","Insira a quantidade vendido")
        try:
            inserir = self.backend.InserirDadosVendas(nome,precoFloat,pagamento, nomeDoProduto, quantidade, idProduto)
            if inserir == True:
                self.AvisoMensagens(self.corVerde,"Sucesso","Foi inserido os dados com sucesso")
            else:
                self.AvisoMensagens(self.corvermelha,"Erro","Não foi possivel inserir os dados")
        except:
            self.AvisoMensagens(self.corvermelha,"Erro","Não foi possivel inserir os dados, Try")
        
    ## backend para verificar dados do Cadastro do produto
    def VerificarCadastroDeProduto(self, nome, preco, quantidade):
        nome = nome.get()
        preco = preco.get()
        quantidade = quantidade.get()
        if not nome and preco and quantidade:
            self.AvisoMensagens(self.corvermelha,"Dados Incompleto","Preencha todos os campos disponivel")
        if len(nome) < 2:
            self.AvisoMensagens(self.corvermelha,"Nome Pequeno","Nome precisa de pelo menos 2 caracteres")
        precoFloat = float(preco.replace(",", "."))
        if precoFloat <= 0:
            self.AvisoMensagens(self.corvermelha,"Preencha o Preço","Não foi preenchido o campo preço")
        if len(quantidade) < 1:
            self.AvisoMensagens(self.corvermelha,"Preencha Quantidade","Insira a quantidade que tem no estoque")
        try:
            inserir = self.backend.InserindoProduto(nome,precoFloat,quantidade)
            if inserir == True:
                self.AvisoMensagens(self.corVerde,"Sucesso","Foi inserido os dados com sucesso")
            else:
                self.AvisoMensagens(self.corvermelha,"Erro","Não foi possivel inserir os dados")
        except:
            self.AvisoMensagens(self.corvermelha,"Erro","Não foi possivel inserir os dados")

    

    ## preenchendo a tabela para altera o estoque do produto   
    def PreenchendoTabelaAlterarEstoque(self):
        for item in self.tabelaAlterarEstoque.get_children():
            self.tabelaAlterarEstoque.delete(item)
        dados = self.backend.TabelaAlterarEstoque()
        for i in dados:
            self.tabelaAlterarEstoque.insert("", "end", values=i)
        
    ## Ideia de criar 2 button para um tabela com os 10 ultimos e outra da tabela com todos os dados
    #def PreenchendoTabelasVendas(self):
    #    pass

    
    ## backend do alterando o estoque
    def AlterandoEstoque(self, event):
        item = self.tabelaAlterarEstoque.selection()[0]
        valores = self.tabelaAlterarEstoque.item(item)["values"]
        id_produto = valores[0]
        estoque_atual = valores[3]
        self.abrirJanelaEditarEstoque(id_produto,estoque_atual)



    ## Criando janela para adicionar o estoque atual
    def abrirJanelaEditarEstoque(self, id_produto, estoque_atual):
        janela = customtkinter.CTkToplevel(self.janela)
        janela.geometry("300x200")
        janela.title("Alterar Estoque")
        label = customtkinter.CTkLabel(janela, text="Novo estoque")
        label.pack(pady=10)
        entry = customtkinter.CTkEntry(janela, placeholder_text=str(estoque_atual))
        entry.pack(pady=10)


        def salvar():
            novo = entry.get()
            self.backend.AlterandoEstoqueProduto(novo, id_produto)
            janela.destroy()
            self.PreenchendoTabelaAlterarEstoque()
        btn = customtkinter.CTkButton(janela, text="Salvar", command=salvar)
        btn.pack(pady=10)


    def ChamandoFrameInserir(self):
        self.NoneFrameBlock()
        self.InserirDados()
    
    def ChamandoFrameCadastroProduto(self):
        self.NoneFrameBlock()
        self.CadastrarProduto()
    
    def ChamandoFrameTabelaAlteraEstoque(self):
        self.NoneFrameBlock()
        self.AlterandoEstoqueProduto()
    
    def ChamandoFrameTabelaVenda(self):
        self.NoneFrameBlock()
        self.TabelaDeVenda()


    def NoneFrameBlock(self):
        if self.frameInserirDados is not None:
            self.frameInserirDados.destroy()
            self.frameInserirDados = None
        if self.frameCadastrarProduto is not None:
            self.frameCadastrarProduto.destroy()
            self.frameCadastrarProduto = None
        if self.frameTabelaVenda is not None:
            self.frameTabelaVenda.destroy()
            self.frameTabelaVenda = None
        if self.frameAlterandoEstoque is not None:
            self.frameAlterandoEstoque.destroy()
            self.frameAlterandoEstoque = None






    ####### vendas tabela
    ################################
    def LimparTabelaVendas(self):
        if hasattr(self, "tabelaVendas"):
            for item in self.tabelaVendas.get_children():
                self.tabelaVendas.delete(item)
    
    def CarregarTodasVendas(self):
        self.LimparTabelaVendas()
        dados = self.backend.DadosTodasVendas()

        for d in dados:
            self.tabelaVendas.insert("", "end", values=d)


    def CarregarUltimosDez(self):
        self.LimparTabelaVendas()
        dados = self.backend.DadosUltimosDez()
        for d in dados:
            self.tabelaVendas.insert("", "end", values=d) 

def chamando():
    app = MainInterface()
    app.janela.mainloop()


if __name__ == "__main__":
    chamando()