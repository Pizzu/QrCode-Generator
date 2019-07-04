import pyqrcode

name = input("Name: ")
surname = input("Surname: ")
org = input("Company: ")
tel = input("Phone number: ")
email = input("Email: ")
address = input("Address: ")

qr = pyqrcode.create("BEGIN:VCARD\r\n" +
"VERSION:4.0\r\n" +
f"N:{surname};{name};;\r\n" +
f"FN:{name} {surname}\r\n" +
f"ORG:{org}\r\n" +
f"TEL;TYPE=work,voice;Phone=uri:{tel}\r\n" +
f"EMAIL:{email}\r\n" +
f"ADR;TYPE=HOME;LABEL='\n{address};;\r\n" +
"END:VCARD\r\n")

qr.png(f'./Qrcodes/{name.replace(" ", "")}{surname.replace(" ", "")}Qrcode.png', scale=5, background='#391052', module_color='#cda434')

