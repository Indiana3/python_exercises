##
# Redacting text in a file
#

# Read the name of the original text file
text_to_redact = input("Please, enter the text to redact: ")
# Open the file
fl = open(text_to_redact, "r", encoding="utf-8")
# Store the text lines in a list
text_lines = fl.readlines()
# Close the file
fl.close()

# Read the name of sensitive words file
sensitive_words = input("Please, enter the name of sensitive words file: ")
# Open the file
fl = open(sensitive_words, "r", encoding="utf-8")
# Create a set to store all the sensitive words
sensitive_words_set = set()
# For each word in the sensitive words list
for word in fl:
    # Remove EOL chars
    word = word.strip()
    # Add the word to the set
    sensitive_words_set.add(word)
# Close the file
fl.close()

# Read the name of redacted file
redacted_fl = input("Please, enter the name of the redacted file: ")
# Open the file
fl = open(redacted_fl, "w", encoding="utf-8")
# For each line of the original text file
for line in text_lines:
    # Remove EOL chars
    line = line.strip()
    # Split line in a list of words
    line_words = line.split()
    # For each word of line
    for line_word in line_words:
        # If lowercase word is one of the sensitive words,
        # replace it with "***"
        if line_word.lower() in sensitive_words_set:
            line_word = line_word.replace(line_word, "*" * len(line_word))
        # Write the word in redacted file followed by a whitespace
        fl.write(line_word + " ")
    # Write EOL chars at the end of the line
    fl.write("\n")
# Close the file
fl.close()



