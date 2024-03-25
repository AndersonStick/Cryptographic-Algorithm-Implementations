import pyDes, os, base64

# ----------------------------------------------------------------
# --- Cifrado DES y codificación Base64 aplicados a una Imagen ---
# ----------------------------------------------------------------

# Nombre de la imagen y llave de 8 bytes:

imageName = "vladimir"
key = "24686420"

# ----------------------------------------------------------------

with open(imageName + ".jpg", mode='rb') as file:
    
    imageRaw = file.read()
    decryptedImage = imageName + "Decrypted.jpg"

    print("\nImagen original representada en bits (Bits 1 al 64): \n", imageRaw[0:64], "\n")

    encrypted = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5).encrypt(imageRaw)
    print("Imagen encriptada con DES (Bits 1 al 64): \n", encrypted[0:64], "\n")

    encoded64 = base64.standard_b64encode(encrypted)
    print("Codificacion con base64 (Bits 1 al 64): \n", encoded64[0:64], "\n")

    toDecrypt = base64.standard_b64decode(encoded64)
    print("Decodificacion con base64 (Bits 1 al 64): \n", toDecrypt[0:64], "\n")

    decrypted = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5).decrypt(toDecrypt, padmode=pyDes.PAD_PKCS5)
    print("Imagen desencriptada con DES (Bits 1 al 64): \n", decrypted[0:64])
    
    with open(decryptedImage, "wb") as file:
        file.write(decrypted)
        file.close()

    os.system("start " + decryptedImage)