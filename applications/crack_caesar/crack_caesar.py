# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {value: key for key, value in encode_table.items()}

for key, value in encode_table.items():
    decode_table[value] = key


def read_file():
    file = open("ciphertext.txt", "r")
    return file.read()


def encrypt(s):
    result = ''

    for c in s:
        c = c.upper()

        if c.isalpha():
            result += encode_table[c]

        else:
            result += c

    return result


def decrypt(s):
    result = ''

    for c in s:
        c = c.upper()

        if c.isalpha():
            if c in decode_table:
                result += decode_table[c]

        else:
            result += c

    print(f"result: {result}")
    return result


print("encoded:")
print(read_file())
print("decoded:")
print(decrypt(read_file()))
