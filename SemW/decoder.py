# FANO DECODING

import os


def split(p, root="", r_ind=0):
    global dictionary

    if len(p) == 1:
        if not root and not r_ind:
            dictionary[alphabet[0]: "0"]
            return 1

        dictionary[alphabet[r_ind]] = root
        return 1

    ind = 1
    while abs(sum(p[:ind]) - sum(p[ind:])) > abs(sum(p[:ind+1]) - sum(p[ind+1:])):
        ind += 1
    split(p[:ind], root+"1", r_ind=r_ind)
    split(p[ind:], root+"0", r_ind=r_ind + ind)


def main():
    global dictionary
    global alphabet

    if os.path.exists("decoder_alphabet.txt"):
        with open("decoder_alphabet.txt", "r") as file:
            alphabet = file.readline().split()
            p = file.readline().replace(",", ".").split()
            p = list(map(float, p))

    print()
    a = list(zip(alphabet, p))
    new_alphabet = []
    new_p = []
    for i in sorted(a, key=lambda x:x[1], reverse=True):
        new_alphabet.append(i[0])
        new_p.append(i[1])
    alphabet = new_alphabet
    p = new_p
    print(f"Алфавит из файла: {', '.join(alphabet)}")
    print()
    dictionary = {}
    split(p)
    print(f"Словарь из алфавита: {dictionary}")
    print()
    dictionary = {value: key for key, value in dictionary.items()}
    data = input("Введите данные для декодирования: ")
    print()
    result = ""
    begin = 0
    for ind in range(1, len(data)+1):
        symbol_bin = data[begin:ind]
        symbol = dictionary.get(symbol_bin)
        if symbol:
            result += symbol
            begin = ind

    print(f"Декодированные данные: {result}")

if __name__ == "__main__":
    main()
