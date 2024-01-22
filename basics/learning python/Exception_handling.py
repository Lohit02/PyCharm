#exception occurs when some violence of basic mathematical rules
# finally always be executed


try:
    numerator=int(input("Enter the dividend : "))
    denominator=int(input("Enter the divisor: "))
    result= numerator/denominator
    print(result)
except ZeroDivisionError:
    print("You can;t divide something by Zero")

except ValueError as e:
    print(e)
except Exception:
    print("Something Went Wrong")

finally:
    print("This file always will be executed")