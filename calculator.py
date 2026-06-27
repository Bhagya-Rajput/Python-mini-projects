try :
    condition = True
    Result = 0
    while condition :   
        a,b  = map(int, input("Enter numbers  separated by space: ").split(" "))
        operator = input(" enter the operation you want to do")
        match operator:
            case "+":
                Result += a+b
            case "-":
                Result += a-b
            case "*":
                Result += a*b
            case "/":
                Result += a/b
            case "//":
                Result += a//b
            case "%":
                Result += a%b
            case "**":
                Result += a**b 
            case _:
                print("entered ivalid operator")
        if type(Result) == float:
          print(f"your result is:{Result:.2f}")
        else :
          print(f"your result is:{Result}")

        retaken = input("if you want to continue enter { Yes }/{ New operation }/{ Quit }").capitalize()
        condition = True if retaken =="Yes" else False

except ValueError:
    print("You enterd wrong Input")
except ZeroDivisionError:
    print("You are trying to divide by zero")


