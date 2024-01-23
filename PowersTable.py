user = int(input("Enter an integer: "))

print("{:<10} {:<10} {:<10}".format("Number", "Squared", "Cubed"))
print("{:<10} {:<10} {:<10}".format("======","======","======"))
#print(str(user)+"         "+str(user*user)+"         "+str(user**3))

for i in range (1, user+1):
    print("{:<10} {:<10} {:<10}".format(i, i**2, i**3))

for i in range(1, user * 1):
        print("{:<10} {:<10} {:<10} {:<10}".format(i, i * 2, i * 3, i * 4))