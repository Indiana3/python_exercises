## Check if a list has duplicates of an element
# @param t a list
# @return True if t has duplicates of an element; False otherwise
def has_duplicates(t):
    t1 = []
    for i in range (0, len(t)):
        if t[i] in t1:
            print(t1)
            return True
        t1.append(t[i])
    print(t1)
    return False

# Call has_duplicates function and display the result
def main():
    print(has_duplicates([1, 2, 3, 1]))

# Call the main function
if __name__ == "__main__":
    main()