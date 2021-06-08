## Decompress a run-len encoded list
# @param t a run-len encoded list: a generic element "A"
# is followed by the number of time it occurs in adjacent positions
# @ return a decompressed run-len encoded list
#
def decompression(t):
    # Base Case
    if t == []:
        return []
    
    # Recursive Case
    decompressed = []
    for _ in range(t[1]):
        decompressed.append(t[0])
    return decompressed + decompression(t[2:])

# Scope a main program inside a main function
def main():
    # Demonstrate how decompression function works and display the result
    run_length_encoded_ls = ["A", 3, "B", 6, "C", 12, "D", 7, "E", 1]
    decompressed = decompression(run_length_encoded_ls)
    print("The run-length decompressed list is {}".format(decompressed))

# Call the main function
if __name__ == "__main__":
    main()

    