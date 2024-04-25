Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #write a script that uses "epoch" time in seconds and translates it into time in days, hours, minues, seconds
>>> import time
>>> time.time()
1714056360.1591203
>>> def chour(t):
...     hour = t/3600
...     print("The number of hours that have passed since epoch began is %f" %hour)
... 
...     
>>> def cminute(t):
...     minute = t/(60)
...     print("The number of minutes that have passed since epoch began is %f" %minute)
... 
...     
>>> def cseconds(t):
...     seconds = t
...     print("The number of seconds that have passed since epoch began is %f" %seconds)
... 
...     
>>> def tot_day():
...     sec=time.time()
...     tot_day = sec / (60*60*24)
...     print("The number of days that have passed since epoch began is %f" %tot_day)
... 
...     
>>> tot_day()
The number of days that have passed since epoch began is 19838.617983
>>> chour(time.time())
The number of hours that have passed since epoch began is 476126.833611
>>> cminute(time.time())
The number of minutes that have passed since epoch began is 28567610.234296
>>> cseconds(time.time())
The number of seconds that have passed since epoch began is 1714056627.112891
