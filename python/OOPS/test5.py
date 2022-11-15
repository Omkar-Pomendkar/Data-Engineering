class Bank:
    def transaction(self,):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you Account opening Status")
    def deposit(self):
        print("this will show you deosited amount")
        # Here this is a multilevel Inheritance

class HDFC(Bank):
    def hdfc_to_icic(self):
        print("This will show you all the Transaction happen to icic from hdfc")

class ICICI (HDFC):
    pass

ic = ICICI()
ic.hdfc_to_icic()
ic.deposit()
ic.account_opening()
ic.transaction()
