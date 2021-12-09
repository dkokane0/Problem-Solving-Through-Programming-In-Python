# Function to check Prime Number is Valid or Not Valid
def PrimeChecker(num):  
    # Checking that given number is more than 1  
    if num > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(num/2) + 1):  
            # checking divisibility  
            if (num % j) == 0:  
                print(num, "is not a Valid Prime Number...")  
                break  
        # Else it is a prime number  
        else:  
            print(num, "Valid Prime Number")  
    # If the given number is 1  
    else:  
        print(num, "is not a Valid Prime Number")  
# Taking an input number from the user  
num = int(input(">>>Enter an input number: "))  
# Printing result  
PrimeChecker(num)  
