'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python wilson.py
    or if it doesn't work use this one:
        python3 wilson.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''


from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry, Radiobutton, Button, Style



class Wilson(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("WILSON")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        
        
        global num
        num = StringVar()
        
        
        global res
        res = StringVar()

        
		
        
      
		
        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter a number :", width=18,background='orange')
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=num,style='My.TEntry')
        entry1.pack(fill=X, padx=5, expand=True)
		
        
		
       

        
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        result = Label(frame2, textvariable=res, width=32,background='orange')
        result.pack(side=LEFT, padx=113, pady=5)

		
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        btntest = Button(frame3, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame3, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame3, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        elif msg == 'errc':
            tkinter.messagebox.showerror('Error!', 'Number must be greater than two')
       
			
    
        
    

    def test(self):
        try:
            
            
            n = int(num.get())
            
			
            if n<3:
                self.errorMsg('errc')
            
            else:
                p=1
                for k in range(1,n):
                    p=p*k
                s=0
                for k in range(1,n):
                    s=s+k
	                
                if p%s==n-1:
                    value="prime"
                    res.set(self.makeAsItIs(value))
                else:
                    value="composite"
                    res.set(self.makeAsItIs(value))
					
               

          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            num.set('')
            
            
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    s.configure('My.TRadiobutton', background='orange')
    s.map('My.TRadiobutton', background=[('active', '#FFC133')])
    root.geometry("300x86")
    wilson = Wilson(root)
    root.mainloop()

if __name__ == '__main__':
    main()