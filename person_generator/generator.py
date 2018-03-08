#!/usr/bin/python

import nin
import zipcode
import name
import address
import random


class PersonGenerator:
    def __init__(self):
        self.files = {}
        self.nin = nin.NationalIdentityNumber()
        
    
    def _get_gender(self, female_ratio):
        
        x = random.randint(1,100)
        if x <= female_ratio*100:
            return 'f'
        else:
            return 'm'


    def generate(self, count=100, outfile='person_data.csv', country='se', female_ratio=0.5):
        nn = name.Names()
        aa = address.Address()
        zz = zipcode.Zipcode()

        for i in range(0,count):
            fname, lname, email = nn.get_name(self._get_gender(female_ratio), country)
            addr = aa.get_address(country)
            zipp, place = zz.get_zipcode(country)
            print fname, lname, email, addr, zipp, place
    

if __name__ == "__main__":
    pg = PersonGenerator()
    pg.generate(count=10)

            
            