import re

class Passport:
    def __init__(self, raw_data):
        self.expiration = int(raw_data.get('eyr', -1))
        self.birth = int(raw_data.get('byr', -1))
        self.issued = int(raw_data.get('iyr', -1))
        self.height = raw_data.get('hgt', 'Unknown')
        self.hair_color = raw_data.get('hcl', 'Unknown')
        self.eye_color = raw_data.get('ecl', 'Unknown')
        #if raw_data.get('pid') and raw_data.get('pid').isdigit():
        #    self.pid = int(raw_data.get('pid'))
        #else:
        #    self.pid = 0 
        self.pid = raw_data.get('pid', 'Unknown')

        self.cid = int(raw_data.get('cid', -1))

    def is_height_valid(self):
        if not (self.height[-2:] == "cm" or self.height[-2:] == "in"):
            return False
        
        h = self.height[:-2]
        print(f"{h}")
        if not h.isdigit():
            return False

        if self.height[-2:] == "cm":
            return 150 <= int(h) <= 193 

        if self.height[-2:] == "in":
            return 59 <= int(h) <= 76 
        return True

    def is_hair_color_valid(self):
        return len(self.hair_color) == 7 and re.match(r"^#\w", self.hair_color)

    def is_eye_color_valid(self):
        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.eye_color in valid_colors

    def is_passport_id_valid(self):
        return len(self.pid) == 9 and self.pid.isdigit()

    def is_valid(self):
        return (2020 <= self.expiration <= 2030) and (1919 < self.birth < 2003) and \
            (2009 < self.issued < 2021) and self.is_passport_id_valid() and \
            self.is_height_valid() and self.is_hair_color_valid() and \
            self.is_eye_color_valid()

def parse_passports(data_file):
    passports = []

    with open(data_file) as fp:
        data = fp.read()
        unparsed_passports = data.split("\n\n") # split by new lines
        for p in unparsed_passports:
            temp = p.split("\n") #split data lines into attributes
            attrs = [x.split(" ") for x in temp]
            flattened = [attr for sublist in attrs for attr in sublist]
            passport = {}
            for attr in flattened:
                if attr.find(":") == -1:
                    continue
                passport[attr.split(":")[0]] = attr.split(":")[1]
            
            passports.append(passport)

        return passports

if __name__ == '__main__':
    data = parse_passports('passport_data.txt')
    passports = [Passport(x) for x in data]

    print(f"Number of valid passports: {len([valid for valid in passports if valid.is_valid()])} ")