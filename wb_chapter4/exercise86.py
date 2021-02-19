## Return the total taxi fare
# @param dist distance travelled in km
def taxi_fare(distance):
    BASE_FARE = 4
    ADDITIONAL_FARE = 0.25
    ADDITIONAL_FARE_KM = 0.14
    additional_fare_paid = distance / ADDITIONAL_FARE_KM * \
    ADDITIONAL_FARE
    total_fare = BASE_FARE + additional_fare_paid
    return total_fare

# Read a distance in km from user
distance = float(input("Please, enter your distance travelled in taxi: "))

# Compute the distance calling taxi_fare() and
# display the result
print("The taxi fare for %.2f km is $%.2f" % (distance, taxi_fare(distance)))