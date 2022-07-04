from letterdata import Document
from report import PdfReport
import os
import tkinter
import customtkinter
from PIL import Image, ImageTk



customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x650")
app.title("PDF letter")

img = ImageTk.PhotoImage(Image.open("paski.png"))
label_hello = customtkinter.CTkLabel(master=app,
                                    image=img,
                                    height=50,
                                    width=400,
                                    corner_radius=5,
                                    fg_color=("white", "gray38"),  # <- custom tuple-color
                                    justify=tkinter.LEFT)
label_hello.pack(padx=15, pady=15)


name = customtkinter.CTkEntry(master=app, placeholder_text="What is your name?",
                               corner_radius=5,
                               width=400,
                               height=50,)
name.pack(padx=20, pady=10)

title = customtkinter.CTkEntry(master=app, placeholder_text="What will be the title of the document?",
                               corner_radius=5,
                               width=400,
                               height=50,)
title.pack(padx=20, pady=10)


date = customtkinter.CTkEntry(master=app, placeholder_text="Enter the city and date in format: City, 00.00.0000",
                               corner_radius=5,
                               width=400,
                               height=50,)
date.pack(padx=20, pady=10)

address1 = customtkinter.CTkEntry(master=app, placeholder_text="Enter the address - street",
                               corner_radius=5,
                               width=400,
                               height=50,)
address1.pack(padx=20, pady=10)

address2 = customtkinter.CTkEntry(master=app, placeholder_text="Enter the address - postal code and city",
                               corner_radius=5,
                               width=400,
                               height=50,)
address2.pack(padx=20, pady=10)



paragraph = customtkinter.CTkEntry(master=app, placeholder_text="Type the main text - paragraph",
                               corner_radius=5,
                               width=400,
                               height=50)
paragraph.pack(padx=20, pady=10)

def create():
    the_document = Document(title.get(), date.get(), address1.get(), address2.get(), paragraph.get(), name.get())
    pdf_report = PdfReport(docname=f"{the_document.title}.pdf")
    pdf_report.generate(document=the_document)

button = customtkinter.CTkButton(master=app, text="Create a Letter", corner_radius=5, command=create)
button.configure(fg_color="#f1c232",
                hover_color="#3c78d8",
                text_color="#2D2D2D")
button.pack(padx=20, pady=10)
app.mainloop()
'''
the_document = Document(title, date, address1, address2, paragraph, name)
pdf_report = PdfReport(docname=f"{the_document.title}.pdf")
pdf_report.generate(document=the_document)


name = input("Hi! What is your full name, you would like to sign the document with ?: ")
title = input("What will be title of the document?: ")
date = input("Enter the city and date, which will appear in right top corner: ")
address1 = input("Enter address, street: ")
address2 = input("Enter address, postal code and city: ")
paragraph = input("Type body text - main paragraph: ")


the_document = Document(title, date, address1, address2, paragraph, name)

print(name)
print(title)
print(date)
print(address1)
print(address2)
print(paragraph)

'''
