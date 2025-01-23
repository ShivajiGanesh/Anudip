#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#...................WHILE IS ALREADY TRUE................#
while True:
    num1 = input("Enter number 1: ")
    if not num1.isdigit():   #TAKES NUM1 ONLY AS DIGIT
        print("Error: You can only enter numbers.")
        continue
        
    num2 = input("Enter number 2: ")
    if not num2.isdigit():   # TAKES NUM2 ONLY AS DIGIT
        print("Error: You can only enter numbers.")
        continue

    chose = input("Choose function a,m,d,s,M or 'q' to quit: ") #USER CAN CHOOSE WHICH OPERATION TO PERFORM
 
    if chose == 'q':    # IF USER ENTER "q" IT ENDS THE PROGRAM USING BREAK
        print("Hope You Find Your Answers")
        break
#...................OPERATIONS..........................#
    a = int(num1) + int(num2)
    m = int(num1) * int(num2)
    s = int(num1) - int(num2)

    if chose == 'd':
        if int(num2) != 0:       #THIS CONDITION IS TO SATISFY ZERO DIVIISION ERROR
            d = int(num1) / int(num2)
            print(d)
        else:
            print("Error: You cannot divide a number by zero.")
    elif chose == 'M':
        if int(num2) != 0:      #THIS CONDITION IS TO SATISFY ZERO MODULUS ERROR
            print(int(num1) % int(num2))
        else:
            print("Error: You cannot perform modulus by zero.")
    elif chose == 'a':
        print(a)
    elif chose == 'm':
        print(m)
    elif chose == 's':
        print(s)
    else:
        print("Invalid function")      #PRINTS IF CHOSE IS OUT OF MENTION(a,s,d,m,M)

