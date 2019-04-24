class Account:
    def __init__(self,first_name,second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0.00
        
        
    def greetings(self):
            return"Hello {} {} welcome to the your banking account you balance is{}".format(self.first_name,self.second_name,self.balance)

    def deposit(self,a):
        self.balance=self.balance+a
        return("you have deposited {}".format(a))

    def withdraw(self,b):
        if b < self.balance:
            self.balance=self.balance-b
       
            return("Hello {} {} you have successfully withdrawn  {}".format(self.first_name,self.second_name,b))
        else:
            return("Hello {} {} you have insufficient balance".format(self.first_name,self.second_name,b))