
encoded_message = "Uif gmbh jt Cfbujuveft"

for i in range(1,26):
    decoded_message = ""
    for char in encoded_message:
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            decoded_message += chr(ord('A') + (ord(char)+i)%ord('Z'))
        elif ord(char) >= ord('a') and ord(char) <= ord('z'):
            decoded_message += chr(ord('a') + (ord(char)+i)%ord('z'))
        else:
            decoded_message += char
    print(decoded_message)
