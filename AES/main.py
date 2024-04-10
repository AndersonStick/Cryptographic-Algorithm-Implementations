import os, base64
from pyaes import AESModeOfOperationCTR

imageName = "crypto"
key = "1234567890123456"

# ----------------------------------------------------------------

imageName = imageName.encode()
key = key.encode()

with open(imageName.decode() + ".png", mode='rb') as file:
# with open(imageName, mode='rb') as file:
    
    imageRaw = file.read()
    decryptedImage = imageName.decode() + "Decrypted.png"

    print("\nImagen original representada en bits (Bits 1 al 64): \n", imageRaw[0:64], "\n")

    encrypted = AESModeOfOperationCTR(key).encrypt(imageRaw)
    print("Imagen encriptada con AES (Bits 1 al 64): \n", encrypted[0:64], "\n")

    encoded64 = base64.standard_b64encode(encrypted)
    print("Codificacion con base64 (Bits 1 al 64): \n", encoded64[0:64], "\n")

    decoded64 = base64.standard_b64decode(encoded64)
    print("Decodificacion con base64 (Bits 1 al 64): \n", decoded64[0:64], "\n")

    decrypted = AESModeOfOperationCTR(key).decrypt(decoded64)
    print("Imagen desencriptada con AES (Bits 1 al 64): \n", decrypted[0:64])
    
    with open(decryptedImage, "wb") as file:
        file.write(decrypted)
        file.close()

    os.system("start " + decryptedImage)