for number in range(2,100):
    for i in range(2,number):
        if (number % i) == 0:
            j=number/i                                          # to calculate the second factor
            print("{0} equals {1} * {2}").format(number,i,j)
            break
    else:
        print("{0} is a prime number").format(number)