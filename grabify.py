import re

# Matches everything between two texts, returns the first match, Returns: str or False
def grab(string, start, end):
    match = re.search(r'%s[^<]*%s' % (start, end), string)
    if match:
        return match.group().split(start)[1][:-len(end)]
    else:
        return False

# Matches everything between two texts, returns list of matches, Returns: list or False
def graball(string, start, end):
    matches = re.findall(r'%s[^<]*%s' % (start, end), string)
    if matches:
        return matches
    else:
        return False

# Grabs all the emails, Returns: list or False
def emails(string):
    matches = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', string)
    if matches:
        return matches
    else:
        return False

# Grabs all the phone numbers, Returns: list or False
def numbers(string):
    matches = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', string)
    if matches:
        return matches
    else:
        return False
