year = int(input("enter the year: "))


def Leap_check(y):
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                return "leap year"
            else:
                return "not a  leap year"
        else:
            return "Leap year"
    else:
        return "not  a leap year"


print(Leap_check(year))