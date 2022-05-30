# Código por Gustavo Albuquerque, 30/05/2022
import tkinter

# Vou começar definindo o Artista / Banda como uma classe
class Artista:

    def __init__(self, nome, genero_musical, pais, 
                 medalhas_ouro):
        self.nome = nome
        self.genero_musical = genero_musical
        self.pais = pais
        self.medalhas_ouro = medalhas_ouro


# Agora, vou criar / definir uma "Lista de Artistas", que vai abrigar todos os artistas.
lista_de_artistas = []

with open("Testes_1.txt", 'r') as arquivo: # O 'r' de 'read' é o default da função open, mas coloquei mesmo assim
    dados = arquivo.read() # Faz a leitura do arquivo. O "dados" é um "blocão" que contém todo o conteúdo do arquivo
    for linha in dados.splitlines(): # O splitlines() separa o blocão em linhas
        dados_linha = linha.split(',') # O método split() retorna uma lista! Ou seja, dados_linha é uma lista
        artista = Artista(nome=dados_linha[0].strip(),
                          genero_musical=dados_linha[1].strip(), 
                          pais=dados_linha[2].strip(),
                          medalhas_ouro=dados_linha[3].strip())
        # Os argumentos da classe Artista são posicionais, então não era necessário declará-los aqui.
        # Fiz isso apenas para deixar mais organizado e facilitar alterações.
        # Os "strip()" servem para remover os espaços vazios.    
        lista_de_artistas.append(artista)

# Agora, vou criar uma UI para exibir a lista. Com Class Janela() não funciona, já que não consigo incluir widgets fora da classe.
# Não consigo mencionar variáveis criadas dentro de uma classe fora dela.


#####################################################################################################
#####################################################################################################
#___________________________________PARTE DA USER INTERFACE__________________________________________
#####################################################################################################
#####################################################################################################

#___________________________________TELA TÍTULO__________________________________________

janela = tkinter.Tk() # Aqui, crio a janela com o tkinter
janela.title("Estatísticas Musicais - Alpha V0.1")  # Função do tkinter para alterar titulo da janela
janela.minsize(width=1080, height=600) # Função do tkinter para alterar tamanho minimo da janela

# Label teste que utilizei para ver se conseguia exibir algum elemento na janela
# label_teste = tkinter.Label(janela, text=lista_de_artistas[0].genero_musical)
# label_teste.pack()

# CONTAINER QUE ABRIGA O TÍTULO E SUBTÍTULO - Não obrigatório, mas ajuda a manter as coisas mais organizadas
frame_titulo = tkinter.Frame(janela)
frame_titulo.pack(side="top")

# Texto principal - Título
texto_titulo = tkinter.Label(frame_titulo, text="ESTATÍSTICAS MUSICAIS", font='Bahnschrift 40 bold')
texto_titulo.pack(side="top", pady=40)

# Subtítulo
texto_subtitulo = tkinter.Label(frame_titulo, text="Estatísticas sobre seu gosto musical! V0.1", font='Bahnschrift')
texto_subtitulo.pack(side="top", pady=5)

# CONTAINER QUE ABRIGA OS BOTÕES - Não obrigatório, mas ajuda a manter as coisas mais organizadas
frame_botoes_titulo = tkinter.Frame(janela)
frame_botoes_titulo.pack(side="top")
# Aqui fica o chamado CONTAINER onde ficam os botões!

# Botão Planilha
botao_planilha = tkinter.Button(frame_botoes_titulo, text="PLANILHA", font='Bahnschrift 20',
                                height=6, width=15)
botao_planilha.pack(side="left", padx=15, pady=50)
# O side = left é o que faz com que os botões se agrupem horizontalmente e não verticalmente
# O padx (padding) é para dar uma separadinha entre os botões

# Botão Rankings
botao_rankings = tkinter.Button(frame_botoes_titulo, text="RANKINGS", font='Bahnschrift 20',
                                height=6, width=15)
botao_rankings.pack(side="left", padx=15, pady=50)
# O side = left é o que faz com que os botões se agrupem horizontalmente e não verticalmente

# Botão Sobre
botao_sobre = tkinter.Button(frame_botoes_titulo, text="SOBRE", font='Bahnschrift 20',
                             height=6, width=15)
botao_sobre.pack(side="right", padx=15, pady=50)
# O side = left é o que faz com que os botões se agrupem horizontalmente e não verticalmente

# CONTAINER QUE ABRIGA O RODAPÉ - Não obrigatório, mas ajuda a manter as coisas mais organizadas
frame_rodape_titulo = tkinter.Frame(janela)
frame_rodape_titulo.pack(side="bottom")

# Texto do rodapé
texto_rodape = tkinter.Label(frame_rodape_titulo, text="Gustavo Albuquerque - 05/2022", font='Bahnschrift 10')
texto_rodape.pack()

janela.mainloop() # "Loop lógico" para manter a janela aberta
