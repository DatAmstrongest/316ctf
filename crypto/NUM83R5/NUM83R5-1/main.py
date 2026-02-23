encoded_message = "20 8 5 6 12 1 7 20 15 20 8 9 19 3 8 1 12 12 5 14 7 5 9 19 26 5 2 18 1"
decoded_message = ""
for num in encoded_message.split(" "):
    decoded_message += chr(ord('a')+int(num)-1)
print(decoded_message)
