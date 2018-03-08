#!/usr/bin/python

import random
import string

class Phone:
    def __init__(self):
        pass
    
    
    def get_random_phone_number(self, old_number):
        nr = ''
        temp = ''
        digits = string.digits
        for c in old_number:
            print ('%s: %s') % (nr, temp)
            if not c.isdigit():
                nr += c
                if temp.__len__():
                    nr += ''.join(random.choice(digits) for x in range(temp.__len__()))
                    temp = ''
            else:
                temp += c
        nr += ''.join(random.choice(digits) for x in range(temp.__len__()))
        return nr


if __name__ == "__main__":
    pp = Phone()
    print pp.get_random_phone_number('+46 708 685040')
    
                    