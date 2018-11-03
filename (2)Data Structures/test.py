def checkio(*args):
    if args :
        x=sorted(args)
        a = x[0]
        b = x[-1]
        return a - b
    else:
        return None


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    print(almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2")
