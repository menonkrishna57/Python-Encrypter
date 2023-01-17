def tot(enc):
    trot=0
    for i in range(len(enc)):
        asc=ord(enc[i])
        trot+=asc
    print(trot)
tot("sus") 
