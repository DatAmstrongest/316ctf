encoded_message = "23 8 5 14 25 15 21 23 1 14 20 20 15 19 21 3 3 5 5 4 1 19 2 1 4 1 19 25 15 21 23 1 14 20 20 15 2 18 5 1 20 8 5 20 8 5 14 25 15 21 12 12 2 5 19 21 3 3 5 19 19 6 21 12"
decoded_message = ""
for num in encoded_message.split(" "):
    decoded_message += chr(ord('a')+int(num)-1)
print(decoded_message)
