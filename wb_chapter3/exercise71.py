##
# Display the first 15 approximation of pi
#

# Initialize:
# pi value to closest integer (3)
# first denominator factor of the series term
# second denominator factor of the series term
# third denominator factor of the series term
# the number of term is going to be added to the series
pi = 3
den_fact_1 = 2
den_fact_2 = 3
den_fact_3 = 4
counter = 1

while counter <= 15:
    series_term = 4 / (den_fact_1 * den_fact_2 * den_fact_3)
    # Add the term if its number in the series is odd
    if counter % 2 == 1:
        pi = pi + series_term
    # Subtract the term if its number in the series is even
    else:
        pi = pi - series_term
    # Print the n approximation
    print("The", counter, "°approximation is", pi)
    den_fact_1 = den_fact_1 + 2
    den_fact_2 = den_fact_2 + 2
    den_fact_3 = den_fact_3 + 2
    counter = counter + 1

