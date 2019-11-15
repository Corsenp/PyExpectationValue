
def compute_present_value(FV, r, y):
    bottom = (1 + r)**y
    PV = FV / bottom

    return PV


def get_the_years():
    y = input("enter the number of years\n")

    try:
        y = int(y)
        return y

    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_the_years()

def get_the_rate():
    r = input("enter the rate\n")

    try:
        r = float(r)
        return r
    
    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_the_rate()

def get_future_value():
    FV = input("enter the future value\n")

    try:
        FV = int(FV)
        return FV
    
    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_future_value()

def main():

    FV = get_future_value()
    r = get_the_rate()
    y = get_the_years()

    PV = compute_present_value(FV, r, y)
    print(PV)

main()