from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from view import *


#cores
co0 = "#00008b"   #azul escuro
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ffff00"   # yellow
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#e9edf5"   # sky blue


#criando janela

janela = Tk()
janela.title("Cadastro")
janela.geometry('1043x453')
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE)

#dividindo janelas

frame_cima = Frame(janela, width=310, height=50, bg=co5, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label Cima
app_nome=Label(frame_cima,text='Cadastro de Cliente', anchor=NW, font=('Ivy 13 bold'), bg=co5, fg = co0, relief='flat')
app_nome.place(x=10, y=20)

#variavel tree global
global tree

#funcao inserir
def inserir():
    nome = e_nome.get()
    dta_nasc = e_cal.get()
    telefone = e_telefone.get()
    cidade = e_cidade.get()

    dta_nasc_atual = datetime.strptime(dta_nasc, "%d/%m/%Y")


    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir_info(nome, dta_nasc_atual, telefone, cidade)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_nome.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_cidade.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()


#funcao atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_cidade.delete(0, 'end')


        dt = '{}/{}/{}'.format(tree_lista[2][8:10], tree_lista[2][5:7], tree_lista[2][0:4])

        e_nome.insert(0, tree_lista[1])
        e_cal.insert(0, dt)
        e_telefone.insert(0, tree_lista[3])
        e_cidade.insert(0, tree_lista[4])

        #funcao inserir
        def update():
            nome = e_nome.get()
            dta_nasc = e_cal.get()
            telefone = e_telefone.get()
            cidade = e_cidade.get()

            dta_nasc_atual = datetime.strptime(dta_nasc, "%d/%m/%Y")

            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar_info(nome, dta_nasc_atual, telefone, cidade, valor_id)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                e_nome.delete(0, 'end')
                e_cal.delete(0, 'end')
                e_telefone.delete(0, 'end')
                e_cidade.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=260)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')


#funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)

        messagebox.showinfo('Sucesso', 'Os dados foram deletados da tabela com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

# Configurando Frame baixo

#Nome
l_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg = co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left' ,relief='solid')
e_nome.place(x=15, y=40)

#telefone
l_telefone = Label(frame_baixo,text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg = co4, relief='flat')
l_telefone.place(x=10, y=70)
e_telefone = Entry(frame_baixo, width=45, justify='left' ,relief='solid')
e_telefone.place(x=15, y=100)

#data de nascimento
l_cal = Label(frame_baixo,text='Data de Nascimento *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg = co4, relief='flat')
l_cal.place(x=10, y=130)
e_cal = DateEntry(frame_baixo, locale='pt_BR', date_pattern='dd/mm/yyyy', width=12, bg = 'darkblue', foreground='white', borderwidth=2)
e_cal.place(x=15, y=160)

#cidade
l_cidade = Label(frame_baixo,text='Cidade *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg = co4, relief='flat')
l_cidade.place(x=160, y=130)
e_cidade = ttk.Combobox(frame_baixo, values=mostrar_cidade(), width=20, justify='left')
e_cidade.place(x=165, y=160)


#botao inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg = co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=210)

#botao atualizar
b_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg = co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=210)

#botao deletar
b_deletar = Button(frame_baixo,text='Deletar', command=deletar, width=10, font=('Ivy 9 bold'), bg=co7, fg = co1, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=210)


#frame direita

def mostrar():

    global tree

    lista=mostrar_info()

    #lista cabecalho
    tabela_head = ['Id', 'Nome', 'Data de Nascimento', 'Telefone', 'Cidade']

    #criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    #scroollbar vertical
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    #scrollbar horizontal
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "center", "center"]
    h=[30, 190, 180, 155, 155]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col,width=h[n],anchor=hd[n])
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)




#chamando a funcao mostrar
mostrar()

janela.mainloop()
