alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p',  'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print()
print('-'*20)
print()


def ceasar(start_text, shift_amount, cipher_direction):
    word = ''
    if cipher_direction == 'decode':
            shift_amount *= -1
    for letra in start_text:
        position = alphabet.index(letra)
        
        new_position = position + shift_amount
        new_letra = alphabet[new_position]
        word += new_letra
    print(f'The {cipher_direction} text is {word}')


ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
