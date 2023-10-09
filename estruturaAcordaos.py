#script para estruturar acórdãos

# importa biblioteca
import fitz
import re
import os
import pandas as pd


path1 = '/Users/rcost/Downloads/acordaosTJDFT/'
lista1 = []
lista1 = os.listdir('/Users/rcost/Downloads/acordaosTJDFT/')

lista = []
listaFinal = []
nomeArquivoLista = []
orgaoLista = []
tipoProcesoLista = []
numeroProcessoLista = []
relatoriaProcessoLista = []
numeroAcordaoLista = []
decisaoProcessoLista = []
unanimidadeLista = []



for arq1 in lista1:
    print ("arquivo: " + arq1)
    if arq1.endswith('.pdf'):
        # faz a leitura
        with fitz.open(arq1) as pdf:
            texto = ""
            textoUltimaPagina = pdf.load_page(-1).get_text()
            if textoUltimaPagina.find("\nDECISÃO") == -1:
                textoUltimaPagina = pdf.load_page(-2).get_text() + pdf.load_page(-1).get_text()
        #    print (textoUltimaPagina)
            for pagina in pdf:
                texto += pagina.get_text()
                break
            
            #tratar os itens da primeira página: órgão, tipo processo [apelação, embargos de declaração [cível, criminal (oculta nome das partes)]], numero processo, [apelante(s), apelado(s), recorrente(s), representante legal(s), recorrido(s) embargante(s), embargado(s)] relator(a), numero acordao, ementa
            #pegar decisão última página
            
            #regex que pega indice do numero do processo
            res = re.search(r"\d{7}-\d{2}\.\d{4}\.\d{1,2}\.\d{2}\.\d{4}", texto)
            
            
            #pega órgao
            indiceInicioOrgao = (texto.index('Órgão'))+5
            indiceFimOrgao = indiceInicioOrgao+15
            orgao = texto[indiceInicioOrgao:indiceFimOrgao]
            
            
            #pega tipo processo
            indiceInicioTipoProcesso = (texto.index('Processo N.'))+11
            indiceFimTipoProcesso = res.start(0)-1
            tipoProcesso = texto[indiceInicioTipoProcesso:indiceFimTipoProcesso]
            
            
             #pega numero processo   
            indiceInicioNumeroProcesso = (res.start(0))
            indiceFimNumeroProcesso = indiceInicioNumeroProcesso+25
            numeroProcesso = texto[indiceInicioNumeroProcesso:indiceFimNumeroProcesso]
            
            
            #pega nome relator   
            indiceInicioNomeRelatoria = (texto.index('Relator'))+7
            if texto.find('Relatora', indiceFimNumeroProcesso) > -1:
                if texto.find('Relatora Designada', indiceFimNumeroProcesso) > -1:
                    indiceInicioNomeRelatoria = (texto.index('Relatora Designada'))+18
                elif texto.find('Relatora', indiceFimNumeroProcesso) > -1:
                    indiceInicioNomeRelatoria = (texto.index('Relatora'))+8
                
            indiceFimNomeRelatoria =  texto.index('\n', indiceInicioNomeRelatoria+1)
        #    print("indiceInicioNomeRelatoria:" + str(indiceInicioNomeRelatoria))
        #    print("indiceFimNomeRelatoria:" + str(indiceFimNomeRelatoria))
            relatoriaProcesso = texto[indiceInicioNomeRelatoria:indiceFimNomeRelatoria]
            
            
            #pega numero acordao   
            indiceInicioNumeroAcordao = (texto.index('Acórdão'))+10
            indiceFimNumeroAcordao = indiceInicioNumeroAcordao+8
            numeroAcordao = texto[indiceInicioNumeroAcordao:indiceFimNumeroAcordao]
            
            
            
            #aqui vai ter que ler de trás pra frente do documento, ou seja, iremos pegar a última página onde fica a Decisão
            
            
            
            #pega decisao   
            indiceInicioDecisao = (textoUltimaPagina.index('DECISÃO\n'))+8
            decisaoProcesso = textoUltimaPagina[indiceInicioDecisao:-1]

            
            
            #pega se foi provido ou desprovido   
            indiceInicioProvimento = (res.start(0))
            indiceFimProvimento = indiceInicioProvimento+25
            foiProvida = texto[indiceInicioProvimento:indiceFimProvimento]
            
            
            #pega se foi unânime
            foiUnanime = "não"
            if "unânime" in decisaoProcesso or "unanime" in decisaoProcesso or "UNÂNIME" in decisaoProcesso or "UNANIME" in decisaoProcesso or "Unanime" in decisaoProcesso or "Unânime" in decisaoProcesso: 
                foiUnanime = "sim"


            print(orgao + " " + tipoProcesso + " " + numeroProcesso + " " + relatoriaProcesso + " " + numeroAcordao + " " + decisaoProcesso)
            nomeArquivoLista.append(arq1)
            orgaoLista.append(orgao)
            tipoProcesoLista.append(tipoProcesso)
            numeroProcessoLista.append(numeroProcesso)
            relatoriaProcessoLista.append(relatoriaProcesso)
            numeroAcordaoLista.append(numeroAcordao)
            decisaoProcessoLista.append(decisaoProcesso)
            unanimidadeLista.append(foiUnanime)
            lista = [arq1, orgao, tipoProcesso, numeroProcesso, relatoriaProcesso, numeroAcordao, decisaoProcesso, foiUnanime]
            listaFinal.append(lista)
            
            
            
            
df1 = pd.DataFrame(listaFinal,columns=['nomeArquivo', 'orgao', 'tipoProcesso', 'numeroProcesso', 'relatoria', 'acordao', 'decisao', 'decisao unânime'])
df1.to_excel("output.xlsx") 






