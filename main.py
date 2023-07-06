# impoortando tkinter
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk

# importando tk calendar
from tkcalendar import Calendar,DateEntry

from tkinter import messagebox
# importando views
from view import*

############# cores ##############
co0 = "#f0f3f5" # Preta
co1 = "#feffff" # Branco
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" # - Profit
co6 = "#038cfc" # Azul
co7 = "#ef5350" # Vermelho
co8 = "e9edf5"  # Verde +
co9 = "#e9edf5" # Verde +


############# Criando Janela ##############

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE,height=FALSE)

############# Dividindo Janela ##############
frame_cima = Frame(janela,width=310,height=50, background=co2, relief='flat')
frame_cima.grid(row=0,column=0)

frame_baixo = Frame(janela,width=310,height=403, background=co1, relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NSEW,padx=0,pady=1)

frame_direita = Frame(janela,width=588,height=403, background=co1, relief='flat')
frame_direita.grid(row=0,column=1, rowspan=2,padx=1,pady=0, sticky=NSEW)

############# Label cima ##############

app_nome = Label(frame_cima, text='Formulário de Consultoria', ancho=NW,font=('Ivy 13 bold'), background=co2,fg=co1, relief='flat')
app_nome.place(x=10,y=20)

#Variavel tree global
global tree


#Função inserir

def inserir():
    nome = e_nome.get() 
    email = e_email.get() 
    telefone = e_telefone.get()
    cal = e_cal.get()
    estado = e_estado.get()
    info = e_info.get()
    
    lista = [nome,email,telefone,cal,estado,info]
    
    if nome =='':
        messagebox.showerror('Error','O nome não pode ser vazio')
    else:
        inserirInfo(lista)       
        messagebox.showinfo('Sucesso', 'As informações foram inseridas com sucesso! ') 
        
        e_nome.delete(0,'end') 
        e_email.delete(0,'end') 
        e_telefone.delete(0,'end') 
        e_cal.delete(0,'end') 
        e_estado.delete(0,'end') 
        e_info.delete(0,'end') 
        
    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()

#Função Atualizar

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]   
        
        #Limpa os campos
        
        e_nome.delete(0,'end') 
        e_email.delete(0,'end') 
        e_telefone.delete(0,'end') 
        e_cal.delete(0,'end') 
        e_estado.delete(0,'end') 
        e_info.delete(0,'end')  
        
        e_nome.insert(0,tree_lista[1]) 
        e_email.insert(0,tree_lista[2]) 
        e_telefone.insert(0,tree_lista[3]) 
        e_cal.insert(0,tree_lista[4]) 
        e_estado.insert(0,tree_lista[5]) 
        e_info.insert(0,tree_lista[6]) 
        
        
        def update():
            nome = e_nome.get() 
            email = e_email.get() 
            telefone = e_telefone.get()
            cal = e_cal.get()
            estado = e_estado.get()
            info = e_info.get()
            
            lista = [nome , email , telefone , cal , estado , info, valor_id]
            
            if nome =='':
                messagebox.showerror('Error','O nome não pode ser vazio')
            else:
                atualizarInfo(lista)       
                messagebox.showinfo('Sucesso', 'As informações foram atualizadas com sucesso! ') 
                
                e_nome.delete(0,'end') 
                e_email.delete(0,'end') 
                e_telefone.delete(0,'end') 
                e_cal.delete(0,'end') 
                e_estado.delete(0,'end') 
                e_info.delete(0,'end') 
                
            for widget in frame_direita.winfo_children():
                widget.destroy()
                
            mostrar()   
             
        # Confirmar
        b_confirmar = Button(frame_baixo,command=update, text='Confirmar',width=10, ancho=NW,font=('Ivy 7 bold'), background=co2,fg=co1, relief='raised',overrelief='ridge')
        b_confirmar.place(x=110,y=380)
          

     

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha da tabela')

#Função Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]  
        
        deletarInfo(valor_id)
        messagebox.showinfo('Sucesso', 'As informações foram deletados da tabela com sucesso! ')
        
        for widget in frame_direita.winfo_children():
            widget.destroy()
            
        mostrar()  

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha da tabela')
    
############# Configurando Frame baixo ##############

# Nome
l_nome = Label(frame_baixo, text='Nome *', ancho=NW,font=('Ivy 10 bold'), background=co1,fg=co4, relief='flat')
l_nome.place(x=10,y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15,y=40)

# Email
l_email= Label(frame_baixo, text='Email *', ancho=NW,font=('Ivy 10 bold'), background=co1,fg=co4, relief='flat')
l_email.place(x=10,y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15,y=100)

# Telefone
l_telefone = Label(frame_baixo, text='Telefone *', ancho=NW,font=('Ivy 10 bold'), background=co1,fg=co4, relief='flat')
l_telefone.place(x=10,y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15,y=160)

# Data da Consulta
l_cal = Label(frame_baixo, text='Data da Consulta *', ancho=NW,font=('Ivy 10 bold'), background=co1,fg=co4, relief='flat')
l_cal.place(x=15,y=190)
e_cal = DateEntry(frame_baixo, width=12,background='darkblue',foreground='white',borderwidth=2)
e_cal.place(x=15,y=220)

# Estado
l_estado = Label(frame_baixo, text='Estado da consulta *', ancho=NW,font=('Ivy 10 bold'), background=co1,fg=co4, relief='flat')
l_estado.place(x=160,y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=160,y=220)

# Sobre
l_info = Label(frame_baixo, text='Informações extra', ancho=NW,font=('Ivy 10 bold'), background=co1,fg=co4, relief='flat')
l_info.place(x=15,y=260)
e_info = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_info.place(x=15,y=290)

# Botao inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir',width=10, ancho=NW,font=('Ivy 9 bold'), background=co6,fg=co1, relief='raised',overrelief='ridge')
b_inserir.place(x=15,y=340)

# Botao Atualizar
b_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar',width=10, ancho=NW,font=('Ivy 9 bold'), background=co2,fg=co1, relief='raised',overrelief='ridge')
b_atualizar.place(x=110,y=340)

# Botao Deletar
b_deletar = Button(frame_baixo,command=deletar, text='Deletar',width=10, ancho=NW,font=('Ivy 9 bold'), background=co7,fg=co1, relief='raised',overrelief='ridge')
b_deletar.place(x=205,y=340)

def mostrar():
    
    global tree 
    
    lista = mostrarInfo()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

#Chamando função mostrar
mostrar()       
 
janela.mainloop()