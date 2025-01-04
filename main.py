import time
import random
import string as str




values = list(str.ascii_lowercase + str.ascii_uppercase + str.digits + str.punctuation+" " )


l_key = list(str.ascii_lowercase + str.ascii_uppercase + str.digits + str.punctuation+' ' )
random.shuffle(l_key)
key = ''.join(l_key)

access = False

def encrpyt():
    global x,new
    e_key = key
    new = []
    F1 = open('base.txt','r')
    x= F1.read()
    for i in x:
    
        pos = int(values.index(i))
        n_pos = e_key[pos]
        new.append(n_pos)
        text = ''.join(new)
    print(key)
    F1.close()
    F2 = open('encrypted.txt','w')
    F2.write(text)
    F2.close()
   

def decrypt():
    global y,new1

    new1 = []
    
    F2 = open('encrypted.txt','r')
    y = F2.read()
    print(y)
    for i in y:
        pos = int(key.index(i))
        n_pos = values[pos]
        new1.append(n_pos)
        text = ''.join(new1)  
        
    F3 = open('decrypted.txt','w')
    F3.write(text)
    F3.close()

def passw():
    global passw,access

    count = 3 
    word = '0000'
    
    for i in range(0,3):
        password = input("Enter your password: ")
        if password == word:
            print("access granted")
            access = True 
            
            break
        else:
            count -= 1
            print("wrong password, try again")
            print(count," tries left")
            
passw()
if access == True:

    print('''choose one of the following options:
          1. decrypt(requires the key)
          2. encrypt''')
    choice = input("Enter your choice: ")
    if choice == '1':
        key = list(input('enter the key here : '))
        decrypt()
    elif choice == '2':
        encrpyt()
        
