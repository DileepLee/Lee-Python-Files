import re
regex = re.compile (r"(\w+) World")
result = regex.search("Hello World is the easiest world")
if result:
    print(result. start(), result.end())
