spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(ls:list):
    result = ''
    for i in range(0,len(ls)):
        result += str(ls[i])
        if i == len(ls)-2:
            result += ", and "
        elif i < len(ls)-2:
            result+=', '
    print(result)
    return result

comma_code(spam)