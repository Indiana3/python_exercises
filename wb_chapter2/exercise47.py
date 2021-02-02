##
# Display the season associated with the date entered
#

# Read the month and day from the user
print("Please, enter: ")
month = input("a month (e.g. January): ")
day = int(input("a day of the month: "))

# Convert month string to lowercase
month = month.lower()

# Determine the season that matches the date entered
if month == "april" or month == "may":
    season = "spring"
elif month == "june":
    if day < 21:
        season = "spring"
    else:
        season = "summer"
elif month == "july" or month == "august":
    season = "summer"
elif month == "september":
    if day < 22:
        season = "summer"
    else:
        season = "autumn"
elif month == "october" or month == "november":
    season = "autumn"
elif month == "december":
    if day < 21:
        season = "autumn"
    else:
        season = "winter"
elif month == "january" or month == "february":
    season = "winter"
elif month == "march":
    if day < 20:
        season = "winter"
    else:
        season = "spring"

# Display the result
print(month.capitalize(), day, "is", season)
    