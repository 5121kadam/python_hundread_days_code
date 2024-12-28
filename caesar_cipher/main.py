alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message here:\n").lower().replace(" ", "")
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def caesar(text, shift, encode_or_decode):
    output_text = ""
    for letter in text:
        if encode_or_decode == "decode":
            shift *= -1
        shifted_index = alphabet.index(letter) + shift
        shifted_index %= len(alphabet)
        output_text += alphabet[shifted_index]
    return output_text

print(caesar(text, shift, direction))
    