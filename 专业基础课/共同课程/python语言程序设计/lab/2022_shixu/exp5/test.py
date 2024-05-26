import re
def split_string(s):
    m = re.match(r'^\D+', s)
    if m:
        prefix = m.group()

        s = s[len(prefix):]
    else:
        prefix = ''
    parts = s.split()
    result = [prefix] + parts
    return result

print(split_string("A-Chuan Hsueh 6680 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"))
