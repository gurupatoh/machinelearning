# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:07:05 2020

@author: GURUH
"""

class creditCard:
    """ A customer credit card """
    def __init__(self,customer,bank,account,limit):
           self._customer =customer
           self._bank=bank
           self._account=account
           self._limit= limit
           self._balance=0
           
        
           """ create a new credit card instace
        The initial balance is zero
        customer The customer name is ('patrick ngigi")
        bank The bank name is ('Ecobank kenya')
        account The account identifier is ('123456789')
        limit The credit limit(measured in kenya shillings)
        """
             
    def get_customer(self):
        """ return the name of the customer"""
        return self._customer
    def get_bank(self):
        """return name of the bank """
        return self._bank
    def get_account(self):
        """ return the account identifier(typically stored as a string)"""
        return self._account
    def get_limit(self):
        """return the cards limit in ksh"""
        return self._limit
    def get_balance(self):
        """return bank acccount balance"""
        return self._balance
    def charge(self,price):
        """charge f=given to the price card assuming sufficient limit,
        return true if the charge was processed and false if denied
        """
        if price +self._balance > self._limit:
            
            return False
        else:
            self._balance+=price
            return True
    def make_payment(self,amount):
        """process cuustomer balance that reduce balance"""
        self._balance-=amount
        
if __name__=='__main__':
    
    wallet=[]
    wallet.append(creditCard('patrick ngigi','ecobank savings','123456789',2500))
    wallet.append(creditCard('patrick ngigi','ecobank federal','123456789',3500))
    wallet.append(creditCard('patrick ngigi','ecobank insurance','7777777',5000))

for val in range(1,17):
    wallet[0].charge(val)
    wallet[1].charge(val*2)
    wallet[2].charge(val*3)
    for c in range(3):
        print('customer=',wallet[c].get_customer())
        print('bank=',wallet[c].get_bank())
        print('account=',wallet[c].get_account())
        print('limit',wallet[c].get_limit())
        print('balance=',wallet[c].get_balance())
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(5000)
        print('New balance:',wallet[c].get_balance())
        print()
        
    
    




        
        
        
        
        
       
       
        
        
    