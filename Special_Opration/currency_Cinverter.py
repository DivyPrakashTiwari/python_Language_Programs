# Function to convert currency
def conver(x, y, m):
    # Check if the initial currency is USD
    if x == "USD":
        # Convert USD to EUR
        if y == "EUR":
            m = 0.95 * m
            return m
        # Convert USD to INR
        elif y == "INR":
            m = 78.14 * m
            return m
        # Convert USD to THB
        elif y == "THB":
            m = 34.71 * m
            return m
        # Convert USD to CAD
        elif y == "CAD":
            m = 1.28 * m
            return m
        else:
            return m
    # Check if the initial currency is EUR
    elif x == "EUR":
        # Convert EUR to USD
        if y == "USD":
            m = 1.05 * m
            return m
        # Convert EUR to INR
        elif y == "INR":
            m = 82.21 * m
            return m
        # Convert EUR to THB
        elif y == "THB":
            m = 36.52 * m
            return m
        # Convert EUR to CAD
        elif y == "CAD":
            m = 1.34 * m
            return m
        else:
            return m
    # Check if the initial currency is INR
    elif x == "INR":
        # Convert INR to USD
        if y == "USD":
            m = 0.013 * m
            return m
        # Convert INR to EUR
        elif y == "EUR":
            m = 0.012 * m
            return m
        # Convert INR to THB
        elif y == "THB":
            m = 0.44 * m
            return m
        # Convert INR to CAD
        elif y == "CAD":
            m = 0.016 * m
            return m
        else:
            return m
    # Check if the initial currency is THB
    elif x == "THB":
        # Convert THB to USD
        if y == "USD":
            m = 0.029 * m
            return m
        # Convert THB to EUR
        elif y == "EUR":
            m = 0.027 * m
            return m
        # Convert THB to INR
        elif y == "INR":
            m = 2.25 * m
            return m
        # Convert THB to CAD
        elif y == "CAD":
            m = 0.037 * m
            return m
        else:
            return m
    # Check if the initial currency is CAD
    elif x == "CAD":
        # Convert CAD to USD
        if y == "USD":
            m = 0.78 * m
            return m
        # Convert CAD to EUR
        elif y == "EUR":
            m = 0.74 * m
            return m
        # Convert CAD to INR
        elif y == "INR":
            m = 61.19 * m
            return m
        # Convert CAD to THB
        elif y == "THB":
            m = 27.18 * m
            return m
        else:
            return m
    else:
        exit()

# Main program
'_main_'

# Welcome message
print("WELCOME TO THE CURRENCY CONVERTER")

# Print available currencies
print("INITALS OF THE CURRENCY")
print("USD")
print("EUR")
print("INR")
print("THB")
print("CAD")

# Initialize a variable to continue the program
op = "YES"

# Loop until the user decides to stop
while (op == "YES"):
    # Get the initial currency from the user
    om = input("Input initals of the currency you want to convert:")
    om = om.upper()

    # Get the target currency from the user
    cm = input("Input initials of the currency you want your money to be converted to:")
    cm = cm.upper()

    # Get the amount to be converted from the user
    ma = float(input("Input the amount of to be converted:"))

    # Call the conversion function
    con = conver(om, cm, ma)

    # Print the conversion result
    print("The money was in", om, "currency and converted to", cm, "currency.")
    print(ma, om, "------>", con, cm)

    # Ask the user if they want to convert more currency
    print("Do you want to convert more currency ; YES OR NO")
    op = input("")
    op = op.upper()

# Thank you message