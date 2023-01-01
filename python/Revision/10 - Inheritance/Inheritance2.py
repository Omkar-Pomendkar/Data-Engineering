class bank:

    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you your Account open Status")
    def deposit(self):
        print("This will show your Diposited Amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("This show all the transaction happend from hdfc to icic bank")

class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.deposit()