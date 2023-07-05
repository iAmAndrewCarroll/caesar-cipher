import string
import random
import nltk
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('words')

def encrypt(text, shift):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    ciphertext = ""
    for char in text:
        if char in alphabet:
            index = alphabet.find(char) + shift
            if index >= len(alphabet):
                index -= len(alphabet)
                ciphertext += alphabet[index - 26]
            else:
                ciphertext += alphabet[index]
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, shift):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.find(char) - shift
            if index < 0:
                index += len(alphabet)
            plaintext += alphabet[index]
        else:
            plaintext += char
    return plaintext

def crack(ciphertext):
    words = nltk.corpus.words.words()
    best_plaintext = ""
    best_score = 0
    for shift in range(26):
        plaintext = decrypt(ciphertext, shift)
        score = sum(word.strip().lower() in plaintext.lower() for word in words)
        if score > best_score:
            best_plaintext = plaintext
            best_score = score
    if best_score == 0:
        return ""
    else:
        return best_plaintext



def main():
    plaintext = "I can do nothing for you but work on myself...you can do nothing for me but work on yourself!"
    ciphertext = encrypt(plaintext, 10)
    print(f"Ciphertext: {ciphertext}")
    plaintext = crack(ciphertext)
    print(f"Plaintext: {plaintext}")

if __name__ == "__main__":
    main()
