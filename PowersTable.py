confirm = "y"
while confirm == "y":
    user = int(input("Enter an integer: "))
    print("{:<10} {:<10} {:<10}".format("Number", "Squared", "Cubed")) # start of table format
    print("{:<10} {:<10} {:<10}".format("======","======","======"))
    #print(str(user)+"         "+str(user*user)+"         "+str(user**3))

    for i in range (1, user+1):
        print("{:<10} {:<10} {:<10}".format(i, i**2, i**3))

    print("Multiplication table below")
    for i in range(1, user * 1): # start of multi table
        print("{:<10} {:<10} {:<10} {:<10}".format(i, i * 2, i * 3, i * 4))
    confirm = input("do you want to continue (y/n)? ")