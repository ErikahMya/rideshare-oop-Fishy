
class PassengerAccount:
    def __init__(self, name):
        self.name = name
        self.__wallet_balance = 0.0

    def top_up_wallet(self, amount):
        # Prevent negative amounts
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        # top up money to the wallet
        self.__wallet_balance += amount
        print(f"Wallet balance: ₱{self.__wallet_balance:.2f}")

    def pay_for_ride(self, fare_amount):
        # Check if the balance is enough
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")

        # Deduct the fare
        self.__wallet_balance -= fare_amount
        print(f"Payment successful! Remaining balance: ₱{self.__wallet_balance:.2f}")

