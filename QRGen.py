""" creacion de Qr con python  """

import qrcode

# Dirección web que quieres codificar
url = input("Ingrese la direccion web: ")
nombre = input("Ingrese el nombre del archivo: ")
# url = "https://s6.cademonline.cl/index.php/136431?newtest=Y&lang=es"

# Crear el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear la imagen
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Redimensionar a 900x900 px
img = img.resize((900, 900))

# Guardar como PNG
img.save(nombre+".png")
print("QR generado con éxito.")