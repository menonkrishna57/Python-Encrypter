def decrypt(total,encrypted):
    decrypted=""
    for i in range(len(encrypted)):
        decrypted+=chr(ord(encrypted[i])-total)
    print(decrypted)
    return decrypted

decrypt(1466,"؎؟زخךخةך؜؟ך؟ب؝جستخ؟؞")