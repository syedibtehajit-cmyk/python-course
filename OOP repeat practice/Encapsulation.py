class bankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,deposit):
     if deposit >= 0:
         self.__balance+=deposit
     else:
        print("Invalid amount")

    def withdrawal(self,withdrawal):
       if withdrawal > 0 and withdrawal <= self.__balance:
         self.__balance -=withdrawal
       else:
           print("insufficent balance")
    
    def show_balance(self):
        print("your balance is",self.__balance)
        
        
bank1=bankAccount(5000)
bank1.deposit(0)
bank1.withdrawal(0)
bank1.show_balance()