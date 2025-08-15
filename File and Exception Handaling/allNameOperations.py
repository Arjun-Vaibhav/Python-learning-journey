class NameValidError(BaseException):
    pass
class ZeroLengthError(Exception):
    pass
#==================================================================
def validprocess(name):
    if len(name) == 0:
        raise ZeroLengthError("Name cannot be empty")

    words = name.split()
    for word in words:
        if not word.isalpha():
            raise NameValidError("Name must contain only alphabetic characters")

    return f"'{name}' is a valid name"

#====================================================================
while(True):
    name = input('Enter name:')
    try:
        res = validprocess(name)
    except NameValidError:
        print('{} Invalid Name--Try again!!'.format(name))
    except ZeroLengthError:
        print('your name should not be empty')
    else:
        print(res)
        print('thanks for using program...')
        break
