# pip install pyotp   // Sirve para generar la autenticación TOTP
# pip install qrcode  // Sirve para generar el Código QR 
# pip install pillow  // Me permitira mostrar la imagen del QR  
import pyotp
import qrcode
from PIL import Image


#Genera un secreto de manera aleatoria
secreto = pyotp.random_base32()

# Permite crear el OTP de autenticación
totp_object = pyotp.TOTP(secreto)

# Aqui pondríamos el nombre de nuestra aplicación
totp = totp_object.provisioning_uri(name = "Tarea 2", issuer_name="M8T2 - TOTP")
print("Mi link TOTP es: ",totp)

# Aquí convertimos el link totp a código QR
qr_imagen = qrcode.make(totp)
nombre_archivo = secreto + ".png"
qr_nombre_archivo = open(nombre_archivo, 'wb')
qr_imagen.save(qr_nombre_archivo)
qr_nombre_archivo.close()

#mostramos la imagen del código QR
mostrar_qr = "./"+nombre_archivo
Image.open(mostrar_qr).show()



# Compara el PIN temporal de Google Authenticator con el SECRETO del servidor
# Nos responderá si la validación a sido correcta o no.
otp = input("Ingresa el PIN de Google Authenticator: " )
valid = totp_object.verify(otp)
print(valid)