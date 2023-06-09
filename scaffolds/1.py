def filter_chars(string):
    return ''.join(filter(lambda x: x.isalpha(), string))

filter_chars('abc123@#$%^ ,./abc')