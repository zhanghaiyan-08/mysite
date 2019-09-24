__author__ = 'Supi'
# @Time    : 2018/8/17 11:06
import random
import string
import hashlib

def randomstrings(stringbit):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=- 我们"
    sa = []
    for i in range(stringbit):
      sa.append(random.choice(seed))
    randomstringsvalue = ''.join(sa)
    return randomstringsvalue

def  randomdigit(digitbit):
    digitseed = "1234567890"
    sa = []
    for i in range(digitbit):
        sa.append(random.choice(digitseed))
    randomdigitvalue = ''.join(sa)
    return randomdigitvalue

