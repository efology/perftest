#!/usr/bin/python
# -*- coding: utf-8 -*-


class NationalIdentityNumber:
    def __init__(self):
        self.numbers_map = {'at':{}, 'de':{}, 'dk':{}, 'fi':{}, 'nl':{}, 'no':{}, 'se':{}}
        pass



    def get_nin(self, country_code, old_nin):
        if country_code=='at':   # at-15
            return self.get_austrian_nin(old_nin)
        elif country_code=='de': # de-81
            return self.get_german_nin(old_nin)
        elif country_code=='dk': # dk-59
            return self.get_danish_nin(old_nin)
        elif country_code=='fi': # fi-73
            return self.get_finnish_nin(old_nin)
        elif country_code=='nl': # nl-154
            return self.get_dutch_nin(old_nin)
        elif country_code=='no': # no-164
            return self.get_norwegian_nin(old_nin)
        elif country_code=='se': # se-209
            return self.get_swedish_nin(old_nin)
        return ''



    #Swedish NIN
    def get_swedish_nin(self, old_nin):
        date_of_birth = old_nin[:7]
        gender = 'm' if int(old_nin[9])%2 else 'f' # as politically correct as possible, given the circumstances ;-)
        try:
            latest_increment = self.numbers_map['se'][date_of_birth][gender]
            latest_increment += 2
            self.numbers_map['se'][date_of_birth].update({gender:latest_increment})
        except KeyError:
            self.numbers_map['se'].update({date_of_birth:{'f':000,'m':001}})
            latest_increment = 000 if gender=='f' else 001
        chars = []
        chars.extend(date_of_birth + str(latest_increment).zfill(3))
        summ = 0
        bytwo = True
        
        for c in chars:
            if c.isdigit(): 
                if bytwo:
                    temp = int(c)*2
                    bytwo = False
                else:
                    temp = int(c)*1
                    bytwo = True
                tempchars = []
                tempchars.extend(str(temp))
                for t in tempchars:
                    summ += int(t)                

        strsum = str(summ)
        last_digit_c = strsum[strsum.__len__()-1]
        checksum = 10 - int(last_digit_c)
        chars.append(str(checksum)[0])
        return ''.join(chars)
    
    
    #Finnish NIN
    def get_finnish_nin(self, old_nin):
        date_of_birth = old_nin[:7]
        gender = 'm' if int(old_nin[9])%2 else 'f'
        control_table = '0123456789ABCDEFHJKLMNPRSTUVWXY'
        try:
            latest_increment = self.numbers_map['fi'][date_of_birth][gender]
            latest_increment += 2
            self.numbers_map['fi'][date_of_birth].update({gender:latest_increment})
        except KeyError:
            self.numbers_map['fi'].update({date_of_birth:{'f':000,'m':001}})
            latest_increment = 000 if gender=='f' else 001
        nin = date_of_birth + str(latest_increment).zfill(3)
        digits = ''
        for c in nin:
            if c.isdigit():
                digits += c
        nin += control_table[int(digits) % 31]
        return nin


    # Norwegian NIN: http://no.wikipedia.org/wiki/F%C3%B8dselsnummer
    def get_norwegian_nin(self, old_nin):
        date_of_birth = old_nin[:6]
        old_social = old_nin[6:]
        individual_digits = old_social[:3]
        bracket = self.norway_individual_digits_to_bracket(individual_digits)
        gender = 'm' if int(individual_digits[2])%2 else 'f'
        try:
            latest_increment = self.numbers_map['no'][date_of_birth][bracket][gender]
            latest_increment += 2
            self.numbers_map['no'][date_of_birth][bracket].update({gender:latest_increment})
        except KeyError:
            self.numbers_map['no'].update({date_of_birth:{bracket:{'f':bracket+000,'m':bracket+001}}})
            latest_increment = bracket+000 if gender=='f' else bracket+001
        nin = date_of_birth + str(latest_increment).zfill(3)
        nin += self.norway_check_one(nin)
        nin += self.norway_check_two(nin)        
        return nin



    def norway_individual_digits_to_bracket(self, individual_digits):
        n = int(individual_digits)
        if n<=499:
            return 000
        if n>=500:
            return 500



    def norway_check_one(self, nin):
        k1 = (11 - ((3*int(nin[0]) + 7*int(nin[1]) + 6*int(nin[2]) 
             + 1*int(nin[3]) + 8*int(nin[4]) + 9*int(nin[5]) 
             + 4*int(nin[6]) + 5*int(nin[7]) + 2*int(nin[8])) % 11))
        if k1 >= 10:
            k1 = 0
        return str(k1)



    def norway_check_two(self, nin):
        k2 = (11 - ((5*int(nin[0]) + 4*int(nin[1]) + 3*int(nin[2])
             + 2*int(nin[3]) + 7*int(nin[4]) + 6*int(nin[5])
             + 5*int(nin[6]) + 4*int(nin[7]) + 3*int(nin[8])
             + 2*int(nin[9])) % 11))
        if k2 >= 10:
            k2 = 0
        return str(k2)


    #Danish NIN
    def get_danish_nin(self, old_nin):
            
        return



if __name__ == "__main__":
    # example use
    nin = NationalIdentityNumber()
    print nin.get_nin('se','720627-2323')
    print nin.get_nin('se','720627-2323')
    print nin.get_nin('se','720627-9323')
    print nin.get_nin('se','720627-1233')
    print nin.get_nin('fi','720627A1231')

