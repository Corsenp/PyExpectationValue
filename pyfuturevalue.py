def compute_the_future_value(PV, r, y):
    FV = PV*((1 + r)**y)

    return FV

def get_present_value():
    PV = input("enter present value\n")

    try:
        PV = int(PV)
        return PV

    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_present_value()

def get_the_rate():
    r = input("enter the annual interest\n")

    try:
        r = float(r)
        return r

    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_the_rate()

def get_the_years():
    y = input("enter the number of years\n")

    try:
        y = int(y)
        return y

    except ValueError:
        print("ERROR : Not a correct Value\n")
        get_the_years()

def main():
    PV = get_present_value()
    r = get_the_rate()
    y = get_the_years()

    FV = compute_the_future_value(PV, r, y)
    print(FV)

main()