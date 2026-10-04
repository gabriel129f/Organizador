#ARQUIVOS .JPG, .PNG IRÃO PARA A PASTA DE IMAGENS, ARQUIVOS .MP3, .WAV IRÃO PARA A PASTA DE MÚSICAS E ARQUIVOS .TXT, .DOCX, .PDF, IRÃO PARA A PASTA DE DOCUMENTOS
categorias= {".jpg": "imagens", ".png": "imagens",".jpeg": "imagens"
             , ".mp3": "musicas", ".wav": "musicas",
               ".txt": "documentos", ".docx": "documentos", ".pdf": "documentos"
               }
from pathlib import Path
pasta = Path("C:/Users/gabri/Downloads")#<--ALTERAR PARA O CAMINHO DA PASTA QUE DESEJA ORGANIZAR
for item in pasta.iterdir():
    if item.is_file(): #SE IR FOR UM ARQUIVO, MOSTRAR O NOME E A EXTENSÃO
        if item.suffix.lower() in categorias:
            pasta_destino = pasta / categorias[item.suffix.lower()]
            pasta_destino.mkdir(exist_ok=True) #CRIA A PASTA DE DESTINO CASO NÃO EXISTA
            item.rename(pasta_destino / item.name) #MOVE O ARQUIVO PARA A PASTA DE DESTINO
        else:
            item.rename(pasta / "outros" / item.name) #MOVE O ARQUIVO PARA A PASTA DE DESTINO