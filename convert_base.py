import functools
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    def to_base(orig, base):
        new_base = ''
        while orig // base > 0:
            new_base += string.hexdigits[orig % base].upper()
            orig //= base

        new_base += string.hexdigits[orig].upper()
            
        return new_base[-1::-1]

    is_negative = num_as_string[0] == '-'
    orig = functools.reduce(lambda total, c: total * b1 + string.hexdigits.index(c.lower()),
                                num_as_string[is_negative:], 0)
    print(orig)
    
    return ('-' if is_negative else '') + to_base(orig, b2)

print(convert_base('4B5C', 14, 5))
