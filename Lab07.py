from sys import exit

def vigenere_head(alphabet):
    return list(' ') + list(alphabet)

def vigenere_sq(alphabet):
    alphabet = list(alphabet)
    sq_list = [vigenere_head(alphabet)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            print(f'{'|---'*len(row)}|')

def letter_to_index(letter, alphabet):
    return alphabet.find(letter)

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return ((letter_to_index(key_letter, alphabet) +
             letter_to_index(plaintext_letter, alphabet)) % len(alphabet))

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text.append(' ')
        elif c in alphabet:
            cipher_text.append(index_to_letter(vigenere_index(key[counter % len(key)], c, alphabet), alphabet))
            counter += 1
    return ''.join(cipher_text)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    return index_to_letter((((letter_to_index(cipher_letter, alphabet))
                            - letter_to_index(key_letter, alphabet)) % len(alphabet)), alphabet)

def decrypt_vigenere(key_list, cipher_text, alphabet):
    plaintext = []
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plaintext.append(' ')
        elif c in alphabet:
            plaintext.append(undo_vigenere_index(key_list[counter % len(key_list)], c, alphabet))
            counter += 1
    return ''.join(plaintext)

def enc_menu(key_list, alphabet, encrypted_list, key_used_list):
    if not key_list:
        print("No keys available. Please add keys.")
        return
    plaintext = input("Enter the text you would like to encrypt: ")

    key = key_list.pop(0)
    key_list.append(key)

    encrypted_list.append(encrypt_vigenere(key, plaintext, alphabet))
    key_used_list.append(key)


def dec_menu(key_list, alphabet, encrypted_list, key_used_list):
    if not key_list:
        print("No keys available. Please add keys.")
        return

    key = key_list.pop(0)
    key_list.append(key)

    for i, cipher_text in enumerate(encrypted_list):
        key = key_used_list[i]
        decrypted_text = decrypt_vigenere(key, cipher_text, alphabet)
        print(f"Decrypted text: {decrypted_text} (Key: {key})")
    #for cipher_text in encrypted_list:
    #    print(decrypt_vigenere(key, cipher_text, alphabet))

def dec_dump_menu(encrypted_list):
    for cipher_text in encrypted_list:
        print(cipher_text)

def getkeys_menu(key_list):
    new_key = input("Enter a new encryption key: ").strip()
    if new_key:
        key_list.append(new_key)
        print(f"Key '{new_key}' added successfully!")
    else:
        print("Invalid key input. Try again.")

def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    # key = 'FONDUE'
    # message = 'Semi important secret message'
    encrypted_list = []
    key_list = []
    key_used_list = []

    menu = [
        ['1). Encrypt', enc_menu, [key_list, alphabet, encrypted_list, key_used_list]],
        ['2). Decrypt', dec_menu, [key_list, alphabet, encrypted_list, key_used_list]],
        ['3). Dump Decrypt', dec_dump_menu, [encrypted_list]],
        ['4). Get Keys', getkeys_menu, [key_list]],
        ['5). Quit', exit, [0]]
    ]
    while True:
        print("-"*80)
        for menu_item in menu:
            print(menu_item[0])
        try:
            choice = int(input("Make your choice"))
            if not (0 < choice <= len(menu)):
                print("Improper choice")
            else:
                menu[choice - 1][1](*menu[choice - 1][2])
        except ValueError as ignored:
            print("Improper choice, you must enter an integer between 1 and 5")

    #for _ in range(3):
    #    encrypted_list.append(
    #        menu[0][1](*menu[0][2]))

    #menu[3][1](*menu[3][2])
    #print('dont print')
    #menu[1][1](*menu[1][2])
    #menu[2][1](*menu[2][2])
    # print(vigenere_sq(alphabet))
    # vigenere_sq_print(vigenere_sq(alphabet))
    # print(letter_to_index('c', alphabet  ))
    # print(vigenere_index('b', 'b', alphabet))
    # print(decrypt_vigenere(key, "Xszl CquCEwury GrfLiy ArvMels", alphabet))
if __name__ == '__main__':
    main()
