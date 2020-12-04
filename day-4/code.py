with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

VALID_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
}

def get_passport_content(line):
    line = line.translate(line.maketrans({":": "':'", " ": "', '", "\n": "', '"}))
    return eval("{'"+line+"'}")

#PART 1
passports = 0
for line in lines:
    passport_content = get_passport_content(line)
    field_diff = VALID_FIELDS - set(passport_content)
    if field_diff == set() or field_diff ==  {"cid"}:
        passports += 1

print("PART 1 - Number of valid passports : " + str(passports))

#PART 2
import re
check_birth_year = lambda passport_content: 1920 <= int(passport_content.get("byr", 0)) <= 2002

check_issue_year = lambda passport_content: 2010 <= int(passport_content.get("iyr", 0)) <= 2020

check_exp_year = lambda passport_content: 2020 <= int(passport_content.get("eyr", 0)) <= 2030

def check_height(passport_content):
    height = passport_content.get("hgt", "")
    if height.endswith("cm"):
        return 150 <= int(height[:-2]) <= 193
    if height.endswith("in"):
        return 59 <= int(height[:-2]) <= 76
    return False

check_haircolor = lambda passport_content: re.search("^#[a-f0-9]{6}$", passport_content.get("hcl", ""))

check_id = lambda passport_content: re.search("^[0-9]{9}$", passport_content.get("pid", ""))

EYE_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
check_eye_color = lambda passport_content : passport_content.get("ecl", "") in EYE_COLORS

FIELD_CHECKS = {
    "byr": check_birth_year,
    "iyr": check_issue_year,
    "eyr": check_exp_year,
    "hgt": check_height,
    "hcl": check_haircolor,
    "pid": check_id,
    "ecl": check_eye_color
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
