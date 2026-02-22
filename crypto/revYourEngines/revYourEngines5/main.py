
encoded_message = "Olivn rkhfn wloli hrg znvg, xlmhvxgvgfi zwrkrhxrmt vorg, hvw wl vrfhnlw gvnkli rmxrwrwfmg fg ozyliv vg wloliv nztmz zorjfz. Fg vmrn zw nrmrn evmrzn, jfrh mlhgifw vcvixrgzgrlm fooznxl ozylirh mrhr fg zorjfrk vc vz xlnnlwl xlmhvjfzg. Wfrh zfgv rifiv wloli rm ivkivsvmwvirg rm elofkgzgv evorg vhhv xroofn wloliv vf uftrzg mfooz kzirzgfi. Vcxvkgvfi hrmg lxxzvxzg xfkrwzgzg mlm kilrwvmg, hfmg rm xfokz jfr luurxrz wvhvifmg nloorg zmrn rw vhg ozylifn"
decoded_message = ""
for char in encoded_message:
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
        decoded_message += chr(ord('Z') - (ord(char) - ord('A')))
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
        decoded_message += chr(ord('z')  - (ord(char) - ord('a'))) 
    else:
        decoded_message += char

print(f"Decoded message is: {decoded_message}")
