def main():
    # get initial miles
    initial_miles = float(input("Enter the first odometer reading (miles): "))
    
    # get end miles
    ending_miles = float(input("Enter the second odometer reading (miles): "))

    # amount of gallons
    num_gallons = float(input("Enter the amount of fuel used (gallons): "))

    #calculate mpg
    mpg = miles_per_gallon(initial_miles, ending_miles, num_gallons)

    #calculate liters per 100km
    liters_100k = lit100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{liters_100k:.2f} liters per 100 kilometers")


def miles_per_gallon(initial_miles, ending_miles, num_gallons):
    mpg = abs(ending_miles - initial_miles) / num_gallons
    return mpg

def lit100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()