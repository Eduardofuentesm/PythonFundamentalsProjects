from distutils.log import info
import qrcode

qr = qrcode.QRCode(
    version= 1,
    error_correction= qrcode.constants.ERROR_CORRECT_H,
    box_size= 10,
    border= 4
)

info = "Este codigo esta bonito"

qr.add_data(info)
qr.make(fit=True)

imagen = qr.make_image()

imagen.save('codigo.png')

# Desde la terminal puedes escribir:
# qr "Hola, este es mi mensaje" > codigo.png