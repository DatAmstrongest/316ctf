encoded_message = "Wkh iodj lv wkh qdph ri wkh shuvrq wkdw vkliwhg klv ohwwhuv wkuhh vsdfhv d ihz ghfdghv ehiruh Fkulvw. Wklv flskhu lv qdphg diwhu klp."

for i in range(1,26):
    decoded_message = ""
    for char in encoded_message:
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            if ord(char)+i > ord('Z'):
                decoded_message += chr(ord('A') + (ord(char)+i - ord('Z')-1))
            else:
                decoded_message += chr(ord(char)+i)
        elif ord(char) >= ord('a') and ord(char) <= ord('z'):
            if ord(char)+i > ord('z'):
                decoded_message += chr(ord('a') + (ord(char)+i - ord('z')-1))
            else:
                decoded_message += chr(ord(char)+i)
        else:
            decoded_message += char
    print(f"Decoded message:{decoded_message}")
