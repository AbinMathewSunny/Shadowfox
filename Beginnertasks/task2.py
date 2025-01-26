# 1. Write a function that takes two arguments, 145 and 'o', and
# uses the `format` function to return a formatted string. Print the
# result. Try to identify the representation used.

def format_example(num, char):
    return format(num, char)
formatted_string = format_example(145, 'o')
print("Formatted:", formatted_string)




# 2. In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π
# r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
# 1.4 liters of water in a square meter, what is the total amount of
# water in the pond? Print the answer without any decimal point in
# it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
# Water per Square Meter


radius = 84  # in meters
pi = 3.14
water_in_a_square_meter = 1.4  # in liters
pond_area = pi * (radius ** 2)
print("Pond Area:", pond_area)
total_water = pond_area * water_in_a_square_meter
print("Total amount of water in the pond ", int(total_water))





# 3. If you cross a 490meterlong street in 7 minutes, calculate your
# speed in meters per second. Print the answer without any decimal
# point in it. Hint: Speed = Distance / Time



distance = 490  # in meters
timeminutes = 7  # in minutes
timeseconds = timeminutes * 60  # converting time to seconds
speed = distance / timeseconds
print("Speed:", int(speed))

