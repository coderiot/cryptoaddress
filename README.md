*cryptoaddress* - validate, convert and detect addresses from different crypto currencies.

## Currencies
 * BTC
 * LTC
 * NMC
 * PPC
 * IXC
 * NVC
 * FTC


## Installation
```sh
$ pip install -e git+https://github.com/coderiot/cryptoaddress.git#egg=cryptoaddress
```

## run tests
```sh
python -m address.test -v
```

## Usage
### validate
```python
>>> import address
>>> address.validate("1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T")
True
```

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

### convert
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
