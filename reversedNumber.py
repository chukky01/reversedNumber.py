
def main():
    
   
    # ask the user for input and then store it in n
    #remember to make n an integer
    n = input("Enter a number and I will print it out in reverse: ")
    n = int(n)
    
    
    #while n is greater than 0
    while n > 0:
        #assign to r the value of the remainder of what's left when you divide the entered input by 10
        r = n % 10
       
       #print out the reversed result  
        print(r)
        
        #The // operator is different from the / operator in Python.
        #The / operator performs a floating-point division, which means that the result of the division could be a decimal number.
        n = n // 10
    

if __name__ == "__main__":
    main()
