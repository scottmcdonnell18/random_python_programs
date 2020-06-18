#!/usr/bin/env python3

import random

chars = "123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()?"

passlen = 8
p = "".join(random.sample(chars, passlen))

print(p)