#SECURE MESSAGE ENCRYPTION SYSTEM
import pickle 
filename="Login.dat"
file="Encrypt.dat"
new="Secret.dat"

def User_Registeration():
    data=[]
    Create_PIN=int(input("Enter your PIN number:"))
    Confirm_PIN=int(input("Enter your PIN number to confirm:"))
    if Create_PIN==Confirm_PIN:
        with open (filename,"rb+")as f:
            try:
                data=pickle.load(f)
                if Create_PIN in data:
                    print("PIN is already taken!")
                else:
                    data.append(Confirm_PIN)
                    f.seek(0)
                    pickle.dump(data,f)
                    f.truncate()
                    print("PIN created successfully!")
            except EOFError:
                data=[Confirm_PIN]
                pickle.dump(data,f)
                print("PIN created successfully!")
    else:
        print("Try again!")
   

def Login():
    L=[]
    Try=3
    with open(filename,"rb")as f:
        try:
            data=pickle.load(f)
            for k in data:
                L.append(k)
            Login_Successful=False
            for i in range(Try):
                User=int(input("Enter your PIN:"))
                for j in L:
                    
                    if j==User:
                        Login_Successful=True
                        print("Login successful!")
                        ch="yes"
                        while ch.lower() in ["yes","y"]:
                            print("---SECURE MESSAGE SYSTEM FUNCTIONS---")
                            print("1. Encrypt Message")
                            print("2. Decrypt Message")
                            print("3. View Encrypted Message")
                            print("4. Exit")
                            choice=int(input("Enter your choice number:"))
                            if choice==1:
                                Encrypt()
                            elif choice==2:
                                Decrypt()
                            elif choice==3:
                                View_Encrypted_Messages()
                            elif choice==4:
                                print("Thank for using our encryption system!")
                                break
                            else:
                                print("Invalid choice entered!")
                            ch=input("Do you want to continue(yes/no):")
                    if Login_Successful:
                        break
            else:
                print("Access denied!")      
            
        except EOFError:
            pass


def Encrypt():
    List=[]
    Data=""
    Secret=[]
    User=input("Enter your message:")
    for i in User:
        Encrypt=chr(ord(i)+3)
        Data+=Encrypt
    List.append(Data)
    with open (file,"ab") as f1:
        pickle.dump(List,f1)
    Secret_key=input("Enter your secret key:")
    Secret.append(Secret_key)
    with open(new,"ab")as f2:
        pickle.dump(Secret,f2)
    print("Your encrypted message:",Data)

def Decrypt():
    Secret_key = input("Enter your secret key:")
    Data = ""
    found = False

    try:
        with open(new, "rb") as f1:

            while True:
                try:
                    secret = pickle.load(f1)

                    for i in secret:
                        if i == Secret_key:
                            found = True
                            break

                    if found:
                        break

                except EOFError:
                    break

            if found:
                Encrypt = input("Enter your encrypted message:")

                for j in Encrypt:
                    Decrypt = chr(ord(j) - 3)
                    Data += Decrypt

                print("Original message is:", Data)

            else:
                print("Incorrect key! Message cannot be decrypted")

    except FileNotFoundError:
        print("No secret keys found!")

def View_Encrypted_Messages():
    L = []
    with open(file, "rb") as f1:
        while True:
            try:
                Data = pickle.load(f1)
                for i in Data:
                    L.append(i)
            except EOFError:
                break

    print("The encrypted messages are:", L)
       
    
        

ch="yes"
while ch.lower() in ["yes","y"]:
    print("---SECURE MESSAGE SYSTEM---")
    print("1. User Registeration")
    print("2. Login")
    print("3. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        User_Registeration()
    elif choice==2:
        Login()
    elif choice==3:
        print("Thank for using our encryption system!")
        break
    else:
        print("Invalid choice!")
    ch=input("Do you want to continue(yes/no):")
        
        
                
    
                    
        
            
            
            
        

    
    
        
    
