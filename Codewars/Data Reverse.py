def data_reverse(data):
    bytes = [data[i:i+8] for i in range(0, len(data), 8)]

    rev_bytes = bytes[::-1]

    rev_data = [i for bytes in rev_bytes for i in bytes]

    return rev_data