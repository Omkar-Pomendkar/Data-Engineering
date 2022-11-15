class Bank:
    def transaction(self,):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you Account opening Status")
    def deposit(self):
        print("this will show you deosited amount")
        # Here this is a multilevel Inheritance
    def test(self):
        print("This is test method from Bank")

class HDFC:
    def hdfc_to_icic(self):
        print("This will show you all the Transaction happen to icic from hdfc")

    def test(self):
        print("This is test method from hdfc bank")

class ICICI(Bank,HDFC):
    pass
i = ICICI()

i.transaction()
i.hdfc_to_icic()
i.account_opening()
i.deposit()
i.test()