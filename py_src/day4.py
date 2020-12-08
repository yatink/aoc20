import re
lines = """<paste problem input here>"""

invalid_lines="""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid_lines = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

parsed_input = lines.replace(" ", "\n").split("\n")

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl',
                   'ecl', 'pid'}

valid_passports = 0
invalid_passports = 0
passport = {}

def check_passport(passport):
    if required_fields - set(passport.keys()):
        return False
    byr = 1920 <= int(passport['byr']) <= 2002
    iyr = 2010 <= int(passport['iyr']) <= 2020
    eyr = 2020 <= int(passport['eyr']) <= 2030
    if passport['hgt'][-2:] == 'cm':
        hgt = 150 <= int(passport['hgt'][:-2]) <= 193
    elif passport['hgt'][-2:] == 'in':
        hgt = 59 <= int(passport['hgt'][:-2]) <= 76
    else:
        hgt = False
    hcl_re = re.compile('^#[0-9a-z]{6}$')
    hcl = bool(hcl_re.match(passport['hcl']))
    ecl = passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    pid_re = re.compile('^[0-9]{9}$')
    pid = bool(pid_re.match(passport['pid']))
    return byr and iyr and eyr and hgt and hcl and ecl and pid


for entry in parsed_input:
    if entry == '':
        if not check_passport(passport):
            invalid_passports += 1
        else:
            valid_passports += 1
        passport={}
    else:
        try:
            key,value=entry.split(":")
        except ValueError:
            import pdb; pdb.set_trace()
        passport[key]=value
import pdb; pdb.set_trace()
if not check_passport(passport):
    invalid_passports += 1
else:
    valid_passports += 1

print valid_passports
print invalid_passports
