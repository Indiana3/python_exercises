## Copy the text from a .txt file into another .txt file
# Before coping the text, check if a pattern string has occurences in it;
# If so, replace them with a given replacement string
#  
def sed(pat_s, rep_s, filename1, filename2):
    try:
        with open(filename1) as fl:
            lines = fl.readlines()
            for line in lines:
                if pat_s in line:
                    line = line.replace(pat_s, rep_s)
                with open(filename2, "a") as fl:
                    fl.write(line)
    except:
        print("Check if the first file exists or if you have spelled it correctly")

                
# Show what sed function does with an example
sed("This", "Here", "pippol.txt", "pippo2.txt")
