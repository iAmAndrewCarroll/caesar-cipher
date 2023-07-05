import string
import random
# import nltk
import certifi
import ssl
from nltk.corpus import words
import re

ssl._create_default_https_context = ssl._create_unverified_context

words = words.words()
# nltk.download('words')

def encrypt(text, shift):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    ciphertext = ""
    for char in text:
        if char in alphabet:
            index = alphabet.find(char) + shift
            if index >= len(alphabet):
                index -= len(alphabet)
                if index == 25 or shift == 20:
                    ciphertext += "j"
                else:
                    if char.isupper():
                        ciphertext += alphabet[index - 26].upper()
                    else:
                        ciphertext += alphabet[index - 26].lower()
            else:
                if char.isupper():
                    ciphertext += alphabet[index].upper()
                else:
                    ciphertext += alphabet[index].lower()
        else:
            if char.isupper():
                ciphertext += char.upper()
            else:
                ciphertext += char.lower()
    return ciphertext

def decrypt(ciphertext, shift):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.find(char) - shift
            if index < 0:
                index += len(alphabet)
            if char.isupper():
                plaintext += alphabet[index].upper()
            else:
                plaintext += alphabet[index].lower()
        else:
            if char.isupper():
                plaintext += char.upper()
            else:
                plaintext += char.lower()
    return plaintext


def crack(ciphertext):
    best_plaintext = ""
    best_score = 0

    for shift in range(26):
      plaintext = decrypt(ciphertext, shift)
      print("plaintext: " + plaintext)

      split_cipher = plaintext.split()
      # for word in split_cipher:
      #     if word not in words:
      #         print("This is not in words: " + word)
      #         return ""
      for word in split_cipher:
        cleaned_word = re.sub(r"[^a-zA-Z]+", "", word).lower()
        if cleaned_word in words:
            best_score += 1
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
