import string

def validPalindrome(s):
    print(s)
    strippedStr = s.translate(str.maketrans('', '', string.punctuation))
    strippedStr = strippedStr.lower()
    strippedStr = "".join(strippedStr.split())
    print(strippedStr)
    ptr1 = 0
    ptr2 = len(strippedStr) - 1
    while strippedStr[ptr1] == strippedStr[ptr2]:
        if ptr1 >= ptr2:
            return True
        ptr1 += 1
        ptr2 -= 1
    return False


def main():
    s = "A man, a plan, a canal: Panama"
    print(validPalindrome(s))

if __name__ == '__main__':
    main()

