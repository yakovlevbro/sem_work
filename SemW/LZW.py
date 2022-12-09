



def compress(uncompressed):
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = chr(dict_size)
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = result = compressed.pop(0)
    for i in compressed:
        if i in dictionary:
            entry = dictionary[i]
        elif i == chr(dict_size):
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % i)
        result += entry

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result



def encode(message):
    message = message + "%"
    table = [message[i:] + message[:i] for i in range(len(message))]
    table = sorted(table)

    last_column = [row[-1:] for row in table]
    bwt = ''.join(last_column)
    return bwt


def decode(bwt):
    table = [""] * len(bwt)
    for i in range(len(bwt)):
        table = [bwt[i] + table[i] for i in range(len(bwt))]
        table = sorted(table)

    inverse_bwt = [row for row in table if row.endswith("%")][0]
    inverse_bwt = inverse_bwt.rstrip("%")
    return inverse_bwt



def full_lzw_compress(message):
    code = encode(message)

    compressed = compress(code)
    print(compressed)
    for i in range(len(compressed)):
        compressed[i] = from_decimal_to_binary(ord(str(compressed[i])), 10)
    return compressed


def full_lzw_decompress(compressed):
    for i in range(len(compressed)):
        compressed[i] = chr(from_binary_to_decimal(compressed[i]))

    decompressed = decompress(compressed)
    return decode(decompressed)


if __name__ == "__main__":

	  message = 'testcode'
    compr = full_lzw_compress(message=message)
    print(compr)
    print(message == full_lzw_decompress(full_lzw_compress(message=message))
