def hash(inpstr):

    codedstr = ''
    for i in inpstr:
        if i.isalpha():
            if i.islower():
                codedstr += 'a'*(ord(i)-96)+"_"
            elif i.isupper():
                codedstr += 'A'*(ord(i)-64)+"_"
        elif i.isnumeric():
            codedstr += '1'*(ord(i)-47)+"_"
        else:
            codedstr += i+"_"

    return codedstr

def unhash(hashed):

    decoded = ''
    for i in hashed.split('_')[:-1]:
        
        if(i[0]=='1'):
            decoded+= chr(47+len(i))
        elif(i[0]=='a'):
            decoded+= chr(96+len(i))
        elif(i[0]=='A'):
            decoded += chr(64+len(i))
        else:
            decoded += i[0]
    return decoded

def main():
    passwd = input("Enter an alphanumeric password (no underscores please): \n")
    if("_" in passwd):
        print(unhash("AAAAAAAAAAAAAAAAAAAAAAAAA_aaaaaaaaaaaaaaa_aaaaaaaaaaaaaaaaaaaaa_ _aaaaaaaaaaaaaa_a_aaaaaaaaaaaaaaaaaaaaa_aaaaaaa_aaaaaaaa_aaaaaaaaaaaaaaaaaaaa_aaaaaaaaaaaaaaaaaaaaaaaaa_ _aaaaaaaaaaaa_aaaaaaaaa_aaaaaaaaaaaaaaaaaaaa_aaaaaaaaaaaaaaaaaaaa_aaaaaaaaaaaa_aaaaa_ _aaaa_aaaaa_aaaaaaaaaaaaaaaaaaaaaa_aaaaaaaaa_aaaaaaaaaaaa_"))
        main()
        return
    hashed = hash(passwd)
    print('Here is the encrypted password:', hashed)

    print('The original password, now decrypted:',unhash(hashed))

if __name__ =="__main__":
    main()

    

