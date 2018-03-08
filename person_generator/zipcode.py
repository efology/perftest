#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import glob
import random

class Zipcode:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('generator.conf')
        self.zipcodes = {}
        for filename in glob.glob(config.get('Zipcode','zipcode_data')):
            self.parse_zipcode_file(filename)
    

    def parse_zipcode_file(self, filename):
        filename_tokens = filename.split('\\')
        country_abbr = filename_tokens[filename_tokens.__len__()-1][:2]
        d = {'zipcode':[], 'place':[]}
        with open(filename,'r') as fo:
            for line in fo:
                tokens = line.split(',')
                d['zipcode'].append(tokens[0])
                d['place'].append(tokens[1].decode('iso-8859-15'))
        self.zipcodes.update({country_abbr:d})


    def get_zipcode(self, country):
        codes = self.zipcodes[country]['zipcode']
        places = self.zipcodes[country]['place']
        index = random.randint(0,codes.__len__()-1)
        return codes[index], places[index]



if __name__ == "__main__":
    zz = Zipcode()
    import time
    t0 = time.time()
    count = 10000000
    for i in range(0,count):
        a,b = zz.get_zipcode('se')
        #print a,b
    t1 = time.time()
    print "fetched %d random zip codes in %f seconds" % (count, (t1 - t0))



