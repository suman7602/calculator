a = input("Please enter your name=")
print("welcome",a)
choice = int (input("'1' for age calculate:\n'2' for number calculate:\n'3' for Temperature calculate:\n'4' for Length "
                    "calculate:\n"))
if choice == 1:
    import datetime
    birth_year = int(input("enter tour birth year"))
    a1 = datetime.datetime.now().year-birth_year
    birth_month = int(input("Enter your birth month"))
    a2 = 12-birth_month
    birth_day = int(input("enter your birth day"))
    a3 = 30-birth_day
    print(a,"you are",a1,"years",a2,"months",a3,"days old")

elif choice == 2:
    print("please enter the 1st no:=")
    n1 = input()
    print("please enter the 2nd no:=")
    n2 = input()
    choice =(int(input("'1' for Addition(+)\n'2' for Subtraction(-)\n'3' for Multiplication(*)\n'4' for Division(/)\n")))
    if choice == 1:
        print("you want to  Addition(+)")
        a1 = (float(n1) +float(n2))
        print(n1,"+",n2,"=", a1)
    elif choice == 2:
        print("you want to Subtraction(-)")
        a2 = (float(n1) - float(n2))
        print(n1, "-", n2, "=", a2)
    elif choice==3:
        print("you want to Multiplication(*)")
        a3 = (float(n1) * float(n2))
        print(n1, "*", n2, "=", a3)
    elif choice==4:
        print("you want to Division(/)")
        a4 = (float(n1) / float(n2))
        print(n1, "/", n2, "=", a4)
elif choice == 3:
    choice= (int (input("'1' celsius to fahrenheit:\n'2' Fahrenheit to celsius:\n")))
    if choice == 1:
        C = int(input("Enter a temperature in Celsius:"))
        F = (C*1.8)+32
        print("Temperature:",C,"celsius=",F,"fahrenheit.")
    elif choice == 2:
        F =int(input( "Enter a temperature in fahrenheit:"))
        C = (F-32)*1/1.8
        print("Temperature:",F,"fahrenheit=",C,"celsius.")
elif choice ==4:
    choice =(int(input("'1' your height calculate:\n'2' Length calculate:\n")))
    if choice == 1:
        choice =int(input("press '1' for calculate your height in CM:\n press '2' for calculate your height in inches "
                          "and feet:\n"))
        if choice ==1:
            print("Enter your height: ")
            h_ft = int(input("Feet:"))
            h_inch = int(input("Inches"))
            h_inch +=h_ft*12
            h_cm = round((h_inch*2.54),1)
            print("your height is",h_cm,"cm")
        elif choice ==2:
            cm = int(input("Enter your Height in CM: "))
            inches = 0.394*cm
            feet = 0.0328*cm
            print("your height is:",round(inches,2),"inches")
            print("your height is:",round(feet,2),"feet")
    elif choice ==2:
        choice = int(input("press '1' for convert inches to feet:\npress '2' for convert inches to CM:\npress '3' for "
                           "convert CM to inches and feet:\n"))
        if choice ==1:
            inches = float(input("Enter the length in inches:"))
            feet = inches/12
            print("The length:",inches,"inches=",feet,"feet")
        elif choice ==2:
            inches = float(input("Enter the length in inches:"))
            CM = 2.54*inches
            print("The length:",inches,"inches=",CM,"centimeter")
        elif choice ==3:
            cm = int(input("Enter the length in CM: "))
            inches = 0.394 * cm
            feet = 0.0328 * cm
            print(cm,"CM=", round(inches, 2), "inches")
            print(cm,"CM=", round(feet, 2), "feet")