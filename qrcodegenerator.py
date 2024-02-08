import qrcode as qr
qrcode=qr.make("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
qrcode.save("Gmail.png")
