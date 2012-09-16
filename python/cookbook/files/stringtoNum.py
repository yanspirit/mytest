import re

re_digits = re.comile(r'(\d+)')
def embedded_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2]=map(int,pieces[1::2])
    return pieces
def sort_strings_with_embedded_numbers(alist):
    aux=[(embedded_numbers(s),s) for s in alist]
    aux.sort()
    return [s for __, s in aux]
'''return sorted(alist,key=embedded_numbers)'''


print ''.join(sort_strings_with_embedded_numbers(files))

