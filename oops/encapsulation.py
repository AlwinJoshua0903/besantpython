#types of  encapsulation
#public:example-self.balance=balance
#private:self.__balance=balance
#protected:self._balance=balance
#private example
'''class encapsulation:
    def __init__(self,account_older,balance=0):
        self.account_older=account_older
        self.__balance=balance
    def etbalance(self):
        return self.__balance
    def amountdeposite(self,amount):
        if amount>0:
            self.__balance=amount
            print(f"desposited ${amount},newbalance ${self.__balance}")
        else:
            print(f"amount cannot be neative value")
    def witdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance=amount
            print(f"witraw ${amount},newbalance ${self.__balance}")
        else:
            print(f"insufficient balance")
account=encapsulation('alwin',3000)
print(account.account_older)
print(account.etbalance())
print(account.amountdeposite(500))
print(account.etbalance())
account.witdraw(100)
account.witdraw(1000)
print(account.etbalance())
account.witdraw(3500)'''

#protected example
class encapsulation:
    def __init__(self,account_older,balance=0):
        self._account_older=account_older
        self.__balance=balance
    def etbalance(self):
        return self.__balance
    def amountdeposite(self,amount):
        if amount>0:
            self.__balance=amount
            print(f"desposited ${amount},newbalance ${self.__balance}")
        else:
            print(f"amount cannot be neative value")
    def witdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance=amount
            print(f"witraw ${amount},newbalance ${self.__balance}")
        else:
            print(f"insufficient balance")
    def setaccountolder(self,new_accountolder):
        if new_accountolder:
            self._account_older=new_accountolder
            print(f"accountolder caned to {self._account_older}")
        else:
            print(f"invalid accountolder")
    def etaccountolder(self):
        return self._account_older

account=encapsulation('alwin',3000)