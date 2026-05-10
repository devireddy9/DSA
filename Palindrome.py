def palindrome(string):
    reversedstring = ""
    for i in range (len(string)-1,-1,-1):
        reversedstring += string[i]
    if reversedstring.lower() == string.lower():
        return True
    else:
        return False

#better way

def palindrome2(string):
    if len(string) <=1:
        return True
    if string[0] ==string[-1]:
        return palindrome2(string[1:-1])
    return False




print(palindrome("mADAM"))
print(palindrome2("MADAM"))