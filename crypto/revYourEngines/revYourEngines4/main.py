
encoded_message = "Xlnnrgnvmg rh hgzbrmt gifv gl dszg blf hzrw blf dlfow wl olmt zugvi gsv nllw gszg blf hzrw rg rm szh ovug."
decoded_message = ""
for char in encoded_message:
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
        decoded_message += chr(ord('Z') - (ord(char) - ord('A')))
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
        decoded_message += chr(ord('z')  - (ord(char) - ord('a'))) 
    else:
        decoded_message += char

print(f"Decoded message is: {decoded_message}")
