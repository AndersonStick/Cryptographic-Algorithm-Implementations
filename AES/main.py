import os, base64  # Importa los módulos os y base64
from pyaes import AESModeOfOperationCTR  # Importa la clase AESModeOfOperationCTR del módulo pyaes

imageName = "crypto"  # Nombre del archivo de imagen
key = "1234567890123456"  # Clave de cifrado AES

# ----------------------------------------------------------------

imageName = imageName.encode()  # Convierte el nombre de la imagen a bytes
key = key.encode()  # Convierte la clave a bytes

with open(imageName.decode() + ".png", mode='rb') as file:  # Abre el archivo de imagen en modo lectura binaria
# with open(imageName, mode='rb') as file:  # Esta línea podría ser una opción alternativa para abrir el archivo
    
    imageRaw = file.read()  # Lee el contenido del archivo de imagen
    decryptedImage = imageName.decode() + "Decrypted.png"  # Nombre del archivo de imagen desencriptado

    print("\nImagen original representada en bits (Bits 1 al 64): \n", imageRaw[0:64], "\n")  # Imprime los primeros 64 bits de la imagen original

    encrypted = AESModeOfOperationCTR(key).encrypt(imageRaw)  # Encripta la imagen utilizando AES
    print("Imagen encriptada con AES (Bits 1 al 64): \n", encrypted[0:64], "\n")  # Imprime los primeros 64 bits de la imagen encriptada

    encoded64 = base64.standard_b64encode(encrypted)  # Codifica la imagen encriptada en base64
    print("Codificacion con base64 (Bits 1 al 64): \n", encoded64[0:64], "\n")  # Imprime los primeros 64 bits de la codificación base64

    decoded64 = base64.standard_b64decode(encoded64)  # Decodifica la imagen encriptada en base64
    print("Decodificacion con base64 (Bits 1 al 64): \n", decoded64[0:64], "\n")  # Imprime los primeros 64 bits de la decodificación base64

    decrypted = AESModeOfOperationCTR(key).decrypt(decoded64)  # Desencripta la imagen utilizando AES
    print("Imagen desencriptada con AES (Bits 1 al 64): \n", decrypted[0:64])  # Imprime los primeros 64 bits de la imagen desencriptada
    
    with open(decryptedImage, "wb") as file:  # Abre un archivo para escribir el resultado desencriptado en modo binario
        file.write(decrypted)  # Escribe la imagen desencriptada en el archivo
        file.close()  # Cierra el archivo

    os.system("start " + decryptedImage)  # Abre el archivo de imagen desencriptado utilizando el programa predeterminado del sistema
