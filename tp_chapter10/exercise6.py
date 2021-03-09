## Check if 2 strings are anagrams
# @param s the first string
# @param v the second string
# @return True if t and v are anagrams; False otherwise
def is_anagram(s, v):
    # Convert s string and v string into lists
    # Arrange elements of both lists in ascending order
    s = list(s)
    s.sort()
    v = list(v)
    v.sort()
    if s == v:
        return True
    return False

# Call the is_anagram function and display the result
print(is_anagram("perry", "riper"))
    