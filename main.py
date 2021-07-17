from tkinter import *
from os import *
from functools import *

def semComando():
    print("")




def baixarVideoPlaylist():
    def download(link):
        print('youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + link.get())

    tela_init = Tk()
    tela_init.title("Insira o Link")
    tela_init.resizable(0,0)
    tela_init.geometry("500x80+250+250")
    lb = Label(tela_init, text="Insira o Link: ")
    entry_link = Entry(tela_init, width=200)
    button_confirm = Button(tela_init, text="OK", command=partial(download, entry_link)).pack(side=BOTTOM)
    lb.pack(side=LEFT)
    entry_link.pack(side=LEFT)
    





root = Tk()

root.title("Youtube Downloader")
root.geometry("800x300+100+200")


barradeMenus = Menu(root)

menuActives = Menu(barradeMenus, tearoff=0)
menuActives.add_command(label="Baixar Vídeo/Playlist", command=semComando)
menuActives.add_command(label="Baixar Música", command=baixarVideoPlaylist)
menuActives.add_separator()
menuActives.add_command(label="Fechar", command=root.quit)
barradeMenus.add_cascade(label="Ações", menu=menuActives)


root.config(menu=barradeMenus)


root.mainloop()