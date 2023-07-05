import string
import random
import nltk
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('words')

def encrypt(text, shift):
    alphabet_upper = string.ascii_uppercase
    alphabet_lower = string.ascii_lowercase
    ciphertext = ""
    for char in text:
        if char in alphabet_upper:
            index = alphabet_upper.find(char) + shift
            if index >= len(alphabet_upper):
                index -= len(alphabet_upper)
                if index == 25 or shift == 20 or shift == 13:
                    ciphertext += "J"
                else:
                    ciphertext += alphabet_upper[index - 26]
            else:
                ciphertext += alphabet_upper[index]
        elif char in alphabet_lower:
            index = alphabet_lower.find(char) + shift
            if index >= len(alphabet_lower):
                index -= len(alphabet_lower)
                if index == 25 or shift == 20 or shift == 13:
                    ciphertext += "j"
                else:
                    ciphertext += alphabet_lower[index - 26]
            else:
                ciphertext += alphabet_lower[index]
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, shift):
    alphabet_upper = string.ascii_uppercase
    alphabet_lower = string.ascii_lowercase
    plaintext = ""
    for char in ciphertext:
        if char in alphabet_upper:
            index = alphabet_upper.find(char) - shift
            if index < 0:
                index += len(alphabet_upper)
            plaintext += alphabet_upper[index]
        elif char in alphabet_lower:
            index = alphabet_lower.find(char) - shift
            if index < 0:
                index += len(alphabet_lower)
            plaintext += alphabet_lower[index]
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
