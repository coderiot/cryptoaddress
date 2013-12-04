#!/usr/bin/env python
# encoding: utf-8

import unittest

import address
import base58


def find_version():
    priv = "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
    pub = "c4c5d791fcb4654a1ef5e03fe0ad3d9c598f9827"

    print "Public version:\n"
    for i in range(256):
        addr = address.from_hash160(pub.decode('hex'), version=i)
        if addr.startswith('PSX'):
            print 'PPC pub version', i, addr
        elif addr.startswith('1Jw'):
            print 'BTC pub version', i, addr
        elif addr.startswith('LdA'):
            print 'LTC pub version', i, addr
        elif addr.startswith('NEW'):
            print 'NMC pub version', i, addr
        elif addr.startswith('xqa'):
            print 'IXC priv version', i, addr
        elif addr.startswith('4Xe'):
            print 'NVC priv version', i, addr
        elif addr.startswith('6wf'):
            print 'FTC priv version', i, addr

    print "\nPrivate version:\n"
    for i in range(256):
        addr = address.from_hash160(priv.decode('hex'), version=i)
        if addr.startswith('7AD'):
            print 'PPC priv version', i, addr
        elif addr.startswith('5KJ'):
            print 'BTC priv version', i, addr
        elif addr.startswith('6vc'):
            print 'LTC priv version', i, addr
        elif addr.startswith('74P'):
            print 'NMC priv version', i, addr
        elif addr.startswith('Mw6'):
            print 'IXC priv version', i, addr
        elif addr.startswith('5ar'):
            print 'NVC priv version', i, addr
        elif addr.startswith('5nX'):
            print 'FTC priv version', i, addr


class ValidAddressTest(unittest.TestCase):
    def setUp(self):
        self.pubs = ['1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',  # btc
                     '1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i',  # btc
                     'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq',  # ltc
                     'NEWoeZ6gh4CGvRgFAoAGh4hBqpxizGT6gZ',  # nmc
                     'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',  # ppc
                     'xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ',  # ixc
                     '4XeGKmz1T7oiwMYS6LWFMYia9ddDoT6ajT',  # nvc
                     '6wftERmjiCayqxNxErWAGJMHvfAt4RZZbn',  # ftc
                     ]

        self.priv = ['5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',  # btc
                     '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',  # ltc
                     '74Pe3r1wxUzY8nHd2taLb5SqpAsxZK6q6VwUcQp7fPS11tYZd9P',  # nmc
                     '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',  # ppc
                     'Mw64RiX6A23DKVivM4USZXC8nBt3bqyKquB8wsifzJ589JYYDF',   # ixc
                     '5artHeGYTmEaCgib9PGNcy4mX9nMxL2JUNpjspYfvZ8wJWQjuBJ',  # nvc
                     '5nXMM2xjaKHw1cCparzNLtfR1qUfrZ5ZCDFPLig3tVBGGBK2QwG',  # ftc
                    ]

    def test_pub_validate(self):
        for a in self.pubs:
            self.assertTrue(address.validate(a))

    def test_priv_validate(self):
        for a in self.priv:
            self.assertTrue(address.validate(a))


class ConvertAddressTest(unittest.TestCase):
    def setUp(self):
        self.pubs = {'btc': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',  # btc
                     'ltc': 'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq',  # ltc
                     'nmc': 'NEWoeZ6gh4CGvRgFAoAGh4hBqpxizGT6gZ',  # nmc
                     'ppc': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',  # ppc
                     'ixc': 'xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ',  # ixc
                     'nvc': '4XeGKmz1T7oiwMYS6LWFMYia9ddDoT6ajT',  # nvc
                     'ftc': '6wftERmjiCayqxNxErWAGJMHvfAt4RZZbn',  # ftc
                     }
        self.priv = {'btc': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',  # btc
                     'ltc': '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',  # ltc
                     'nmc': '74Pe3r1wxUzY8nHd2taLb5SqpAsxZK6q6VwUcQp7fPS11tYZd9P',  # nmc
                     'ppc': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',  # ppc
                     'ixc': 'Mw64RiX6A23DKVivM4USZXC8nBt3bqyKquB8wsifzJ589JYYDF',   # ixc
                     'nvc': '5artHeGYTmEaCgib9PGNcy4mX9nMxL2JUNpjspYfvZ8wJWQjuBJ',  # nvc
                     'ftc': '5nXMM2xjaKHw1cCparzNLtfR1qUfrZ5ZCDFPLig3tVBGGBK2QwG',  # ftc
 }

    def test_btc_to_ltc(self):
        ltc = address.convert(self.pubs['btc'], 'ltc')
        self.assertEqual(self.pubs['ltc'], ltc)

    def test_all_pub_convert(self):
        for k1 in self.pubs:
            for k2 in self.pubs:
                addr = address.convert(self.pubs[k1], k2)
                self.assertEqual(self.pubs[k2], addr,
                                 msg="%s != %s in conversion from %s to %s" % (self.pubs[k2], addr, k1, k2))

    def test_all_priv_convert(self):
        for k1 in self.priv:
            for k2 in self.priv:
                addr = address.convert(self.priv[k1], k2)
                self.assertEqual(self.priv[k2], addr,
                                 msg="%s != %s in conversion from %s to %s" % (self.pubs[k2], addr, k1, k2))

    def test_unknown_currency(self):
        self.assertRaises(Exception, address.convert, '', 'xxx')


class DetectAddressTest(unittest.TestCase):
    def setUp(self):
        self.addrs = {'btc': {'pub': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',
                             'priv': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'},
                     'ltc': {'pub': 'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq',
                             'priv': '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi'},  # ltc
                     'nmc': {'pub': 'NEWoeZ6gh4CGvRgFAoAGh4hBqpxizGT6gZ',
                             'priv': '74Pe3r1wxUzY8nHd2taLb5SqpAsxZK6q6VwUcQp7fPS11tYZd9P'},  # nmc
                     'ppc': {'pub': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',
                             'priv': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho'},  # ppc
                     'ixc': {'pub': 'xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ',
                             'priv': 'Mw64RiX6A23DKVivM4USZXC8nBt3bqyKquB8wsifzJ589JYYDF'},  # ixc
                     'nvc': {'pub': '4XeGKmz1T7oiwMYS6LWFMYia9ddDoT6ajT',
                             'priv': '5artHeGYTmEaCgib9PGNcy4mX9nMxL2JUNpjspYfvZ8wJWQjuBJ'},  # nvc
                     'ftc': {'pub': '6wftERmjiCayqxNxErWAGJMHvfAt4RZZbn',
                             'priv': '5nXMM2xjaKHw1cCparzNLtfR1qUfrZ5ZCDFPLig3tVBGGBK2QwG'},  # ftc
                     }

    #def test_detect(self):
        #pass
        #for curr, addrs in self.addrs.items():
            #pub_det = address.detect(addrs['pub'])
            #self.assertEqual(curr, pub_det['currency'])
            #self.assertEqual('pub', pub_det['type'])
            #pub_det = address.detect(addrs['priv'])
            #self.assertEqual(curr, pub_det['currency'])
            #self.assertEqual('priv', pub_det['type'])


class Hash160Test(unittest.TestCase):
    def setUp(self):
        self.h160 = "c4c5d791fcb4654a1ef5e03fe0ad3d9c598f9827"
        self.addr = "1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T"

    def test_hex_from_hash160(self):
        addr = address.from_hash160(self.h160)
        self.assertEqual(self.addr, addr)

    def test_digest_from_hash160(self):
        addr = address.from_hash160(self.h160.decode('hex'))
        self.assertEqual(self.addr, addr)

    def test_to_hash160(self):
        h160 = address.to_hash160(self.addr)
        self.assertEqual(self.h160, h160)


class Base58Test(unittest.TestCase):
    def setUp(self):
        self.h160 = "c4c5d791fcb4654a1ef5e03fe0ad3d9c598f9827"
        self.b58 = "5vtvghp3bnuQkx9dRHH6Qv6xDNbhvJw7vyuLj1PeFT9wEGA6Mn1NYJS"

    def test_b58encode(self):
        assert base58.b58encode(self.h160) == self.b58

    def test_b58decode(self):
        assert base58.b58decode(self.b58) == self.h160

    def test_invalid_b58decode(self):
        self.assertRaises(Exception, base58.b58decode, 'I')
        self.assertRaises(Exception, base58.b58decode, 'O')
        self.assertRaises(Exception, base58.b58decode, '0')
        self.assertRaises(Exception, base58.b58decode, 'l')

class GenerateAddressTest(unittest.TestCase):
    def setUp(self):
        self.secret = 'hello'
        self.secret_pub_hex = 'b84a3b37524e049979df3b4e715cac485385d400'
        self.secret_compr_hex = 'e3dd7e774a1272aeddb18efdc4baf6e14990edaa'
        self.secret_priv_hex = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        self.secret_compr_priv_hex = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b982401'

        self.secret2 = 'hellow'
        self.secret2_compr_hex = 'b980c68e635aa6f2a10f7cd2e4f36a48c8bb7eb2'
        self.secret2_compr_priv_hex = 'd0bc381952d0827f36467818a9560eb5eb6fda8a64a422aa21fcda3f2263e8b401'

    def test_with_secret(self):
        priv, pub = address.generate(secret=self.secret)
        self.assertEqual(pub.hex, self.secret_pub_hex)
        self.assertEqual(priv.hex, self.secret_priv_hex)

    def test_compressed_with_secret(self):
        priv, pub = address.generate(secret=self.secret, compressed=True)
        self.assertEqual(pub.hex, self.secret_compr_hex)
        self.assertEqual(priv.hex, self.secret_compr_priv_hex)

    def test_compressed_with_secret2(self):
        priv, pub = address.generate(secret=self.secret2, compressed=True)
        self.assertEqual(pub.hex, self.secret2_compr_hex)
        self.assertEqual(priv.hex, self.secret2_compr_priv_hex)

if __name__ == '__main__':
    #find_version()
    unittest.main()
