import tkinter as tk
from tkinter import *

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title('Text Editor')
        
        self.text = tk.Text(master, font=('Arial', 18), wrap="word")
        self.text.pack(expand=True, fill='both')
        
        self.bold_button = tk.Button(master, text='Convert', command=self.bold_text)
        self.bold_button.pack(side='top')
        
        self.text.tag_configure('bold', font=('Arial', 18, 'bold'))
        
        # Add the binding for select all
        self.text.bind("<Control-Key-a>", self.select_all)
        self.text.bind("<Control-Key-A>", self.select_all)
   
    # Select all the text in textbox
    def select_all(self, event):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(INSERT, "1.0")
        self.text.see(INSERT)
        return 'break'
        
        
    def bold_text(self):
        paras = self.text.get('sel.first', 'sel.last').split('\n')
        for i, para in enumerate(paras, start=1):
            words = para.split()
            start = 0
            for word in words:
                print(start, len(word), word)
                self.text.tag_add('bold', f'{i}.{start}', f'{i}.{start + len(word)//2}')
                start += len(word)+1

        
                

if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
