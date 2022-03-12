def match_symbol(p, s, flag=True):
    return len(s) > 0 and (p[0] == s[0] or p[0] == "." and flag)


def match_q(pattern, string):
    if match_symbol(pattern, string):
        return match_pattern(pattern[2:], string[1:]) or \
               match_pattern(pattern[2:], string)
    return match_pattern(pattern[2:], string)


def match_s(pattern, string):
    if match_symbol(pattern, string):
        return match_pattern(pattern, string[1:]) or \
               match_pattern(pattern[2:], string)
    return match_pattern(pattern[2:], string)


def match_p(pattern, string):
    if match_symbol(pattern, string):
        return match_pattern(pattern[:1] + "*" + pattern[2:], string[1:])
    return False


def match_pattern(pattern, string):
    if pattern == '$' :
        return string == ''
    if pattern == '':
        return True
    if pattern[0] == '\\':
        if match_symbol(pattern[1:], string, False):
            return match_pattern(pattern[2:], string[1:])
        return False
    if len(pattern) > 1 and pattern[1] in ['?', '*', '+'] :
        if pattern[1] == '?':
            return match_q(pattern, string)
        elif pattern[1] == '*':
            return match_s(pattern, string)
        elif pattern[1] == '+':
            return match_p(pattern, string)
    else:
        if match_symbol(pattern, string):
            return match_pattern(pattern[1:], string[1:])
        return False


def match(pattern, string):
    if pattern.startswith('^'):
        return match_pattern(pattern[1:], string)
    if pattern == "":
        return True
    for i in range(0, len(string)):
        if match_pattern(pattern, string[i:]):
            return True
    return False


if __name__ == "__main__":
    pattern_, string_ = input().strip("'").split("|")
    print(match(pattern_, string_))

