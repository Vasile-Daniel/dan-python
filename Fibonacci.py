# Fibonacci - Dan Daniel 12.03.2021

def fibonacci():
    n1 = 0; n2 = 1; count = 0
    while True:
        nterms = int(input("Insert a positive integer number, biger then 1: "))
        if nterms <= 0 or nterms == 1: 
            print("The number must be a positive integer, biger then 1")
        else:
            print("Fibonacci sequence is:")
            while count < nterms:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count +=1
            break
        

fibonacci()