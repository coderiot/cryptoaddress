#!/usr/bin/env python
# encoding: utf-8

import hashlib

import string

import base58


versions = {'btc': {'pub': 0,
                    'priv': 128},
            'ltc': {'pub': 48,
                    'priv': 176},
            'nmc': {'pub': 52,
                    'priv': 180},
            'ppc': {'pub': 55,
                    'priv': 183},
            'ixc': {'pub': 138,
                    'priv': 10},
            'nvc': {'pub': 8,
                    'priv': 136},
            'ftc': {'pub': 14,
                    'priv': 142},
           }


def dhash(s):
    """Compute double sha256 digest.

    :s: string,
    :returns: string, double sha256 digest

    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


#def hash160(s):
    #h = hashlib.new('ripemd160')
    #h.update(hashlib.sha256(s).digest())
    #return h.digest()

def from_hash160(h160, currency='btc', typ='pub', version=None):
    """Create crypto currency address from hash160 digest.

    :h160: string, digest hash160 to create address from.
    :currency: string, three letter code for the currency
    :typ: string, type of address 'priv' for private addresses
                  or 'pub' for public addresses
    :version: int, prefix for any other currency,
                   if set params currency and typ are ignored
    :returns: string, Base58 encoded address

    """
    if all(c in string.hexdigits for c in h160):
        h160 = h160.decode('hex')

    currency = currency.lower()

    if version is None:
        version = versions[currency][typ]

    if currency not in versions.keys():
        raise Exception('Currency %s is unknown.' % currency)

    h160 = chr(version) + h160
    h = dhash(h160)
    addr = h160 + h[0:4]

    pad = 0
    for c in h160:
        if c == chr(0):
            pad += 1
        else:
            break

    return base58.alphabet[0] * pad + base58.b58encode(addr)


def to_hash160(addr):
    """@todo: Docstring for address_to_hash160

    :addr: string, Base58 encoded crypto currency address
    :returns: string, hash160 generated the address
                      without version and checksum.

    """
    return base58.b58decode(addr)[1:-4].encode('hex')


def validate(addr):
    """Validate crypto currency address.

    :addr: string, base58 encoded address
    :returns: bool, if valid or not

    """
    # check if base58
    try:
        dec_addr = base58.b58decode(addr)
    except:
        return False

    # checksum check
    return dec_addr[-4:] == dhash(dec_addr[:-4])[:4]


def detect(addr):
    """Detect the currency type of an address.

    :addr: string, cryptocurrency address
    :returns: dict with name of currency and type public or private.

    """
    # check for valid address
    if not validate(addr):
        raise Exception('Invalid address.')

    version = ord(base58.b58decode(addr)[0])
    res = {'currency': None, 'type': None}
    for c, p in versions.items():
        if p['pub'] == version:
            res['currency'] = c
            res['type'] = 'pub'
        elif p['priv'] == version:
            res['currency'] = c
            res['type'] = 'priv'

    return res


def convert(addr, to):
    """Convert crypto currency address to another.

    :addr: string, base58 encoded address
    :to: string, currency code
    :returns: string, base58 encoded address for new currency

    """
    if to not in versions.keys():
        raise Exception('Currency %s is unknown.' % to)

    det = detect(addr)
    to = to.lower()

    h160 = to_hash160(addr)
    return from_hash160(h160, to, typ=det['type'])
