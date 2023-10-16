from Chatgpt import Chatgpt
from tkinter import *
from tkinter import filedialog
import PyPDF2


global photo

class Application:
    def __init__(self, master=None):
        #PRIMEIRO CONTAINER
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady = 5)
        
        #cria o título da aplicação
        self.titulo = Label(self.primeiroContainer, text="CONSULTA CHATGPT")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()



        #SEGUNDO CONTAINER
        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady = 5)
        
        #cria o label do textfield que vai selecionar o arquivo PDF para traduzir
        self.nomeLabel = Label(self.segundoContainer,text="Arquivo (pdf): ", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        #cria o textfield que vai selecionar o arquivo PDF para traduzir
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT) 
        
        #cria botão de Upload
        self.upload = Button(self.segundoContainer, text="Upload", command = self.select_PDF)
        self.upload.pack(pady = 5)
        


        #TERCEIRO CONTAINER
        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 30)

        #cria textarea que vai mostrar TODO texto do acórdao do pdf
        self.textoAcordaoLabel = Label(self.terceiroContainer, text="Acórdão", font=self.fontePadrao)
        self.textoAcordaoLabel.pack(side=LEFT)
        self.textoAcordao = Text(self.terceiroContainer, height = 20, width = 70)
        self.textoAcordao["font"] = self.fontePadrao
        self.textoAcordao.pack(side=LEFT)


        
        #QUARTO CONTAINER        
        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 5)
        self.quartoContainer.pack(padx = 60)
        
        #cria o label do textarea que se deseja traduzir
        #self.chatGPTLabel = Label(self.quartoContainer, text="ChatGPT", font=self.fontePadrao)
        #self.chatGPTLabel.pack(side=LEFT)

        #self.chatGPT = Text(self.quartoContainer, height = 8, width = 65)
        #self.chatGPT["font"] = self.fontePadrao
        #self.chatGPT.pack(side=LEFT)
        #self.chatGPT.insert(END, "Tal dever, ao qual estão vinculados os órgãos de imprensa não deve consubstanciar-se dogma absoluto, ou condição peremptoriamente necessária à liberdade de imprensa, mas um compromisso ético com a informação verossímil, o que pode, eventualmente, abarcar informações não totalmente precisas.")
        
        self.textoGPTLabel = Label(self.quartoContainer, text="Reescreva", font=self.fontePadrao)
        self.textoGPTLabel.pack(side = LEFT)
        
        #cria botão de consulta Chatgpt
        self.photo = PhotoImage(file = r'C:\Users\rcost\Downloads\gui_python\chatgpt-logo.png')
        self.consultar = Button(self.quartoContainer, image = self.photo, command = self.consultaChatgpt)
        self.consultar.pack(side = LEFT)
        
        #cria botão de consulta Latim
        self.photoLatim = PhotoImage(file = r'C:\Users\rcost\Downloads\gui_python\chatgpt-latim.png')
        self.consultarLatim = Button(self.quartoContainer, image = self.photoLatim, command = self.consultaLatim)
        self.consultarLatim.pack(side = LEFT)
        
        self.textoGPTLabel = Label(self.quartoContainer, text="Traduza", font=self.fontePadrao)
        self.textoGPTLabel.pack(side = RIGHT)
        
        
        
        
        
        
        #QUINTO CONTAINER
        self.quintoContainer = Frame(master)    

        
        #SEXTO CONTAINER        
        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(pady = 10)     
        
        #cria textarea que vai mostrar o texto traduzido retornado pelo chatgpt
        self.textoGPTLabel = Label(self.sextoContainer, text="ChatGPT", font=self.fontePadrao)
        self.textoGPTLabel.pack(side=LEFT)
        self.textoGPT = Text(self.sextoContainer, height = 12, width = 70)
        self.textoGPT["font"] = self.fontePadrao
        self.textoGPT.pack(side=LEFT)
        


    #Método rescreve texto
    def consultaChatgpt(self):
        consulta = Chatgpt.Chatgpt()        
    
        #textoChatGPT = self.chatGPT.get("1.0",END)
        textoChatGPT = self.textoAcordao.selection_get()
        retornoConsulta = consulta.selectGPT("Reescreva a frase de forma simples: "+textoChatGPT)
        
        #apaga o texto que já está escrito no textarea
        self.textoGPT.delete('1.0', END)
        #escreve na textarea com o resultado da consulta no chatgpt
        self.textoGPT.insert(END, retornoConsulta)
        
    
        #Método significado latim
    def consultaLatim(self):
        consulta = Chatgpt.Chatgpt()        
    
        #textoChatGPT = self.chatGPT.get("1.0",END)
        textoChatGPT = self.textoAcordao.selection_get()
        retornoConsulta = consulta.selectGPT("qual o significado de \""+textoChatGPT+"\"")
        
        #apaga o texto que já está escrito no textarea
        self.textoGPT.delete('1.0', END)
        #escreve na textarea com o resultado da consulta no chatgpt
        self.textoGPT.insert(END, retornoConsulta)

 
    
    def select_PDF(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        PDF_file = open(filename, 'rb')
        read_pdf = PyPDF2.PdfReader(PDF_file)
        number_of_pages = len(read_pdf.pages)
        doc_content = ""

        #Extrai o texto do arquivo PDF#
        for i in range(number_of_pages):
            page = read_pdf.pages[i]
            page_content = page.extract_text()
            doc_content += page_content
        
        #apaga o texto que já está escrito no textarea
        self.textoAcordao.delete('1.0', END)
        self.textoAcordao.insert(END, doc_content)
        
        return filename 
        
        

root = Tk()
root.geometry("700x750")
#scrollbar = Scrollbar(root)
#scrollbar.pack( side = RIGHT, fill = Y )
Application(root)
root.mainloop()