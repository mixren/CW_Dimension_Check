import tkinter as tk
from PIL import Image
from PIL import ImageTk
import os

class MyAboutWindow:
    TITLE = "About"

    def __init__(self, root):
        self.root = root

        self.root.title(self.TITLE)
        
        '''jpg = Image.open('./repo/comparison.jpg')
        #jpg = jpg.resize((20, 20))
        image = ImageTk.PhotoImage(jpg)
        label = tk.Label(self.root, image = image)
        label.pack(fill = "both", expand = "yes")'''
   
        '''text2 = tk.Text(root, height=20, width=50)
        scroll = tk.Scrollbar(root, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
        text2.tag_bind('follow',
                    '<1>',
                    lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
        text2.insert(tk.END,'\nWilliam Shakespeare\n', 'big')
        quote = """
        To be, or not to be that is the question:
        Whether 'tis Nobler in the mind to suffer
        The Slings and Arrows of outrageous Fortune,
        Or to take Arms against a Sea of troubles,
        """
        text2.insert(tk.END, quote, 'color')
        text2.insert(tk.END, 'follow-up\n', 'follow')
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)'''
