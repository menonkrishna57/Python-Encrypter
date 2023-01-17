def totkey(passkey):
    totasc=0
    for i in range(len(passkey)):
        totasc+=ord(passkey[i])
        print(totasc)
    return totasc

def encrypt(env,total):
    encrypted=""
    for i in range(len(env)):
        newchr=ord(env[i])+total
        encrypted=encrypted+chr(newchr)
    return encrypted

print(encrypt("Text to be encrypted",totkey("Hope this works")))

