from tkinter import *
from tkinter import Toplevel, Label, Entry, Button
from tkinter import messagebox

from models.produto import Produto
from config.DBConnection import *
from tkinter.messagebox import showinfo

from sqlalchemy.exc import IntegrityError
from tkinter import Button, Entry, Label, Toplevel, ttk
from controller.produto import consulta_todos_produtos_por_nome, lista_produtos

global novo_nome_entry, nova_descricao_entry, nova_embalagem_entry,novo_valor_entry

def preencher_tv(tree, nm_produto=None):
    for i in tree.get_children():
        tree.delete(i)

    produtos = lista_produtos() if not nm_produto else consulta_todos_produtos_por_nome(nm_produto)

    for produto in produtos['data']:
        tree.insert("", "end", values=(
            produto.cd_produto,
            produto.nm_produto,
            produto.ds_produto,
            "Ensacado" if produto.tp_embalagemproduto == "E" else "A granel",
            produto.vl_produto))
            

def atualiza_produto():
    atualiza_produto = Toplevel()
    atualiza_produto.title("Atualização de produto")
    atualiza_produto.geometry("1000x500")
    atualiza_produto.configure(background="#dde")

    Label(atualiza_produto, text="Digite o código do produto que deseja alteração", font=("Helvetica", 14), background="#dde", anchor="w").place(x=10, y=30, width=450, height=30)
    Label(atualiza_produto, text="Código Produto:", background="#dde", anchor="w").place(x=10, y=70, width=110, height=20)
    cd_produto_entry = Entry(atualiza_produto)
    cd_produto_entry.place(x=130, y=70, width=60, height=20)



    tview = ttk.Treeview(atualiza_produto, columns=("Código", "Nome", "Descrição", "Embalagem", "Valor"), show="headings")
    tview.heading("Código", text="Código")
    tview.heading("Nome", text="Nome")
    tview.heading("Descrição", text="Descrição")
    tview.heading("Embalagem", text="Embalagem")
    tview.heading("Valor", text="Valor")

    tview.column("Código", minwidth= 0, width=20)
    tview.column("Nome", minwidth= 0, width=200)
    tview.column("Descrição", minwidth= 0, width=350)
    tview.column("Embalagem", minwidth= 0, width=20)
    tview.column("Valor", minwidth= 0, width=15)
    
    tview.pack(padx=0, ipadx=190,ipady=240,pady=120, anchor='n') 
    
    preencher_tv(tview)

    
    def abrir_opcoes_atualizacao(cd_produto):
        opcoes_atualizacao = Toplevel()
        opcoes_atualizacao.title("Opções de Atualização")
        opcoes_atualizacao.geometry("1000x500")
        opcoes_atualizacao.configure(background="#dde")
        nome_produto = session.query(Produto.nm_produto).filter(Produto.cd_produto == cd_produto).first()        



        
        Label(opcoes_atualizacao, text="Selecione o que deseja atualizar do produto:", font=("Helvetica", 14), background="#dde", anchor="w").pack(padx=10, pady=10)
        Label(opcoes_atualizacao, text=f"{nome_produto}",background='#dde', anchor="w").place(x=10,y=20, width=250, height=20)

        Label(opcoes_atualizacao, text="Nome:",background='#dde', anchor="w").place(x=10,y=50, width=110, height=20) 
        novo_nome_entry = Entry(opcoes_atualizacao)
        novo_nome_entry.place(x=150, y=50, width= 110, height=20)

        Label(opcoes_atualizacao, text="Descrição:",background='#dde', anchor="w").place(x=10,y=80, width=110, height=20) 
        nova_descricao_entry = Entry(opcoes_atualizacao)
        nova_descricao_entry.place(x=150, y=80, width= 110, height=20)

        Label(opcoes_atualizacao, text="Embalagem:",background='#dde', anchor="w").place(x=10,y=110, width=110, height=20) 
        nova_embalagem_var = StringVar(opcoes_atualizacao)
        nova_embalagem_var.set("Selecione")  
        nova_embalagem_options = ["Granel", "Ensacado"]
        nova_embalagem_dropdown = OptionMenu(opcoes_atualizacao, nova_embalagem_var, *nova_embalagem_options)
        nova_embalagem_dropdown.place(x=150, y= 110)
        
        Label(opcoes_atualizacao, text="Valor:",background='#dde', anchor="w").place(x=10,y=145, width=110, height=20) 
        novo_valor_entry = Entry(opcoes_atualizacao)
        novo_valor_entry.place(x=150, y=145, width= 110, height=20)

        def atualizar_nome():

            cd_produto = cd_produto_entry.get()
            novo_nome = novo_nome_entry.get()

            if not cd_produto:
                messagebox.showerror("Erro", "Por favor, insira o código do produto.")
                return

            if not novo_nome:
                messagebox.showerror("Erro", "Por favor, insira o novo nome do produto.")
                return

            try:
                produto = session.query(Produto).filter_by(cd_produto=cd_produto).first()
                if produto:
                    produto.nm_produto = novo_nome
                    session.commit()
                    messagebox.showinfo("Sucesso", "Nome do produto atualizado com sucesso.")
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

        btn_atualizar_nome = Button(opcoes_atualizacao, text="Alterar", command=atualizar_nome)
        btn_atualizar_nome.place(x=290,y=50,width=90,height=20)


        def atualizar_descricao():

            cd_produto = cd_produto_entry.get()
            nova_descricao = nova_descricao_entry.get()
            

            if not cd_produto:
                messagebox.showerror("Erro", "Por favor, insira o código do produto.")
                return

            if not nova_descricao:
                messagebox.showerror("Erro", "Por favor, insira a nova descrição do produto.")
                return

            try:
                produto = session.query(Produto).filter_by(cd_produto=cd_produto).first()
                if produto:
                    produto.ds_produto = nova_descricao
                    session.commit()
                    messagebox.showinfo("Sucesso", "Descrição do produto atualizada com sucesso.")
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

        btn_atualizar_descricao = Button(opcoes_atualizacao, text="Alterar", command=atualizar_descricao)
        btn_atualizar_descricao.place(x=290,y=80,width=90,height=20)


        def atualizar_embalagem():

            cd_produto = cd_produto_entry.get()     
            

            if(nova_embalagem_var.get() == "Granel"): 
                nova_embalagem = "G"
            else:
                nova_embalagem = "E"

            if not cd_produto:
                messagebox.showerror("Erro", "Por favor, insira o código do produto.")
                return

            if not nova_embalagem:
                messagebox.showerror("Erro", "Por favor, insira o novo tipo de embalagem do produto.")
                return

            try:
                produto = session.query(Produto).filter_by(cd_produto=cd_produto).first()
                if produto:
                    produto.tp_embalagemproduto = nova_embalagem
                    session.commit()
                    messagebox.showinfo("Sucesso", "Tipo de embalagem do produto atualizado com sucesso.")
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

        btn_atualizar_embalagem = Button(opcoes_atualizacao, text="Alterar", command=atualizar_embalagem)
        btn_atualizar_embalagem.place(x=290,y=110,width=90,height=20)


        def atualizar_valor():

            cd_produto = cd_produto_entry.get()
            novo_valor = novo_valor_entry.get()

            if not cd_produto:
                messagebox.showerror("Erro", "Por favor, insira o código do produto.")
                return

            if not novo_valor:
                messagebox.showerror("Erro", "Por favor, insira o novo valor do produto.")
                return

            try:
                novo_valor = float(novo_valor)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o produto.")
                return

            try:
                produto = session.query(Produto).filter_by(cd_produto=cd_produto).first()
                if produto:
                    produto.vl_produto = novo_valor
                    session.commit()
                    messagebox.showinfo("Sucesso", "Valor do produto atualizado com sucesso.")
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

        btn_atualizar_valor = Button(opcoes_atualizacao, text="Atualizar Valor", command=atualizar_valor)
        btn_atualizar_valor.place(x=290,y=145,width=90,height=20)


    def seleciona_produto():
        cd_produto = cd_produto_entry.get()
        if not cd_produto:
            messagebox.showerror("Erro", "Por favor, insira o código do produto.")
            return
        abrir_opcoes_atualizacao(cd_produto)

    selecionar = Button(atualiza_produto, text="Selecionar Produto", command=seleciona_produto)
    selecionar.place(x=300, y=80)
