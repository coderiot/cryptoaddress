#!/usr/bin/env python
# encoding: utf-8

from binascii import hexlify, unhexlify

alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def b58decode(s):
    """Decode string use Base58."""
    n = 0
    for c in s:
        if c not in alphabet:
            raise Exception('Character %r is not a valid base58 character' % c)
        n = n * 58 + alphabet.index(c)

    pad = 0
    for c in s:
        if c == alphabet[0]:
            pad += 1
        else:
            break

    h = "%x" % n

    if len(h) % 2:
        h = '0' + h

    return chr(0) * pad + unhexlify(h)


def b58encode(s):
    """Encode string use Base58."""
    # Convert big-endian bytes to integer
    n = int('0x0' + hexlify(s).decode('utf-8'), 16)

    # Divide that integer into bas58
    res = []
    while n > 0:
        n, r = divmod(n, 58)
        res.append(alphabet[r])
    res = ''.join(res[::-1])

    return res
