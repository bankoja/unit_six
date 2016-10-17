# James Bankole 10/17/16 unit 6
# This program prompts the user to input a max number, and then calculates and displays the all primes leading to that
# number.


def getNumber():
    """This function prompts the user for the max number."""
    return int(input("Type in the max number:"))


def maxNL(userNumber):
    """This function creates the number list from 2 to the max number."""
    numberL = [x for x in range(2, userNumber + 1)]
    return numberL


def primesGen(numberList):
    """This function creates the primes list, calculates the primes in the number list, adds the primes in the
     number list to the primes list, then displays the primes list."""
    primesL = []
    while len(numberList) > 0:
        nextPrime = numberList[0]
        primesL.append(nextPrime)
        for x in numberList:
            if x % nextPrime == 0:
                numberList.remove(x)
    print("Yo! your primes are", primesL)


def main():
    userNumber = getNumber()
    numberList = maxNL(userNumber)
    primesGen(numberList)


main()
