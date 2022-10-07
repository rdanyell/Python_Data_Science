import sys

def caesar(code, phrase, n):
    if code == 'decode':
        n *= -1
    new_phrase = ''
    alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # run every symbol of the frase and if it's in alphabet1 or 2 we replace it 
    for i in range(len(phrase)):
        if phrase[i] in alphabet1:
            m = alphabet1.find(phrase[i])
            new_phrase += alphabet1[(n + m) % len(alphabet1)]
        elif phrase[i] in alphabet2:
            m = alphabet2.find(phrase[i])
            new_phrase += alphabet2[(n + m) % len(alphabet2)]
    # if the symbol is not in the alphabert1 or 2 just copy it
        else:
            new_phrase += phrase[i]

    print(new_phrase)

if __name__ == '__main__':
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        raise Exception("Error argument")
    if not sys.argv[2].isascii():
        raise Exception("Error: str not from ascii")
    try:
        n_shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Error: shift is not int")
    caesar(sys.argv[1], sys.argv[2], n_shift)