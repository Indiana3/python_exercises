##
# Check if a string is a palindrome
#

## Determine if a string is a palindrome
# @param s a string
# @return True if s is a palindrome; False otherwise
#
def isPalindrome(s):
    # Create a list with chars to remove from s
    chars_to_remove = [" ", ".", ",", ";", ":", "!", "?"]
    # Remove the chars in the previous list from s (if any)
    new_s = "".join([s[i] for i in range(len(s)) if s[i] not in chars_to_remove])
    # Base case
    if len(new_s) <= 0:
        return True
    # Recusive case
    elif len(new_s) > 1:
        if new_s[0] == new_s[-1]:
            return isPalindrome(new_s[1:-1])
        else:
            return False

# Read a new_string from unew_ser and dinew_splay the renew_sult
def main():
    s = input("Please, enter a string: ")
    if isPalindrome(s):
        print("The string '%s' is a palindrome" % s)
    else:
        print("The string '%s' is not a palindrome" % s)

# Call the main function
if __name__ == "__main__":
    main()