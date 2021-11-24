# Programmer: Roope Turkki
# Date: 24/11/2021

def getIndex(charset,character):
    for i in range(len(charset)):
        if character == charset[i]:
            return i

def getChar(charset, index):
    return charset[index]
        
def encrypt(string, key = 21):
    encrypted_string = ""
    print()
    key = int(key)
    charset = "0abcdefghijklmnopqrstuvwxyzåäö! "
    print("original, original binary ==> encrypted binary, encrypted character")
    for character in string:
        index = getIndex(charset,character)
        encrypted = index^key
        binary_encrypted = bin(encrypted)[2:]
        while(len(str(binary_encrypted)) != 5):
            binary_encrypted = "0" + str(binary_encrypted) 
        index_bin = str(bin(index)[2:])
        while(len(index_bin) != 5):
            index_bin = "0" + index_bin
        char = getChar(charset, encrypted)
        print(character, index_bin + " ==>", binary_encrypted, char)
        encrypted_string += char
    print(f"'{string}' xor-encrypted with key {key} is '{encrypted_string}'")

def decrypt(encrypted, key = 21):
    print()
    charset = "0abcdefghijklmnopqrstuvwxyzåäö! "
    for character in encrypted:
        index = getIndex(charset, character)
        decrypted = index^int(key)
        binary_decrypted = bin(decrypted)[2:]
        while(len(str(binary_decrypted)) < 5):
            binary_decrypted = "0" + str(binary_decrypted) 
        char = getChar(charset, decrypted)
        print(character, binary_decrypted, char)
        
def main():
    while(True):
        question = input("Do you want to encrypt or decrypt? (e/d): ")

        if question == "e":
            string = input("What do you want to encrypt: ")
            key = input("Give a key (leave blank to use default): ")
            if key == '':
                encrypt(string)
                break
            else:
                encrypt(string, key)
                break
        elif question == "d":
            string = input("What do you want to decrypt: ")
            key = input("Give a key (leave blank to use default): ")
            if key == '':
                decrypt(string)
                break
            else:
                decrypt(string, key)
                break
        else:
            print("Unknown input, try again!")



if __name__ == "__main__":
    main()
