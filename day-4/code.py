import sys

with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

def get_passport_content(line):
    if sys.version_info < (3,0):
        line = line.replace(":", "':'").replace(" ", "', '").replace("\n", "', '")
    else:
        line = line.translate(line.maketrans({":": "':'", " ": "', '", "\n": "', '"}))
    return eval("{'"+line+"'}")

#PART 1
VALID_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

passports = 0
for line in lines:
    passport_content = get_passport_content(line)
    field_diff = VALID_FIELDS - set(passport_content)
    if field_diff == set() or field_diff ==  {"cid"}:
        passports += 1

print("PART 1 - Number of valid passports : " + str(passports))

#PART 2
import re

def check_height(passport_content):
    height = passport_content.get("hgt", "")
    if height.endswith("cm"):
        return 150 <= int(height[:-2]) <= 193
    if height.endswith("in"):
        return 59 <= int(height[:-2]) <= 76
    return False

EYE_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

FIELD_CHECKS = {
    "byr": lambda passport_content: 1920 <= int(passport_content.get("byr", 0)) <= 2002,
    "iyr": lambda passport_content: 2010 <= int(passport_content.get("iyr", 0)) <= 2020,
    "eyr": lambda passport_content: 2020 <= int(passport_content.get("eyr", 0)) <= 2030,
    "hgt": check_height,
    "hcl": lambda passport_content: re.search("^#[a-f0-9]{6}$", passport_content.get("hcl", "")),
    "pid": lambda passport_content: re.search("^[0-9]{9}$", passport_content.get("pid", "")),
    "ecl": lambda passport_content : passport_content.get("ecl", "") in EYE_COLORS
}

passports = 0
for line in lines:
    passport_content = get_passport_content(line)
    is_valid = True
    for field in FIELD_CHECKS:
        if not FIELD_CHECKS[field](passport_content):
            is_valid = False
            break
    if is_valid:
        passports += 1

print("PART 2 - Number of valid passports : " + str(passports))
