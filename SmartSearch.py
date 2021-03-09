from tkinter import*
import webbrowser as wb
win=Tk()
win.geometry("400x100+400+70")
win.title("Smart Search")

var=IntVar()
def go():
    sec=str(var.get())
    
    if txt.get()=="" or txt.get()==" ":
        print("Bos")
    else:
        if sec=="1":
            wb.open("https://www.google.com/search?client=opera&q="+txt.get()+"&sourceid=opera&ie=UTF-8&oe=UTF-8")
        
        elif sec=="2":
            
            wb.open("https://www.youtube.com/results?search_query="+txt.get())
        
        if sec=="3" :
            wb.open("https://www.n11.com/arama?q="+txt.get())


lbl=Label(win,text="Aranacak kelimeyi girin.")
lbl.pack()
txt=Entry(win,bd=4,width=55,font=30)
txt.pack()
rad1=Radiobutton(win,text="Google",variable=var,value=1,command=go,font=18)
rad1.pack(side=LEFT)
rad2=Radiobutton(win,text="Youtube",variable=var,value=2,command=go,font=18)
rad2.pack(side=LEFT)
rad3=Radiobutton(win,text="n11",variable=var,value=3,command=go,font=18)
rad3.pack(side=LEFT)


label=Label(win)
label.pack(side=BOTTOM)
win.mainloop()