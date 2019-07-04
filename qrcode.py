import pyqrcode
import tkinter as tk

def qrCode(name, surname, org, tel, email, address):
    qr = pyqrcode.create("BEGIN:VCARD\r\n" +
    "VERSION:4.0\r\n" +
    f"N:{surname};{name};;\r\n" +
    f"FN:{name} {surname}\r\n" +
    f"ORG:{org}\r\n" +
    f"TEL;TYPE=work,voice;Phone=uri:{tel}\r\n" +
    f"EMAIL:{email}\r\n" +
    f"ADR;TYPE=HOME;Address='\n{address};;\r\n" +
    "END:VCARD\r\n")
    qr.png(f'./Qrcodes/{name.replace(" ", "")}{surname.replace(" ", "")}Qrcode.png', scale=5, background='#391052', module_color='#cda434')
    print("Done")

#Constants
HEIGHT = 680
WIDTH = 780

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="Assets/QrCodeBg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#Main Frame
main_frame = tk.Frame(root, bg="black", bd=5)
main_frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.8, anchor="n")

#Name Frame
name_frame = tk.Frame(main_frame, bg="black", bd=3)
name_frame.place(relwidth=0.5, relheight=0.2)
name_label = tk.Label(name_frame, text="Name")
name_label.place(relwidth=0.3, relheight=0.5)
name_entry = tk.Entry(name_frame, font=40)
name_entry.place(rely=0.5,relwidth=1, relheight=0.5)

#Surname Frame
surname_frame = tk.Frame(main_frame, bg="black", bd=3)
surname_frame.place(relx=0.5, relwidth=0.5, relheight=0.2)
surname_label = tk.Label(surname_frame, text="Surname")
surname_label.place(relwidth=0.3, relheight=0.5)
surname_entry = tk.Entry(surname_frame, font=40)
surname_entry.place(rely=0.5,relwidth=1, relheight=0.5)

#Company Frame
org_frame = tk.Frame(main_frame, bg="black", bd=3)
org_frame.place(rely=0.3, relwidth=0.5, relheight=0.2)
org_label = tk.Label(org_frame, text="Company Name")
org_label.place(relwidth=0.5, relheight=0.5)
org_entry = tk.Entry(org_frame, font=40)
org_entry.place(rely=0.5,relwidth=1, relheight=0.5)

#Phone Number Frame
tel_frame = tk.Frame(main_frame, bg="black", bd=3)
tel_frame.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)
tel_label = tk.Label(tel_frame, text="Phone Number")
tel_label.place(relwidth=0.5, relheight=0.5)
tel_entry = tk.Entry(tel_frame, font=40)
tel_entry.place(rely=0.5,relwidth=1, relheight=0.5)

#Email Frame
email_frame = tk.Frame(main_frame, bg="black", bd=3)
email_frame.place(rely=0.6, relwidth=0.5, relheight=0.2)
email_label = tk.Label(email_frame, text="Email")
email_label.place(relwidth=0.3, relheight=0.5)
email_entry = tk.Entry(email_frame, font=40)
email_entry.place(rely=0.5,relwidth=1, relheight=0.5)
#Address Frame
address_frame = tk.Frame(main_frame, bg="black", bd=3)
address_frame.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.2)
address_label = tk.Label(address_frame, text="Address")
address_label.place(relwidth=0.3, relheight=0.5)
address_entry = tk.Entry(address_frame, font=40)
address_entry.place(rely=0.5,relwidth=1, relheight=0.5)

#Button
create_button = tk.Button(main_frame, text="Create Qrcode", font=40, command=lambda: qrCode(name_entry.get(),surname_entry.get(),org_entry.get(),tel_entry.get(),email_entry.get(),address_entry.get()))
create_button.place(relx=0.5, rely=0.9, relwidth=0.5, relheight=0.1, anchor="n")

root.mainloop()




