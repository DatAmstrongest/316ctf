
encoded_message = "Kvlkov nzb svzi blfi dliwh, yfg gsvb uvvo blfi zggrgfwv. - Qlsm X. Nzcdvoo"
decoded_message = ""
for char in encoded_message:
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
        decoded_message += chr(ord('Z') - (ord(char) - ord('A')))
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
        decoded_message += chr(ord('z')  - (ord(char) - ord('a'))) 
    else:
        decoded_message += char

print(f"Decoded message is: {decoded_message}")
