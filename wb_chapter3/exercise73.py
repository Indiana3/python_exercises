##
# Given a message from user and a shift amount, for each uppercase
# and lowercase letter of the message 
# determine the corresponding shifted letter 
#

# Read the message from user
message = input("Please, enter your message: ")

# Read the shift amount 
shift_amount = int(input("Please, enter the shift amount: "))

# Initialize an empty list where store the shifted letter
shifted_message_chr_list = []

# For each char of message, check if it's an uppercase or 
# lowercase alphabetical letter and
# determine the corresponding shifted letter
for i in range(len(message)):
    if ord(message[i]) >= 65 and ord(message[i]) <= 90:
        if ord(message[i]) + shift_amount < 65:
            shifted_message_chr_list.append(chr(ord(message[i]) + shift_amount + 26))
        elif ord(message[i]) + shift_amount > 90:
            shifted_message_chr_list.append(chr(ord(message[i]) + shift_amount -26))
        else:
            shifted_message_chr_list.append(chr(ord(message[i]) + shift_amount))
    elif ord(message[i]) >= 97 and ord(message[i]) <= 122:
        if ord(message[i]) + shift_amount < 97:
            shifted_message_chr_list.append(chr(ord(message[i]) + shift_amount + 26))
        elif ord(message[i]) + shift_amount > 122:
            shifted_message_chr_list.append(chr(ord(message[i]) + shift_amount -26))
        else:
            shifted_message_chr_list.append(chr(ord(message[i]) + shift_amount))
    else:
        shifted_message_chr_list.append(message[i])

# Create a new message string from 
# the list storing shifted letters
shifted_message = "".join(shifted_message_chr_list)

# Display the encoded/ decoded message
print(shifted_message)