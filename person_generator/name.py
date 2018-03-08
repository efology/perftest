#!/usr/bin/python
# -*- coding: utf-8 -*-


import ConfigParser
import random
import glob
import string

class Names:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('generator.conf')
        self.male_names = []
        self.female_names = []
        self.last_name_tokens = []
        self.prefixes = {'at':[], 'de':[], 'dk':[], 'fi':[], 'nl':[], 'no':[], 'se':[]}
        self.suffixes = {'at':[], 'de':[], 'dk':[], 'fi':[], 'nl':[], 'no':[], 'se':[]}
        self.email_domains = []
        self.load()
        
        
    
    def load(self):
        self.load_first_names()
        self.load_last_names()
        self.load_prefixes()
        self.load_suffixes()
        self.load_email_domains()
        
    
        
    def load_first_names(self):
        for filename in glob.glob(self.config.get('Names','first_names')):
            with open(filename,'r') as fo:
                for line in fo:
                    tokens = line.strip().split(',')
                    if tokens[1] == 'M':
                        self.male_names.append(tokens[0])
                    else:
                        self.female_names.append(tokens[0])
            fo.close()

            
    
    
    
    def load_last_names(self):
        for filename in glob.glob(self.config.get('Names','last_names')):
            with open(filename, 'r') as fo:
                for line in fo:
                    self.last_name_tokens.append(line.strip())
            fo.close()
            
            
            
    def load_prefixes(self):
        for filename in glob.glob(self.config.get('Names','prefixes')):
            with open(filename, 'r') as fo:
                for line in fo:
                    tokens = line.strip().split(',')
                    self.prefixes[tokens[0]].append(tokens[1])
            fo.close()
            
                    

    def load_suffixes(self):
        for filename in glob.glob(self.config.get('Names','suffixes')):
            with open(filename, 'r') as fo:
                for line in fo:
                    tokens = line.strip().split(',')
                    self.suffixes[tokens[0]].append(tokens[1])
            fo.close()
    
    
    
    def load_email_domains(self):
        for filename in glob.glob(self.config.get('Names','emails')):
            with open(filename, 'r') as fo:
                for line in fo:
                    tokens = line.strip().split('@')
                    self.email_domains.append(tokens[1])
            fo.close()    
    
    
        
    def get_name(self, gender, country):
        fname = ''
        if gender == 'f':
            fname = self.female_names[random.randint(0, self.female_names.__len__()-1)]
        else:     
            fname = self.male_names[random.randint(0, self.male_names.__len__()-1)]
        lname = self.get_prefix(country) + self.get_lastname() + self.get_suffix(country)
        email = self.latinize(fname) + '.' + self.latinize(lname) + '@' 
        email += self.email_domains[random.randint(0, self.email_domains.__len__()-1)]
        return fname, lname.capitalize(), email



    def get_prefix(self, country):
        if self.prefixes[country].__len__():
            return self.prefixes[country][random.randint(0, self.prefixes[country].__len__()-1)]
        return ''


    def get_lastname(self):
        return string.lower(self.last_name_tokens[random.randint(0, self.last_name_tokens.__len__()-1)])

    

    def get_suffix(self, country):
        return self.suffixes[country][random.randint(0, self.suffixes[country].__len__()-1)]



    def latinize(self, s):
        for c in s:
            if c=='ä' or c=='å' or c=='á' or c=='à':
                c='a'
            elif c=='ö' or c=='ø':
                c='o'
            elif c=='Ä' or c=='Å' or c=='Á' or c=='À':
                c='A'
            elif c=='Ö' or c=='Ø':
                c='O'
            elif c=='É' or c=='È' or c=='Ë':
                c='E'
            elif c=='é' or c=='è' or c=='ë':
                c='e'
            elif c=='ú' or c=='ù' or c=='ü' or c=='û':
                c='u'
            elif c=='Ú' or c=='Ù' or c=='Ü' or c=='Û':
                c='U'
        return s



if __name__ == "__main__":
    nn = Names()
    print nn.get_name('f', 'se')
    print nn.get_name('m', 'nl')
    print nn.get_name('f', 'de')
    print nn.get_name('m', 'de')
