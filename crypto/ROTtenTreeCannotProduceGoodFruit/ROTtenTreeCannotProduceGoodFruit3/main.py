encoded_message = "Jxu vbqw yi jxu dkcruh ev sxqhqsjuhi jxyi ijhydw mqi ixyvjut tkhydw jxu udshofjyed fhesuii. Hucucruh, jxu squiqh ixyvj yi jxhuu. Mxqj mqi jxyi ixyvj?"

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
    print(f"Decoded message:{decoded_message}. Number of shifts in encryption is: {26-i}")
