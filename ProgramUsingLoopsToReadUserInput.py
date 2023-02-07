# Task 1 A, Build a program that calculates the average price of a house in a given neighborhood

# Introduction to program
print("\nWelcome to my real estate average price calculator!")

# Create Variable to store Name of neighborhood
Neighborhood = str(input("\nEnter the neighborhood name: "))

# Create a Empty list to store house values
Home_List = []

# Create function to calculate average
def Average(l):
    avg = sum(l) / len(l)
    return avg

# Set loop for when input = y, Add Houseprices to the list
while input("\nWould you like to add the price of one more house?") == "y":
    HousePrices = int(input("Enter house price: "))
    Home_List.append(HousePrices)

# Calculate Average of the homes, and disply print statements
average = Average(Home_List)
print("\nThe average house price in the " + Neighborhood + " Neighborhood is", average)
print("\nThanks for using the App!")



# Task 1 B, Adjust your app from part a, calculate the sum, max, min, and average

# Introduction to program
print("\nWelcome to my real estate average price calculator!")

# Create Variable to store Name of neighborhood
Neighborhood = str(input("\nEnter the neighborhood name: "))

# Create a Empty list to store house values
Home_List = []

# Create function to calculate average
def Average(l):
    avg = sum(l) / len(l)
    return avg

# Set loop for when input = y, Add Houseprices to the list
while input("\nWould you like to add the price of one more house?") == "y":
    HousePrices = int(input("Enter house price: "))
    Home_List.append(HousePrices)

# Calculate the average of the homes, and disply print statements with count, min, max, and sum
average = Average(Home_List)
print("\nYou have entered", len(Home_List), "values ,", "sum is", sum(Home_List),",",
"max is",max(Home_List) ,",","min is",min(Home_List) )
print("\nThe average house price in the " + Neighborhood + " Neighborhood is", average)