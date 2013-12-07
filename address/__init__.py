#!/usr/bin/env python
# encoding: utf-8

import hashlib

import string

from collections import namedtuple

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
            'gdc': {'pub': 97,
                    'priv': 225},
            'tag': {'pub': 65,
                    'priv': 193},
            'dgc': {'pub': 30,
                    'priv': 158},
            'zet': {'pub': 80,
                    'priv': 224},
            'xjo': {'pub': 43,
                    'priv': 143},
            'wdc': {'pub': 73,
                    'priv': 201},
            'xpm': {'pub': 23,
                    'priv': 151},
            'qrk': {'pub': 58,
                    'priv': 128},
            'pts': {'pub': 56,
                    'priv': 184},
            'mec': {'pub': 50,
                    'priv': 178},
            'frc': {'pub': 0,
                    'priv': 128},
            'trc': {'pub': 0,
                    'priv': 128},
            'bqc': {'pub': 85,
                    'priv': 213},
            'anc': {'pub': 23,
                    'priv': 151},
            'i0c': {'pub': 105,
                    'priv': 128},
            'sbc': {'pub': 125,
                    'priv': 253},
            'btb': {'pub': 25,
                    'priv': 153},
            'mnc': {'pub': 50,
                    'priv': 178},
            'bte': {'pub': 18,
                    'priv': 128},
            'ifc': {'pub': 102,
                    'priv': 230},
            'col': {'pub': 2,
                    'priv': 130},
            'tix': {'pub': 19,
                    'priv': 147},
            'cnc': {'pub': 28,
                    'priv': 156},
            'yac': {'pub': 77,
                    'priv': 205},
            'dtc': {'pub': 30,
                    'priv': 158},
            'zcc': {'pub': 80,
                    'priv': 208},
            'cent': {'pub': 55,
                    'priv': 183},
            'lky': {'pub': 47,
                    'priv': 175},
            'frc': {'pub': 35,
                    'priv': 163},
            'krc': {'pub': 79,
                    'priv': 207},
            'fst': {'pub': 96,
                    'priv': 224},
            'clr': {'pub': 28,
                    'priv': 128},
            'cgb': {'pub': 11,
                    'priv': 139},
            'nec': {'pub': 53,
                    'priv': 181},
            'emd': {'pub': 34,
                    'priv': 162},
            'adt': {'pub': 2,
                    'priv': 130},
            'net': {'pub': 112,
                    'priv': 240},
            'dvc': {'pub': 0,
                    'priv': 128},
            'bet': {'pub': 25,
                    'priv': 143},
            'osc': {'pub': 2,
                    'priv': 130},
            'tek': {'pub': 26,
                    'priv': 164},
            'dem': {'pub': 53,
                    'priv': 181},
            'uno': {'pub': 130,
                    'priv': 224},
            'tgc': {'pub': 127,
                    'priv': 224},
            'ixc': {'pub': 138,
                    'priv': 10},
           }


def dhash(s):
    """Compute double sha256 digest.

    :s: string,
    :returns: string, double sha256 digest

    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def sha256hash160(s):
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(s).digest())
    return h.digest()


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

    if currency not in versions.keys():
        raise Exception('Currency %s is unknown.' % currency)

    if version is None:
        version = versions[currency][typ]

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
    :returns: list of dicts with name of currency and type public or private.

    """
    # check for valid address
    if not validate(addr):
        raise Exception('Invalid address.')

    version = ord(base58.b58decode(addr)[0])
    det = []
    for c, p in versions.items():
        res = {'currency': None, 'type': None}
        if p['pub'] == version:
            res['currency'] = c
            res['type'] = 'pub'
            det.append(res)
        elif p['priv'] == version:
            res['currency'] = c
            res['type'] = 'priv'
            det.append(res)

    return det


def convert(addr, to, typ='pub'):
    """Convert crypto currency address to another.

    :addr: string, base58 encoded address
    :to: string, currency code
    :typ: string, address type: priv or pub
    :returns: string, base58 encoded address for new currency

    """
    if to not in versions.keys():
        raise Exception('Currency %s is unknown.' % to)

    h160 = to_hash160(addr)
    return from_hash160(h160, to, typ=typ)


Key = namedtuple('Key', ['b58', 'hex'])


def generate(currency='btc', secret=None, compressed=False):
    """Generate address pair for currency. (Default: BTC)

    :currency: string, 3 letter currency code
    :secret: string, seed for private address
    :compressed: bool, if key pair is on compresses format or not
    :returns: tuple, (private_key, public_key) containing representation in hex and base58 format.

    """
    from ecdsa import SigningKey, SECP256k1

    if secret:
        h = hashlib.sha256(secret).hexdigest()
        secret_exp = int(h, 16)
        sk = SigningKey.from_secret_exponent(secret_exp, curve=SECP256k1)
    else:
        sk = SigningKey.generate(curve=SECP256k1)

    priv = sk.to_string()
    pub = sk.get_verifying_key()

    if compressed:
        priv = priv + '\x01'
        if pub.pubkey.point.y() % 2:
            prefix = '\x03'
        else:
            prefix = '\x02'
        pub = prefix + pub.to_string()[0:32]
    else:
        pub = '\x04' + pub.to_string()

    priv_hex = priv.encode('hex')
    priv_b58 = from_hash160(priv_hex, typ='priv', currency=currency)

    pub_hex = sha256hash160(pub).encode('hex')
    pub_b58 = from_hash160(pub_hex, currency=currency)

    return Key(hex=priv_hex, b58=priv_b58), Key(hex=pub_hex, b58=pub_b58)
