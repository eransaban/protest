from __future__ import absolute_import
import string
symbols = string.punctuation  #create a varible with multiple symbols
credit = [] #create an empty list for id checks

"""Classes to catch Specific Errors"""
class CreditCardNot16(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid - Credit Card Must Be 16 Digits"

class StartWithDigits(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid - Credit Card Must Start With Either 4, 5 or 6"

class OnlyDigits(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid - Credit Card Must is Digits 0-9 ONLY!"

class SymbolsUsed(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid - Don't Use any Symbols when typing Credit Card Number"

class Consecutive(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Invalid - 4 Or more Consecutive Repeated Digits Are Not Allowed "

def check_hypens(card):
    """Strip Hypens and store digits for test in credit"""
    global credit
    for i in card:
        if i == u"-":
            pass
        else:
            credit.append(i)
    return credit

def check_credit(arg):
    """Run Tests and raise specific error"""
    global symbols  #imports symbols list
    id = True  #set id value as True
    if len(arg) != 16: #check if number is equal to 16
        id = False
        raise CreditCardNot16
    if arg[0] != u"4" and arg[0] != u"5" and arg[0] != u"6": #check if number start with 4,5,6
        id = False
        raise StartWithDigits
    if any(char.isalpha() for char in arg):  #check if there any letters in numbers
        id = False
        raise OnlyDigits
    if any(char in symbols for char in arg): #check if there's any symbols in the numbers
        id = False
        raise SymbolsUsed
    for i in arg:  #check if there's space in the number (not included in the symbols list)
        if i == u" ":
            id = False
            raise SymbolsUsed
    for i in xrange(len(arg)-3): # check for consecutive and repeated numbers
        if arg[i] == arg[i+1]:
            if arg[i+1] == arg[i + 2]:
                if arg[i + 2] == arg[i + 3]:
                    id = False
                    raise Consecutive
    return id

def main():
    u""" Ask for a credit card number and runs check
    first of all strip hypens and then run test on the remaining digits and raise appropriate error """
    global credit
    creditcard = raw_input("Hi Please enter your Credit Card Number:")
    try:
        check_hypens(creditcard)
        if check_credit(credit) == True:
            print 'Credit Card Number Is Valid'
            credit = []
            main()
    except CreditCardNot16, err1:
        print err1
        credit = []
        main()
    except StartWithDigits, err2:
        print err2
        credit = []
        main()
    except OnlyDigits, err3:
        print err3
        credit = []
        main()
    except SymbolsUsed, err4:
        print err4
        credit = []
        main()
    except Consecutive, err5:
        print err5
        credit = []
        main()
    except:
        print "Invalid Please Try again"
        credit = []
        main()

if __name__ == "__main__":
    main()
