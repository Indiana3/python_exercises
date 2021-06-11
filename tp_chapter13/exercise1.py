from string import punctuation

## Create a new text file and write on StarWars
with open("starwars.txt", "w") as fl:
    fl.write("Hello there!\nI'm Obi One Kenobi.\nI'm a Star Wars supporter.\nI'm going to read the new romance focused on the events happened in the Old Republic.\n\
I don't look forward to reading it.")

# Read each line of the file
with open("starwars.txt", "r") as fl:
    line = fl.readline()
    while line != "":
        # Remove whitespaces at the end 
        line = line.strip()

        # Remove punctuation marks 
        for p in punctuation:
            line = line.replace(p, "")
        
        # Store the words of the line in a list
        words = line.split()

        # Create an empty list for uppercased words
        uppercased_words = []
        
        # Capitilize each word and add it to uppercased_words
        for word in words:
            word = word.capitalize()
            uppercased_words.append(word)
        
        # Restore the line with uppercase words
        line = " ".join(uppercased_words)

        # Display the line
        print(line)

        # Move to next line
        line = fl.readline()




    