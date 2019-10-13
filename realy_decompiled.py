import struct
import sys
args = sys.argv
import serpent
mod_fix = 4294967295

def get_next_key(current_key, current_byte):
    a = current_byte + current_key
    a = (a << 12) + a + 2127912214 & mod_fix
    a = a >> 19 ^ a ^ 3345072700
    a = (a << 5) + a + 374761393 & mod_fix
    a = a << 9 ^ a - 744332180
    a = (a << 3) + a - 42973499 & mod_fix
    a = a >> 16 ^ a ^ 3042594569
    return a


def encrypt(data, bytes_key):
    key = struct.unpack('=L', bytes_key)[0]
    data = bytearray(data)
    for i in range(len(data)):
        data[i] ^= key & 255
        key = get_next_key(key, data[i])
    
    return bytes(data)


def decrypt(data, bytes_key):
    key = struct.unpack('=L', bytes_key)[0]
    data = bytearray(data)
    for i in range(len(data)):
        old_byte = data[i]
        data[i] ^= key & 255
        key = get_next_key(key, old_byte)
    
    return bytes(data)

encrypted_flag = [
    62,
    125,
    128,
    30,
    59,
    77,
    9,
    125,
    32,
    40,
    187,
    190,
    227,
    207,
    120,
    195,
    88,
    210,
    27,
    20,
    147,
    218,
    153,
    83,
    197]
KEY = 'SAFE'
if type(encrypted_flag) == list:
    print "Hello, you've received message, but it seems to be encrypted! Use our tool to decrypt it."
else:
    print ''.join(list(map(lambda x: chr(x) if type(x) == int else str(x), encrypted_flag)))
