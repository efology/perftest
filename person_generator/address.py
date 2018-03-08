#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import string

class Address:
    def __init__(self):
        pass
    

    def get_address(self, country):
        addr = self.get_random_string()
        if country=='se':
            addr += 'gatan '
        elif country=='no':
            addr += 'gata '
        elif country=='dk':
            addr += ' Gade '
        elif country=='fi':
            addr += 'katu '
        elif country=='de':
            addr += 'strasse '
        elif country=='nl':
            addr += 'straat '
        elif country=='at':
            addr += 'gasse '
        digits = string.digits
        addr += ''.join(random.choice(digits) for x in range(2))
        return string.capitalize(addr)


        
    def get_random_string(self):
        chars = string.ascii_lowercase
        return ''.join(random.choice(chars) for x in range(8))
       

        
if __name__ == "__main__":
    aa = Address()
    print aa.get_address('se')
    print aa.get_address('no')
    print aa.get_address('dk')
    print aa.get_address('fi')
    print aa.get_address('de')
    print aa.get_address('nl')
    print aa.get_address('at')
    