import tkinter as tk


win=tk.Tk()
win.title('Calculator')
win.geometry('400x400+200+200')


B=tk.Button(win)
B.place(relx=0,rely=0,relwidth=1,relheight=0.1)
B.configure(text='QUIT')
B.configure(command=win.destroy)


EVar=tk.StringVar()
E=tk.Entry(win,textvariable=EVar)
E.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
E.configure(justify="right")

def cmdEset(a):
     EVar.set(EVar.get()+a)

def cmdCRTL(a):
    if a=='Clear':
        EVar.set('')
    elif a=='Enter':
        EVar.set(str(eval(EVar.get())))
    elif a=='Excute':
        print(TX.get(1.0,tk.END))
        exec(TX.get(1.0,tk.END),globals())
    elif a=='OpenPdf':
        import os
        os.startfile('C:\\Users\\soill\\OneDrive\\桌面\\mathTEACH\\mathTEACH\\mathTEACHSPACE\\a.pdf')
    elif a=='SAVE':
        fid=open('FirstWin.txt','w',encoding='utf-8')
        fid.write(TX.get(1.0,tk.END))
        fid.close()
    elif a=='LOAD':
        s=open('FirstWin.txt','r',encoding='utf-8').read()
        TX.delete(1.0,tk.END)
        TX.insert(1.0,s)
    else:
        cmdEset(a)

numList=['0','1','2','3','4','5','6','7','8','9']
Crtl=['Clear','+','-','*','/','Enter','Excute','OpenPdf','SAVE','LOAD']

DX=1./10

i=0
for x in numList: 
    B=tk.Button(win)
    B.configure(text=x)
    B.place(relx=i*DX,rely=0.2,relwidth=DX,relheight=0.1)
    B.configure(command=lambda a=x:cmdEset(a))
    i=i+1


i=0
for x in Crtl:
    B=tk.Button(win)
    B.configure(text=x)
    B.place(relx=i*DX,rely=0.3,relwidth=DX,relheight=0.1)
    B.configure(command=lambda a=x:cmdCRTL(a))
    i=i+1

TX=tk.Text(win)
TX.place(relx=0,rely=0.4,relwidth=1,relheight=0.5)

    
win.mainloop()
