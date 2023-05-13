# Imports
from tkinter import *
from tkinter import ttk

# Funcões
def clique_esquerdo_mouse(retorno):
    """
    -> Essa função serve apenas para facilitar a criação
    e a manutenção do programa, caso queira redimencionar a tela
    ou saber a localização de algum widget por exemplo.
    Após clicar com o botão esquerdo a função imprime no terminal
    a localização eixo X e Y de onde ocorreu o clique e a geometria atual da tela
    (Largura x Altura + distância a esquerda + distância topo).
    """
    print(f'X: {retorno.x} | Y: {retorno.y} | Geo: {janela.geometry()}')


def contar():
    """
    -> Faz a contagem e retorna os resultados na tela:
    - Quantidade de caracteres considerando a letra ou palavra ignorada.
    - Quanridade de palavras.
    - Quantidade da contagem personalizada ('Apenas').
    """
    ig = ignore_entry.get()
    texto = str(campo.get('1.0', END).strip())
    qnt_palavras = len(texto.split())
    apenas = apenas_entry.get()
    qnt_apenas = 0
    if len(ig) > 0:
        textoe = texto.replace(ig, '')
        qnt_palavras = len(textoe.split())
    else:
        textoe = texto

    if len(apenas) > 0:
        qnt_apenas = textoe.count(apenas)

    qnt_texto = (len(textoe))

    res_label['text'] = f'Quantidade de caracteres: {qnt_texto}.'
    palavras_label['text'] = f'Quantidade de palavras: {qnt_palavras}.'
    apenas_label['text'] = f'Quantidade "Apenas": {qnt_apenas}.'


def limpar_campo():
    """
    -> Limpa apenas o campo de texto.
    """
    campo.delete('1.0', END)


def limpar_tudo():
    """
    -> Limpa campo de texto, entry ignore e entry apenas.
    """
    campo.delete('1.0', END)
    ignore_entry.delete(0, END)
    apenas_entry.delete(0, END)


# Tela
janela = Tk()
janela.title('Contador de caracteres')

    # Redimencionamento da tela
janela.geometry('500x690+400+0')    # Largura x Altura + distancia a esquerda + distancia topo
janela.wm_resizable(height=False, width=False)    # Serve para "fixar" o redimensionamento da tela

    # Configurações da tela
janela.rowconfigure(0, minsize=70, weight=0)
janela.columnconfigure(1, minsize=400, weight=1)

    # Imagens de fundo
fundo = PhotoImage(file='feather-white-500x700.png')

label_fundo = Label(janela, image=fundo)
label_fundo.place(x=0, y=0)

    # Widgets
desc = Label(text='Digite o texto abaixo:', font=('Arial', 12, 'bold'), bg='#422f9b', fg='white')
desc.grid(column=0, row=0,  pady=5, padx=5, columnspan=2,)

campo = Text(height=15, width=15, font=('Arial', 11))
campo.grid(column=0, row=1, stick='nswe', padx=10, pady=5, columnspan=2)

scrollbar = ttk.Scrollbar(orient='vertical', command=campo.yview)
scrollbar.grid(column=1, row=1, stick='nse', padx=10, pady=5.5)
campo['yscrollcommand'] = scrollbar.set

ignore_Label = Label(text='Ignorar:', font=('Arial', 12, 'bold'), bg='#3a2d99', fg='white')
ignore_Label.grid(column=0, row=4, pady=10, padx=5, stick='e')

ignore_entry = Entry(font=('Arial', 12), width=35)
ignore_entry.grid(column=1, row=4, pady=10)

apenas_Label = Label(text='Apenas:', font=('Arial', 12, 'bold'), bg='#362d98', fg='white')
apenas_Label.grid(column=0, row=5, pady=10, padx=5, stick='e')

apenas_entry = Entry(font=('Arial', 12), width=35)
apenas_entry.grid(column=1, row=5, pady=10)

bt_contar = Button(text=' Contar ', command=contar, bg='green', fg='white', font=('Arial', 12), height=2, width=11)
bt_contar.grid(column=1, row=6, padx=15, pady=15, stick='w', columnspan='2')

bt_limpar_campo = Button(text='Limpar\nCampo', command=limpar_campo, bg='orange', fg='black', font=('Arial', 12), height=2, width=11)
bt_limpar_campo.grid(column=1, row=6)

bt_limpar_tudo = Button(text='Limpar\nTudo', command=limpar_tudo, bg='purple', fg='white', font=('Arial', 12), height=2, width=11)
bt_limpar_tudo.grid(column=1, row=6, columnspan=1, padx=10, stick='e')

res_label = Label(text='', font=('Arial', 12), bg='black', fg='white')
res_label.grid(column=0, row=7, padx=15, pady=10, columnspan=2, stick='nswe')

palavras_label = Label(text='', font=('Arial', 12), bg='black', fg='white')
palavras_label.grid(column=0, row=8, padx=15, pady=10, columnspan=2, stick='nswe')

apenas_label = Label(text='', font=('Arial', 12), bg='black', fg='white')
apenas_label.grid(column=0, row=9, padx=15, pady=10, columnspan=2, stick='nswe')

# Eventos de testes
janela.bind('<Button-1>', clique_esquerdo_mouse)

# Looping principal
janela.mainloop()


# Desenvolvido por Igor Souza.
# GitHub- https://github.com/Isouz
