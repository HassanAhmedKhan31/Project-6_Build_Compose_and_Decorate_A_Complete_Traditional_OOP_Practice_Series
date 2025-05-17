class Bank:
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
b1 = Bank()
print("Before:", b1.bank_name)
Bank.change_bank_name("UBL")
print("After:", b1.bank_name)
