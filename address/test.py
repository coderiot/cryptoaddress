#!/usr/bin/env python
# encoding: utf-8

import unittest

import address
import base58

# secret: correct horse battery staple
pubs = {'btc': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',
        'ltc': 'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq',
        'nmc': 'NEWoeZ6gh4CGvRgFAoAGh4hBqpxizGT6gZ',
        'ppc': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',
        'ixc': 'xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ',
        'ftc': '6wftERmjiCayqxNxErWAGJMHvfAt4RZZbn',
        'ppc': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',
        'dgc': 'DP5XzAYM55zzvtcLdZqG2JhszjHyNnvW8i',
        'zet': 'ZVyhDbSka7AopZafrYVCGaKDTxB8zhm9k2',
        'mec': 'MRqbgLW7GhGXHZQ57xVdip9capSqZatiut',
        'anc': 'AZiK6QTL6pksCrdjTdW2dRoNbCVNQ7zRs6',
        'qrk': 'QeYRZCtQx8yXq2WmKKABbpKucrWPFn2Z8g',
        'bte': '8Z2JArxtYvSV7gwJLXqSCoSSSgCep4FTWh',
        'sbc': 'scBqXUriXE2Ed4rZxRUY6DZcnemax23Uev',
        'gdc': 'gLiwxSWeeB3hivx9Gg9cWhwbAXZB14WW5c',
        'nvc': '4XeGKmz1T7oiwMYS6LWFMYia9ddDoT6ajT',
        'nmc': 'NEWoeZ6gh4CGvRgFAoAGh4hBqpxizGT6gZ',
        'btc': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',
        'btb': 'BNPX4d3uXBgcqiuuWUAfbgLwrD1FpP313N',
        'mnc': 'MRqbgLW7GhGXHZQ57xVdip9capSqZatiut',
        'pts': 'PqsDazHqXn3nCAEbGUVYdZnLMqzVqdmE9z',
        'krc': 'Z6e6EV9Trvhw18Saq89snT3RqSvCHADBXb',
        'frc': 'FPmYui2nczKP24JmkfVrSw4p9FagvnFKex',
        'wdc': 'WgcUKqMjbqvg6Xc4gc9xshQi4RNY1S38TD',
        'tix': '8xMu9yGBG6uMw85PMxAkgviE5BTbYADVRW',
        'bqc': 'bWfi98wC81VBujH6ye9nhCg9cUTrTTdMTB',
        'xpm': 'AZiK6QTL6pksCrdjTdW2dRoNbCVNQ7zRs6',
        'dtc': 'DP5XzAYM55zzvtcLdZqG2JhszjHyNnvW8i',
        'ixc': 'xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ',
        'xjo': 'JcUNnaR6JS2PZXRTx2AQKwF7BHeEfaiSt4',
        'zcc': 'ZVyhDbSka7AopZafrYVCGaKDTxB8zhm9k2',
        'cent': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',
        'col': '27ceR8CHC32U2khuwpWLSo5rNc5ZWKC247',
        'ltc': 'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq',
        'ftc': '6wftERmjiCayqxNxErWAGJMHvfAt4RZZbn',
        'tag': 'TTueSxyRvQDfZ4VNVFVQzhER2PJzGds5gu',
        'cnc': 'CaQL1wwmej5FJ2LAajAd44AJjin5zEqXBK',
        'i0c': 'jZRmqJtxKckiGQ4qU2pAPi7tCZcimLyda2',
        'ifc': 'iMQxsz16C5N5p6eaPmpCwLJXK3qtXZuvoh',
        'lky': 'LDpnj1cF99stqFyp3hVgGSLFhJg1UbRceb',
        'trc': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',
        'yac': 'YHxtGGYtSZnBNGAQnHVEpCVraSQJpbjuUb',
        'fst': 'fwPLyLDMvzapuVp4FFpJ2afoY2JEHc2KJn',
        'clr': 'CaQL1wwmej5FJ2LAajAd44AJjin5zEqXBK',
        'cgb': '5jf5H6ssafCMPexhAbWCovXw39Q3ryw5ic',
        'nec': 'NdrQdfPyQEf9jrpLCDVbBBxyULDfhhus4A',
        'emd': 'EzRwvbjVuorWCdAgjFAXxoo2WkKkEtGjmZ',
        'adt': '27ceR8CHC32U2khuwpWLSo5rNc5ZWKC247',
        'net': 'nNnzj4yyHszqzS3Sdy9Pnb2Pc6RKe28vk2',
        'dvc': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',
        'bet': 'BNPX4d3uXBgcqiuuWUAfbgLwrD1FpP313N',
        'osc': '27ceR8CHC32U2khuwpWLSo5rNc5ZWKC247',
        'tek': 'Bmj83jMCEN9VfA3zXtVz5ocjUiGCYu2FKE',
        'dem': 'NdrQdfPyQEf9jrpLCDVbBBxyULDfhhus4A',
        'uno': 'ucsrT2MA58LciEZ15X98WqvYwB4JVaGzxN',
        'tgc': 'tQs3VhTHwawzFw8k1G9B4U7C3fHUJeaWXn',
        'ixc': 'xqagKtjTka3dFhfhGsogPr6qyD7rAzGQKQ',
        'asc': 'AANi7JA3PeHzPRVeSDAi9JXaxhERjVThbm',
        'cin': 'CaQL1wwmej5FJ2LAajAd44AJjin5zEqXBK',
        'nrb': 'EBkjxP8vVSvkZktWgQVtzZFTFjorpcr1Bs',
        'spt': 'MRqbgLW7GhGXHZQ57xVdip9capSqZatiut',
        'nan': 'MqBCfSoPysjQ6zYA9NpxCwRQDKhnH98QEv',
        'rec': 'RTDdXRUzNVuHTtnwN9ppa4sUss2GmwKAbn',
        'orb': 'oaoogPsqRRPUSjThiE9MExqkVcC9njjahZ',
        'xen': 'XtdHHAFbjPKJYq2Kks9vL5E4ww9N5BWZts',
        'cap': 'EzRwvbjVuorWCdAgjFAXxoo2WkKkEtGjmZ',
        'hbn': 'EzRwvbjVuorWCdAgjFAXxoo2WkKkEtGjmZ',
        'src': 'scBqXUriXE2Ed4rZxRUY6DZcnemax23Uev',
        'glx': 'gk4YwYowMMWaYN6EJ6UvzqDNo2p7nZWuFj',
        'dmd': 'dXMj4gRdfuoZztyY6jpP7q35kzka5XqTcj',
        'boc': 'BNPX4d3uXBgcqiuuWUAfbgLwrD1FpP313N',
        'exc': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',
        'grw': 'GbnMs2vekXi1UMj2pvVouJtB2mMX7gjtWG',
        'glc': '7M1VDY52RP3rfPX3GGqUkRd5ZARpgush3h',
        'phs': '9m378BrkgTq7ZzMZQnqPfBFoLByUzuGo3E',
        'alf': 'aJeuBp3KzU6ZTRrquP9qEprnixh2QRZUuM',
        'csc': 'CaQL1wwmej5FJ2LAajAd44AJjin5zEqXBK',
        'cmc': 'CB4j2qeUwYcNUbC5ZJqJZvtX7DX9Dqkakq',
        'pxc': 'PqsDazHqXn3nCAEbGUVYdZnLMqzVqdmE9z',
        'flo': 'FPmYui2nczKP24JmkfVrSw4p9FagvnFKex',
        'arg': 'AZiK6QTL6pksCrdjTdW2dRoNbCVNQ7zRs6',
        'crc': 'QFCpa6b8ExWf1bNgHtps7h47zMFSZMNa9Q',
        'buk': '3KdTNT69KaR6V48B25WHuAuDG7rPaNHvoY',
        'red': 'RrZEWXnH5gNAHKw2PaA94C9GWNHDPWBv5c',
        'elp': 'eL2w2u2D6GjKdmFi9aV265af21GTWYnrVN',
        'btg': 'gk4YwYowMMWaYN6EJ6UvzqDNo2p7nZWuFj',
        'dbl': 'Ay3v5Wkcp1Dk2HmpV3qM7Z5ADhkKApqpWK',
        'elc': 'Eb6LwVSDCdPdPC2bhpqDUgXEtF4oWjVxqs',
        'nbl': 'NdrQdfPyQEf9jrpLCDVbBBxyULDfhhus4A',
        'ezc': 'Eb6LwVSDCdPdPC2bhpqDUgXEtF4oWjVxqs',
        'lk7': '7M1VDY52RP3rfPX3GGqUkRd5ZARpgush3h',
        'ryc': 'RTDdXRUzNVuHTtnwN9ppa4sUss2GmwKAbn',
        'sxc': 'SFtqVe5Znrq36m57QzVTYKR48sYABVkGyx',
        'pyc': 'PSXcbszYpbauNj6WF4AE9SWYjLjZArBajH',
        'doge': 'DP5XzAYM55zzvtcLdZqG2JhszjHyNnvW8i',
        'amc': 'Ay3v5Wkcp1Dk2HmpV3qM7Z5ADhkKApqpWK',
        'gld': 'EBkjxP8vVSvkZktWgQVtzZFTFjorpcr1Bs',
        'gme': 'GbnMs2vekXi1UMj2pvVouJtB2mMX7gjtWG',
        'mem': 'JD8moU7obFZWk6HNvbq5qoyKYnPHuSCdHx',
        'jkc': '7kM6CeNK8ZWjUpf8HhAoEYtsBfgmSJxBai',
        'tea': 'TsFFS5GidagYNVdTWfpjUpWCetZvxoP7wH',
        'vtc': 'VswGMcmABUzvTfKtdmVKuSs8oQreYcmZeM',
        'mmc': 'MRqbgLW7GhGXHZQ57xVdip9capSqZatiut',
}
priv = {'btc': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'ltc': '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',
        'nmc': '74Pe3r1wxUzY8nHd2taLb5SqpAsxZK6q6VwUcQp7fPS11tYZd9P',
        'ppc': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',
        'ixc': 'Mw64RiX6A23DKVivM4USZXC8nBt3bqyKquB8wsifzJ589JYYDF',
        'ftc': '5nXMM2xjaKHw1cCparzNLtfR1qUfrZ5ZCDFPLig3tVBGGBK2QwG',
        'ppc': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',
        'dgc': '6KdGAk9FD87ZAjW768vMc2FoffLAFpZZnSP7F7gPnyHUA9ttj7B',
        'zet': '8XvPp3mMTCkW4srevPtJZBpv7ByZAJBMid4DM15ZQDj4jGYEcFe',
        'mec': '6zW9hP7tFde5s98DDjLLgSFHyweXFuR5XDoG87SKg5RE2dHMpaF',
        'anc': '6623w812F9NyDzSAk5aMvn4PFs28htfSGxtMY4s7qPEkhoV8sQS',
        'qrk': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'bte': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'sbc': '9WHyvmnHAYN4yfi7DCtHDVDNfVqP1ickYA7LRM2ZEDvK3GbzvKw',
        'gdc': '8Zs8zHDPJdRjChSMpyWJWWRh2JbGp12EWG8Kb9mTPsjTDpxhB2G',
        'nvc': '5artHeGYTmEaCgib9PGNcy4mX9nMxL2JUNpjspYfvZ8wJWQjuBJ',
        'nmc': '74Pe3r1wxUzY8nHd2taLb5SqpAsxZK6q6VwUcQp7fPS11tYZd9P',
        'btc': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'btb': '69uYHau5wzjRVdbaZEpMqRFw66Fa1JMBrF2a2NEuphFXh3FQHaB',
        'mnc': '6zW9hP7tFde5s98DDjLLgSFHyweXFuR5XDoG87SKg5RE2dHMpaF',
        'pts': '7CAckmp5NBhSg4cSfD4LQMqwUdLqA8ULF4Dub1Zhe1TYzJcerWL',
        'krc': '7xsjp78oxyFemvyfWYLKLjdkYFWM7KrULkrPCTPKW5cULhBgcNj',
        'frc': '6VLz3uPQUFVgqqQdd32MNdFgFEQkWLmwidjeTs7smFKQdH5Z5cs',
        'wdc': '7mDGkiScrRCHy1VS54cKcp373Zp3D6oDcvRjjZFwY9a9NushHNZ',
        'tix': '5xF5ECCtqSg4gi7M7m6N7VfHbQZG75Hw8QbvZU7XrmDCjJys4Ai',
        'bqc': '8AYCsVq15XK1arTtx24K4fEQ2wCf1Yuj4bH2fMWhU1eoJPHfrU4',
        'xpm': '6623w812F9NyDzSAk5aMvn4PFs28htfSGxtMY4s7qPEkhoV8sQS',
        'dtc': '6KdGAk9FD87ZAjW768vMc2FoffLAFpZZnSP7F7gPnyHUA9ttj7B',
        'ixc': 'Mw64RiX6A23DKVivM4USZXC8nBt3bqyKquB8wsifzJ589JYYDF',
        'xjo': '5pU6XGQmRjyA9RnXVScNJDGBvx6PWFvRyrKVasMwt9BekqewcWF',
        'zcc': '7zpUzLaqpPvsukZNR7xKJ4EXTN84m2hM8PvVSc5DVjcrqH8MTpp',
        'cent': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',
        'col': '5PCREFaMMDBDPmEMhuYNu3U82U6446y3kYQ6QvRHxd6cLkgsEfx',
        'ltc': '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',
        'ftc': '5nXMM2xjaKHw1cCparzNLtfR1qUfrZ5ZCDFPLig3tVBGGBK2QwG',
        'tag': '7VfKLrrN31nUtSqnpReKzFEuietJ1U4DKorsnMkmauX3Rt6pjir',
        'cnc': '6FjmpHFBWGm6u6LhGygMhP4FqS6ixQspDAEtkpJbofGhAvuvi2M',
        'i0c': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'ifc': '8jarsSTYZkorsoLtMscJH7RZbsfs4XEcSTUrouCwN9mPgw1j4iq',
        'lky': '6tfvAgmnhMcQTgP6VzULpUSyEboNJntTAJawPfNdh7Q4YmEk7Wu',
        'trc': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'yac': '7tzFTeEkG7uCWHpFhP6KS6SCi2GuovAimUiAiA1XWmbhMP6scZ1',
        'fst': '8XvPp3mMTCkW4srevPtJZBpv7ByZAJBMid4DM15ZQDj4jGYEcFe',
        'clr': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'cgb': '5gh7pLce23GFc9Ths88NUvs6GVdWuSYvqJ34cGcMuXA6nPooqdc',
        'nec': '76LPE5TyoufmGbsKwUCLYQ3cjHVgD1wht91arZW1f3SPWT7Gohc',
        'emd': '6TQEsfwNcppTi1pviTQMRJeuL7o2rdw4vzfYDiRymbK28i6LvCx',
        'adt': '5PCREFaMMDBDPmEMhuYNu3U82U6446y3kYQ6QvRHxd6cLkgsEfx',
        'net': '952Jdkws61a8E19wRfpHpKRJm1q3ZZfNJrBwFQ5uJhqGdApMkHV',
        'dvc': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'bet': '5pU6XGQmRjyA9RnXVScNJDGBvx6PWFvRyrKVasMwt9BekqewcWF',
        'osc': '5PCREFaMMDBDPmEMhuYNu3U82U6446y3kYQ6QvRHxd6cLkgsEfx',
        'tek': '6XHjE8qSKgAuyezLXceMKwrTAM2UA3cpWGoki1omkuKo7uqracS',
        'dem': '76LPE5TyoufmGbsKwUCLYQ3cjHVgD1wht91arZW1f3SPWT7Gohc',
        'uno': '8XvPp3mMTCkW4srevPtJZBpv7ByZAJBMid4DM15ZQDj4jGYEcFe',
        'tgc': '8XvPp3mMTCkW4srevPtJZBpv7ByZAJBMid4DM15ZQDj4jGYEcFe',
        'ixc': 'Mw64RiX6A23DKVivM4USZXC8nBt3bqyKquB8wsifzJ589JYYDF',
        'asc': '645JktYzPihk6ArTqVxMyTTcLkQR4BpZVKpFHvBDqjENDCeG65n',
        'cin': '6FjmpHFBWGm6u6LhGygMhP4FqS6ixQspDAEtkpJbofGhAvuvi2M',
        'nrb': '6PWkXD3JuyU1SNfWuJAMWfTMVtZbZEFKMiXKjR4BnHJF9RmpyJh',
        'spt': '6zW9hP7tFde5s98DDjLLgSFHyweXFuR5XDoG87SKg5RE2dHMpaF',
        'nan': '72StscZv74KJzxhv8JxLdkr4u4GEucFxJrsNNG8DfjRcXG5MSNk',
        'rec': '7KwbThcCmtQMDLwGHXYLDeF395ohkwqqPcWLZcKHcdV6xr1oFyd',
        'orb': '9ArYATHxeHbodTu49QgHgHDdWMgCWgBzfmQFyr9bHfrS746XGsH',
        'xen': '7s3WHQniQhDyNUEYnoUKUmqRnufCADKqyqe4U1KdX7bJrkqeGJH',
        'cap': '6TQEsfwNcppTi1pviTQMRJeuL7o2rdw4vzfYDiRymbK28i6LvCx',
        'hbn': '6TQEsfwNcppTi1pviTQMRJeuL7o2rdw4vzfYDiRymbK28i6LvCx',
        'src': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        'glx': '8botAWfRA46xLX24jZ8JTq2TwRCzThs7HuCRqJTMPXjqiVJJry8',
        'dmd': '8LFvkf5ALeh9FxNRUvAJqGEGcWHFG586zndZt6xBSHgjmXQUVta',
        'boc': '69uYHau5wzjRVdbaZEpMqRFw66Fa1JMBrF2a2NEuphFXh3FQHaB',
        'exc': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',
        'grw': '6bBDabjW2XXNFJ9kLmtMEb3zzaFuTTJa5YwyCKBZkDLa7863JsK',
        'glc': '5pU6XGQmRjyA9RnXVScNJDGBvx6PWFvRyrKVasMwt9BekqewcWF',
        'phs': '628Zaf6xYJ2WxMGkvvLN28rqRdnhQUyghgk93mVKr5DyiamzEg3',
        'alf': '84hyLoUuXFHLBPinEHCKChS5HbMW4SP6hg4hvuT1V3ddpX6cK5L',
        'csc': '6FjmpHFBWGm6u6LhGygMhP4FqS6ixQspDAEtkpJbofGhAvuvi2M',
        'cmc': '6Do2e3o9er5smGkzNQ4Mk4TUvKV1Ji2wRXAnWfchp1GJgK7gzei',
        'pxc': '7CAckmp5NBhSg4cSfD4LQMqwUdLqA8ULF4Dub1Zhe1TYzJcerWL',
        'flo': '6VLz3uPQUFVgqqQdd32MNdFgFEQkWLmwidjeTs7smFKQdH5Z5cs',
        'arg': '6623w812F9NyDzSAk5aMvn4PFs28htfSGxtMY4s7qPEkhoV8sQS',
        'crc': '7E7Mw1G7DcNfotC9ZngLMgSiPjxYoqKD2hJ1qAFbdfTwV1q6C1y',
        'buk': '5V2ekwvSuVCtoDyUReQNm1GSmowD1DVg7TcR9NUywb7mpd6sKVg',
        'red': '7MtLdw4EdK5aMAWyC7ALAxqp4CRRQegiBFaSom1BcHVVTTt836o',
        'elp': '8Q9R77yE3W3bXbXqJ5QJjuRpSjWgZUora4mnNQKyRbhWkmeaSdW',
        'btg': '8botAWfRA46xLX24jZ8JTq2TwRCzThs7HuCRqJTMPXjqiVJJry8',
        'dbl': '67xo7MT46a4CMp1sefCMt6fAAydrMbWK4bxTnDZ1q3F9CTSb7ZM',
        'elc': '6RTVhSVLmQ9EaCFDosnMTz48R1BKCw6C9MbRyZk5mwJddzkqnE4',
        'nbl': '76LPE5TyoufmGbsKwUCLYQ3cjHVgD1wht91arZW1f3SPWT7Gohc',
        'ezc': '6RTVhSVLmQ9EaCFDosnMTz48R1BKCw6C9MbRyZk5mwJddzkqnE4',
        'lk7': '5pU6XGQmRjyA9RnXVScNJDGBvx6PWFvRyrKVasMwt9BekqewcWF',
        'ryc': '7KwbThcCmtQMDLwGHXYLDeF395ohkwqqPcWLZcKHcdV6xr1oFyd',
        'sxc': '7Pq5pAWGUjkoUz6g6gnL8HSayK394MXaxteZ3uh5bwVsx7BBAmL',
        'pyc': '7ADsaYN3Wm2DYF2jkdSLT3FAZWj7WRdTTR9oLrsoeMTAVgq1Mho',
        'doge': '6KdGAk9FD87ZAjW768vMc2FoffLAFpZZnSP7F7gPnyHUA9ttj7B',
        'amc': '67xo7MT46a4CMp1sefCMt6fAAydrMbWK4bxTnDZ1q3F9CTSb7ZM',
        'gld': '6PWkXD3JuyU1SNfWuJAMWfTMVtZbZEFKMiXKjR4BnHJF9RmpyJh',
        'gme': '6bBDabjW2XXNFJ9kLmtMEb3zzaFuTTJa5YwyCKBZkDLa7863JsK',
        'mem': '6ixCHXXdSEEGnaUZy6NM3sT6f2in4Gg5E7EQAuw9iqN85eUNVK8',
        'jkc': '5vJL3xkrz1zqYtXeDBUNAB4WgHwYTNT4LmXpKKRds7CpEhQ9rE7',
        'tea': '8XvPp3mMTCkW4srevPtJZBpv7ByZAJBMid4DM15ZQDj4jGYEcFe',
        'vtc': '7hKnQFYZ9ZqqhNL2FuNKiAqZDLabuh7U3eHXFFt9YqZNPcf8YWd',
        'mmc': '6zW9hP7tFde5s98DDjLLgSFHyweXFuR5XDoG87SKg5RE2dHMpaF',
}


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
        self.pubs = [a for _, a in pubs.items()]
        self.priv = [a for k, v in priv.items()]

    def test_pub_validate(self):
        for a in self.pubs:
            self.assertTrue(address.validate(a))

    def test_priv_validate(self):
        for a in self.priv:
            self.assertTrue(address.validate(a))


class ConvertAddressTest(unittest.TestCase):
    def setUp(self):
        self.pubs = pubs
        self.priv = priv

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
                addr = address.convert(self.priv[k1], k2, typ='priv')
                self.assertEqual(self.priv[k2], addr,
                                 msg="%s != %s in conversion from %s to %s" % (self.pubs[k2], addr, k1, k2))

    def test_unknown_currency(self):
        self.assertRaises(Exception, address.convert, '', 'xxx')


class DetectAddressTest(unittest.TestCase):
    def setUp(self):
        self.addrs = {}
        for k, a in pubs.items():
            self.addrs[k] = {'pub': a}

        for k, a in priv.items():
            self.addrs[k]['priv'] = a

    def test_detect(self):
        for curr, addrs in self.addrs.items():
            pub_det = address.detect(addrs['pub'])
            self.assertIn(curr, [d['currency'] for d in pub_det])
            self.assertIn('pub', [d['type'] for d in pub_det if d['currency'] == curr])

            priv_det = address.detect(addrs['priv'])
            self.assertIn(curr, [d['currency'] for d in priv_det])
            self.assertIn('priv', [d['type'] for d in priv_det if d['currency'] == curr])


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
