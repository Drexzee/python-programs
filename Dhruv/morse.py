# hello there, this is the tool where you can change the message into a morse code by using different characters for the original message and vice-versa. 
# Mapping English letters to custom symbols
custom_code = {
    'a': '(',  'b': ')',  'c': '#',  'd': '$',  'e': '%',
    'f': '^',  'g': '&',  'h': '*',  'i': '!',  'j': '~',
    'k': '-',  'l': '+',  'm': '=',  'n': '{',  'o': '}',
    'p': '[',  'q': ']',  'r': ':',  's': ';',  't': '"',
    'u': '<',  'v': '>',  'w': '?',  'x': '/',  'y': '|',
    'z': '`',  ' ': '_'
}

reverse_code = {}
for key in custom_code:
    value = custom_code[key]
    reverse_code[value] = key

def encode(text):
    text = text.lower()
    text.lower()
    encoded = ''
    for char in text:
        if char in custom_code:
            encoded += custom_code[char]
        else:
            encoded += '?' #unknown character
    return encoded        


def decode(code):
    decoded = ''
    for symbol in code:
        if symbol in reverse_code:
            decoded += reverse_code[symbol]
        else:
            decoded += '?' # unknown symbol 
    return decoded          

# Simple terminal UI
def main():
    print("=== Custom Morse Encoder / Decoder ===")
    print("[1] Encode a message")
    print("[2] Decode a message")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        user_input = input("Enter message to encode: ")
        result = encode(user_input)
        print("Encoded message:", result)
    elif choice == '2':
        user_input = input("Enter code to decode: ")
        result = decode(user_input)
        print("Decoded message:", result)
    else:
        print("Invalid choice. Please run again.")

# Run the program
main()


