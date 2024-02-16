# -*- coding: utf-8 -*-
"""Taller OTP 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m4HHpdF0M-igZBlUbYaR13KLu2qFaaxa

# **FIRST CRIPTOGRAPHY HOMEWORK**
## Anderson Stick Barrera Tovar
### 1000623506

The One Time Pad (OTP) algorithm is a method of encryption that provides perfect secrecy when implemented correctly. It was invented in 1917 by Gilbert Vernam, though its formal proof of security was provided by Claude Shannon in 1949. The key concept behind OTP is the use of a random, secret key that is at least as long as the message being encrypted.

Here's how the OTP algorithm works:

1. **Key Generation**: A truly random key is generated. This key must be at least as long as the message to be encrypted and should never be reused for any other message.

2. **Encryption**: To encrypt a message, each character of the message is combined (usually XOR operation) with the corresponding character in the key. The resulting ciphertext is generated.

3. **Decryption**: Decryption is essentially the reverse process. Each character of the ciphertext is combined with the corresponding character in the key to retrieve the original message.

Key properties and characteristics of the One Time Pad algorithm:

- **Perfect Secrecy**: One Time Pad provides perfect secrecy, meaning that even with unlimited computational power, an attacker cannot gain any information about the plaintext without knowing the key. This property holds true if the key is truly random, is at least as long as the message, and is only used once.
  
- **Key Management**: The security of OTP depends heavily on the secrecy and randomness of the key. If the key is compromised or reused, the security of the encryption is lost. Therefore, key management is critical in OTP.
  
- **Vulnerabilities and Practical Limitations**: While theoretically secure, OTP has practical limitations and vulnerabilities. The primary challenge is the secure distribution of the key, as it must be distributed in a secure manner to both the sender and the receiver. Additionally, the key must be as long as the message, making it impractical for large messages.
  
- **Computational Efficiency**: While OTP offers perfect secrecy, it is not computationally efficient, especially for large volumes of data. The encryption and decryption process requires the same amount of time and effort as the length of the message itself.

Overall, the One Time Pad is a fascinating encryption algorithm that demonstrates the concept of perfect secrecy, but its practical application is limited due to challenges in key distribution and computational efficiency.

# **What is a One Time-Pad?**

**The one-time pad is an encryption technique that transforms plaintext to ciphertext.**

**Given a plaintext message, the one-time pad encrypts the plaintext with a randomly generated key that is at least as long as the length of the plaintext, if not longer. In order for the one-time pad to stay secure, a key that is generated randomly cannot be used more than once, hence the name of the encryption technique.**

$\text{One-Time Pad Encryption}: E(k, p) \rightarrow c$

$\text{One-Time Pad Decryption}: De(k, c) \rightarrow p$

$\text{Where: } E = \text{Encryption}, D = \text{Decryption}, k = \text{randomly generated key}, p = \text{plaintext}, c = \text{ciphertext}$

<sup>Source: Lecture - [Introduction to Cryptography](https://www.cs.purdue.edu/homes/ninghui/courses/Fall05/lectures/355_Fall05_lect09.pdf) from Purdue University by Ninghui Li</sup>

<sup>Source: Lecture - [Perfect Secrecy, One Time Pad, Randomness](https://www.cs.umd.edu/~gasarch/COURSES/456/F18/lecps/lecps.pdf) University of Maryland Course by William Gasarch</sup>
"""

import secrets
import string

"""The `secrets` and `string` libraries in Python serve specific purposes in the provided code to implement the One Time Pad (OTP) encryption algorithm.

1. **`secrets`**: This library is used to generate cryptographically secure random numbers. In the code, `secrets.choice()` is used to randomly select elements from a sequence (in this case, a range of numbers) to construct the OTP key. It's preferable to use `secrets` over `random` for security applications as `secrets` uses cryptographically secure entropy sources.

2. **`string`**: This library provides useful constants for ASCII characters. In the code, `string.ascii_lowercase` is used to obtain a string containing all lowercase letters of the English alphabet. This is used to build a dictionary that maps indices to alphabet letters, facilitating the encryption and decryption of messages.
"""

def generate_key(message_length):
    # Generate a random key with the same length as the message
    key = [secrets.choice(range(0, 26)) for _ in range(message_length)]
    return key

def otp(message, key):
    # Create a dictionary where keys are indices and values are lowercase letters of the alphabet
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}

    # Create a dictionary where keys are lowercase letters of the alphabet and values are indices
    inv_dict = {letter: index for index, letter in plain_dict.items()}

    # Convert the message to lowercase to ensure consistency
    message = message.lower()

    # Remove all characters that are not letters or numbers from the message
    message = ''.join(letter for letter in message if letter.isalnum())

    # Ensure that the key is the same length as the message
    key = key[:len(message)]

    # Encrypt the message using OTP
    encrypt_list = [(inv_dict[let] + k) % len(plain_dict) for let, k in zip(message, key)]

    # Return a list containing the encrypted message and the key used for encryption
    return [''.join([plain_dict[ind] for ind in encrypt_list])]

# Use Example:
message = 'Buenas tardes soy un mensaje cifrado por OTP'
key = generate_key(len(message))
print("Generated OTP Key:", key)

# Perform OTP encryption on the given message with a specified key
otp_cipher = otp(message, key)

# Print the encrypted message (cipher)
print(f'The one time pad cipher text: {otp_cipher}')

"""##Decryption"""

def otp_decrypt(ciphertext, key):
    # Create a dictionary where keys are indices and values are lowercase letters of the alphabet
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}

    # Create a dictionary where keys are lowercase letters of the alphabet and values are indices
    inv_dict = {letter: index for index, letter in plain_dict.items()}

    # Ensure that the key is the same length as the ciphertext
    key = key[:len(ciphertext)]

    # Decrypt the message using OTP
    decrypt_list = [(inv_dict[let] - k) % len(plain_dict) for let, k in zip(ciphertext, key)]

    # Return the decrypted message
    return ''.join([plain_dict[ind] for ind in decrypt_list])

# Decrypt the cipher text using the same key
decrypted_message = otp_decrypt(otp_cipher[0], key)
print(f'Decrypted message: {decrypted_message}')

"""# References
<sup>Source: Lecture - [Introduction to Cryptography](https://www.cs.purdue.edu/homes/ninghui/courses/Fall05/lectures/355_Fall05_lect09.pdf) from Purdue University by Ninghui Li</sup>

<sup>Source: Lecture - [Perfect Secrecy, One Time Pad, Randomness](https://www.cs.umd.edu/~gasarch/COURSES/456/F18/lecps/lecps.pdf) University of Maryland Course by William Gasarch</sup>


"""