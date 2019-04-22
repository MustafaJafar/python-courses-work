class Account :
    def __init__ (self , filepath) : 
        self.filepath = filepath
        with open(filepath , 'r') as file :
            #val = file.read() 
            #self.balance = 0 if val == "" else int(val)   #'Yes' if fruit == 'Apple' else 'No'
            try : 
                self.balance = int (file.read())
            except ValueError : 
                self.balance = 0

    def withdraw(self , ammount) :
        self.balance = self.balance - ammount 
    
    def deposit(self , ammount) :
        self.balance = self.balance + ammount 
    
    def commit (self):
         with open(self.filepath , 'w') as file :
            file.write(str(self.balance))

class Checking(Account) :
    """this class generates checking objects"""
    type = "checking" 
    def __init__ (self, filepath , fee ):
        Account.__init__(self , filepath)
        self.fee = fee 

    def transfer (self , amount) :
        self.balance = self.balance - amount - self.fee

'''
account = Account("balance.txt")
print (account.balance)
account.deposit(200)
account.commit()
print (account.balance)

Checking = Checking("balance.txt" , 5 )
Checking.transfer(100)
print (Checking.balance)
Checking.commit()
'''

jack_Checking = Checking("jack.txt" , 5 )
jack_Checking.transfer(100)
print (jack_Checking.balance)
jack_Checking.commit()
print(jack_Checking.type)

johns_Checking = Checking("johns.txt" , 5 )
johns_Checking.transfer(100)
print (johns_Checking.balance)
johns_Checking.commit()
print(johns_Checking.type)
print(johns_Checking.__doc__)