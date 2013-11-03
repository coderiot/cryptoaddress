*cryptoaddress* - validate, convert and detect addresses from different crypto currencies.

## Currencies
 * BTC
 * LTC
 * NMC
 * PPC
 * IXC
 * NVC
 * FTC

## Requirements

 - [ecdsa](https://github.com/warner/python-ecdsa)

## Installation
```sh
pip install -e git+https://github.com/coderiot/cryptoaddress.git#egg=cryptoaddress
```

## run tests
```sh
python -m address.test -v
```

## Usage
### generate new address for currency
```python
>>> priv, pub = address.generate(currency='btc')
>>> priv.b58
'5JoDLL3VW3YyxKywCiZRa9RA5ByPvNrnpc6rYG5FudXeoZGCHvK'
>>> pub.b58
'125WvPrXRBnBZBinhhyB3K3FALxgzGNDTQ'
```

### generate new compressed address
```python
>>> priv, pub = address.generate(currency='btc', compressed=True)
>>> priv.b58
'L53Mzz8SspiSqwvsPdyPf2Zo2c5qHVzco4geb6qXXfnvMyFLXgfy'
>>> pub.b58
'1Eu6g6PyojgqgWuyngpPyX1MkA4WMyzLJ1'
```

### generate new address by secret
```python
>>> priv, pub = address.generate(currency='btc', secret='hello')
>>> priv.b58
'5JA5gN4G78DhFSW4jr28vjb8JEX5UhVMZB16Jr6MjDGaeguJEvm'
>>> pub.b58
'1HoSFymoqteYrmmr7s3jDDqmggoxacbk37'
```

### generate address from RIPEMD-160 Hash (Default: BTC)
```python
>>> import address
>>> address.from_hash160("c4c5d791fcb4654a1ef5e03fe0ad3d9c598f9827")
'1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T'
```
### generate LTC address from RIPEMD-160 Hash
```python
>>> import address
>>> address.from_hash160("c4c5d791fcb4654a1ef5e03fe0ad3d9c598f9827", currency='ltc')
'1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T'
```

### generate all address types for one RIPEMD-160 Hash
```python
>>> import address
>>> for curr in address.versions:
...     print curr.upper(), address.from_hash160(h, currency=curr)
PPC PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH
IXC xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ
LTC LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq
FTC 6wftERmjiCayqxNxErWAGJMHvfAt4RZZbn
NVC 4XeGKmz1T7oiwMYS6LWFMYia9ddDoT6ajT
NMC NEWoeZ6gh4CGvRgFAoAGh4hBqpxizGT6gZ
BTC 1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T
```

### validate public address
```python
>>> import address
>>> address.validate("1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T")
True
```

### validate private address
```python
>>> import address
>>> address.validate("5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS")
True
```

```python
>>> import address
>>> address.validate("14oLvT2")
False
```

### convert BTC public address to LTC public address
```python
>>> import address
>>> address.convert('1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T', to='ltc')
'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq'
```
### convert BTC private address to LTC private address
```python
>>> import address
>>> address.convert('5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS', to='ltc')
'6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi'
```

### detect address type
```python
>>> import address
>>> address.detect('5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS')
{'currency': 'btc', 'type': 'priv'}
```

```python
>>> import address
>>> address.detect('1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T')
{'currency': 'btc', 'type': 'pub'}
```
