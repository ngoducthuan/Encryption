from generateKey import *
import sys


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.set_int_max_str_digits(5000)

encode_key, decode_key, n = rsa_key()

def encode(message):
    """
        Encode each character in massage
    """
    #Convert message to list character
    list_message = list(message)
    #Init list to store each character after encryption
    encode_list = []
    #Encryption each character in list then store it to encode_list
    for character in list_message:
        encode_character = ord(character) ** encode_key % n
        encode_list.append(encode_character)
    return encode_list 

def decode(encode_list):
    #Init list to store each character after decryption
    s = []
    #Decryption each character
    for enc_character in encode_list:
        dec_character = enc_character ** decode_key % n
        s.append(chr(dec_character))
    return ''.join(s)  # Nối các ký tự lại với nhau

if __name__ == "__main__":
    message = "Ngô Đức Thuận"
    encode_message = encode(message)
    print(encode_message)
    decode_message = decode(encode_message)
    print(decode_message)
