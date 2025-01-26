# 1. Write a program to determine the BMI Category based on user input.
# Ask the user to:
# Enter height in meters
# Enter weight in kilograms
# Calculate BMI using the formula: BMI = weight / (height)2
# Use the following categories:
# If BMI is 30 or greater, print "Obesity"
# If BMI is between 25 and 29, print "Overweight"
# If BMI is between 18.5 and 25, print "Normal"
# If BMI is less than 18.5, print "Underweight"
# Example:
# Enter height in meters: 1.75
# Enter weight in kilograms: 70
# Output: "Normal"

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")



# 2. Write a program to determine which country a city belongs to. Given
# list of cities per country:
# Australia = ["Sydney","Melbourne""Brisbane""Perth"]

# UAE = ["Dubai",
# "Abu Dhabi",
# "Sharjah"
# ,
# "Ajman"]

# India = ["Mumbai"
# ,
# "Bangalore"
# ,
# "Chennai"
# ,
# "Delhi"]

# Ask the user to enter a city name and print the corresponding country.    



cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city_name = input("Enter a city name: ")

for country, city_list in cities.items():
    if city_name in city_list:
        print(f"{city_name} is in {country}")
        break
else:
    print("City not found")




# 3. Write a program to check if two cities belong to the same country.
# Ask the user to enter two cities and print whether they belong to the
# same country or not.


# 3. Program to check if two cities belong to the same country.

cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

same = False

for country, city_list in cities.items():
    if city1 in city_list and city2 in city_list:
        print(f"Both cities are in {country}")
        same = True
        break

if not same:
    print("They don't belong to the same country")