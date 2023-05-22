#calculate windchill
def wind_chill (t, v):
    return 35.74 + (0.6215*t) - (35.75*(v**0.16)) + (0.4275*t*(v**0.16))

def c_convertion (t):
    '''
    This function converts Celcius to Farenheit

    Parameters:
    t = temperature in Celcius

    Returns:
    Temperature in Farenheit
    '''
    return t * 9/5 + 32
    

# temperature in fahrenheit
t = float(input("\nWhat is the temperature? "))

# degree type
degree_type = input("Fahrenheit or Celsius (F/C)? ").upper()

if degree_type == "C":
    t = c_convertion(t)

#wind speed in miles per hour
for v in range(5, 61, 5):
   #printing wind_chill
    windchills = wind_chill(t, v)
    print(f"At temperature {t}F, and wind speed {v} mph, the windchill is: {windchills:.2f}F")








