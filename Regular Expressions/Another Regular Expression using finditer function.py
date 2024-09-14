import re
regex = r"([a-z A-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 25, Dec 9, Feb")
for match in matches :
    print("Match at index : ", match.start(), match.end())