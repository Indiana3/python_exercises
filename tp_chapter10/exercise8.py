from random import randint

# Determine the number of days in a month (not considering leap years)
# @param m the month passed as integer
# @return number of days
def days(m):
    if m == 2:
        return 28
    elif m == 1 or m == 3 or m == 5 or \
        m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        return 30

# Generate random samples of 23 birthday
# Check if 2 people has birthday on the same day
def main():
    # Generate 23 birthdays and arrange them in a list t
    STUDENTS = 23
    birthdays = []
    for i in range (STUDENTS):
        m = str(randint(1, 12))
        d = str(randint(1, days(m)))
        birthday = [d, m]
        birthdays.append(birthday)
    # Check if in birthdays list a birthday appears twice
    birthday_twice = []
    for i in range (0, len(birthdays)):
        if birthdays[i] in birthdays[:i]:
            birthday_twice.append(birthdays[i])
    # Display each birthday that appears twice or more
    if birthday_twice == []:
        print("Nobody has birthday on the same day")
    else:
        for i in range (len(birthday_twice)):
            print("Two students has birthday on the")
            print("th of ".join(birthday_twice[i]))

# Call the main function
if __name__ == "__main__":
    main()

    

