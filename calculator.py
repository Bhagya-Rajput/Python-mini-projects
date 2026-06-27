condition = True
Result = 0
continued = False
while condition :   
    try:
        if continued:
          a = Result
          b = int(input("enter new value"))
          print(f"{a},{b}= previous{Result}")
        else:
           a,b  = map(int, input("Enter numbers  separated by space: ").split(" "))
        operator = input(" enter the operation you want to do")
        match operator:
            case "+":
                Result = a+b
            case "-":
                Result = a-b
            case "*":
                Result = a*b
            case "/":
                Result = a/b
            case "//":
                Result = a//b
            case "%":
                Result = a%b
            case "**":
                Result = a**b 
            case _:
                print("entered invalid operator")
                continue
        if isinstance(Result,float):
          print(f"your result is:{Result:.2f}")
        else :
          print(f"your result is:{Result}")

        retaken = input("if you want to continue enter { Yes -> Y}/{ New operation ->C}/{ Quit }").strip().upper()
        if(retaken == "Y"):
         continued = retaken == "Y"
        elif(retaken == "C"): 
         Result = 0
         continued = False
        else:
         break
    except ValueError as e:
        print("You enterd wrong Input",e)
    except ZeroDivisionError:
        print("You are trying to divide by zero")




