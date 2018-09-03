#!/usr/bin/env python
import time
import datetime
import base64
import hashlib
import onetimepass as otp
from dateutil import tz

""" def get_totp(
        secret,
        as_string=False,
        digest_method=hashlib.sha1,
        token_length=6,
        interval_length=30,
        clock=None,
) """
#my_secret = 'MFRGGZDFMZTWQ2LK'
#my_secret1 = str.encode("ninja@example.comHDECHALLENGE003ninja@example.comHDECHALLENGE003ninja@example.comHDECHALLENGE003ninja@example.comHDECHALLENGE003ninja@example.comHDECHALLENGE003ninja@example.comHDECHALLENGE003")
my_secret1 = str.encode("ninja@example.comHDECHALLENGE003")

print (my_secret1)
my_secret = base64.b32encode(my_secret1)
#my_secret = my_secret[0:128]
#my_secret = "6E696E6A61406578616D706C652E636F6D4844454348414C4C454E47453030336E696E6A61406578616D706C652E636F6D4844454348414C4C454E4745303033"
#my_secret = base64.b64encode(my_secret1)
#my_clock = time.time()
#my_clock = time.strptime("Mar 17 2014 15:20:51", "%b %d %Y %H:%M:%S").time()
#my_clock = 1395069651
#my_clock=1395069651
#datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
my_clock = int(datetime.datetime(2014,3,17,15,20,51,0,tz.gettz('UTC')).timestamp())
print (my_secret)
print (my_clock)
#my_token = otp.get_totp(secret=my_secret,token_length=10,clock=my_clock)
my_token = otp.get_totp(secret=my_secret,digest_method=hashlib.sha512,token_length=10,interval_length=30,clock=my_clock)

print (my_token)
