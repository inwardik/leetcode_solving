def num_to_ip(num):
    hex_num = str(hex(num))[2:].rjust(8, '0')
    result = ''
    for segment in range(0, 8, 2):
        result = result + str(int(hex_num[segment:segment+2], 16))
        if segment < 6:
            result += '.'
    return result


def lcg(modulus=2**32, a=1664525, c=1013904223, seed=1):
    """Linear_congruential_generator"""
    total = modulus
    while total > 0:
        total -= 1
        seed = (a * seed + c) % modulus
        yield seed


for i in lcg(seed=1):
    print(num_to_ip(i))
