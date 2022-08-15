from ast import While
from distutils.log import error
from translate import Translator
import translate
import keyboard
from tkinter import *
while True:
   if keyboard.is_pressed('g'): 
      try:  
        master = Tk()
        master.title('en to pt')
        master.geometry('180x50+850+400')
        master.resizable(False, False)

        e = Entry(master, width=20)
        e.grid (row=0, column=0)

        def t():
            en = e.get()
            s = Translator(from_lang='english', to_lang='pt-br')
            res = s.translate(en)
            print(res)
            
            
            
            l = Label(master, text=res)
            l.grid(row=1, column=0)
                
        b = Button(master, text='traduzir', command=t)
        b.grid(row=0, column=4)

        master.mainloop()
      except:
          print('Houve um erro: ', error)
   if keyboard.is_pressed('h'): 
       try: 
        master = Tk()
        master.title('pt to en')
        master.geometry('270x80+850+400')
        master.resizable(False, False)

        e = Entry(master, width=20)
        e.grid (row=0, column=0)

        def t():
            en = e.get()
            s = Translator(from_lang='pt-br', to_lang='english')
            res = s.translate(en)
            print(res)
            l = Label(master, text=res)
            l.grid(row=0, column=4)
                
        b = Button(master, text='traduzir', command=t)
        b.grid(row=3, column=0)

        master.mainloop() 
       except:
          print('Houve um erro: ', error) 