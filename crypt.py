
def hash(inpstr):

    codedstr = ''

    for i in inpstr[:]:
        if i.isalpha():
            codedstr += 'a'*(ord(i)-96)+"_"
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
        else:
            decoded += i[0]
    return decoded

def main():
    passwd = input("Enter an alphanumeric password (no underscores please): \n")
    if("_" in passwd):
        print("You naughty little devil")
        main()
        return
    hashed = hash(passwd)
    print('Here is the encrypted password:', hashed)

    print('The original password, now decrypted:',unhash(hashed))

if __name__ =="__main__":
    main()

    

