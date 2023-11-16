
# Initialization of Cities and Drivers
Cities = ["Beirut", "Jounieh", "Jbeil", "Tripoli", "Tyre", "Saida", "Baalbeck", "Hermel"]
Drivers = {"Ali": ["Jounieh", "Jbeil", "Tripoli"], "Hussein": ["Beirut", "Saida", "Tyre"], "Jad": ["Baalbeck", "Hermel"]}

# Function to add a new city to the Cities list
def Add_City(Cities):
    city = input("Name of the city to add: ")
    if city.isalpha() == True:
        if city not in Cities:
            Cities.append(city)
            print(Cities)
            return Cities
        else:
            return Add_City(Cities)

# Function to add a new driver along with the cities the driver will visit
def Add_Driver(Drivers, Cities):
    driver = input("The name of the driver to add:")
    while driver in Drivers or driver.isalpha() == False:
        driver = input("The name of the driver to add:")
    driver_cities = []
    n = int(input("How many cities " + driver + " will visit?"))
    print("Please input the cities that " + driver + " will visit taking into consideration the destinations: ")
    i = 0
    while i < n:
        city = input("City to visit:")
        if city.isalpha() == True and city in Cities:
            driver_cities.append(city)
            i += 1
        else:
            print("The city you've entered is either invalid or doesn't exist. Please try again.")
    Drivers[driver] = driver_cities
    return Drivers

# Function to add a city to the route of an existing driver
def Add_City_To_Route(Drivers, Cities):
    driver = input("The name of the driver:")
    while driver not in Drivers:
        driver = input("The name of the driver (should be existing):")
    city = input("The name of the city to add the route: ")
    while city not in Cities:
        city = input("The name of the city to add the route (should be an existing city): ")
    if city in Drivers[driver]:
        print("City is already in the route of the driver.")
        return

    print("Input:")
    print("1. To add to the beginning of the route")
    print("-1. To add to the end of the route")
    print("#. (any other number) to add that city to the given index")
    pos = int(input("Where to add the city? "))

    if pos == 1:
        Drivers[driver].insert(0, city)
    if pos == -1:
        Drivers[driver].append(city)
    else:
        Drivers[driver].insert(pos, city)
    return Drivers

# Function to delete a city from the route of an existing driver
def Delete_City_From_Route(Drivers):
    driver = input("The name of the driver:")
    while driver not in Drivers:
        driver = input("The name of the driver (should be existing):")
    city = input("The name of the city to delete from route: ")
    while city.isalpha() == False:
        city = input("The name of the city to delete from route (should be a valid city): ")
    if city not in Drivers[driver]:
        print("City is already not in the route.")
        return Drivers
    else:
        Drivers[driver].remove(city)
        return Drivers

# Function to check the deliverability of a package to a specific city
def Delivery(Drivers, Cities):
    city = input("Input the name of the city where you would like to deliver: ")
    if city not in Cities:
        print("Sorry, we don't deliver to" + city)
        return
    else:
        available_drivers = []
        for i in Drivers:
            if city in Drivers[i]:
                available_drivers.append(i)
        print("The list of all the drivers that deliver to " + city)
        print(available_drivers)

# Main Loop
while True:
    # Displaying the menu
    print("Enter:")
    print("1. To add a city")
    print("2. To add a driver")
    print("3. To add a city to the route of a driver")
    print("4. Remove a city from driver's route")
    print("5. To check the deliverability of a package")

    # User input for choice
    choice = input("Choice: ")
    while choice.isdigit() == False:
        choice = input("Make sure to input a valid choice: ")

    # Handling user's choice
    if choice == '1':
        Cities = Add_City(Cities)
        print(Cities)
        continue

    if choice == '2':
        Drivers = Add_Driver(Drivers, Cities)
        print(Drivers)

    if choice == '3':
        Drivers = Add_City_To_Route(Drivers, Cities)
        print(Drivers)

    if choice == '4':
        Drivers = Delete_City_From_Route(Drivers)
        print(Drivers)

    if choice == '5':
        Delivery(Drivers, Cities)