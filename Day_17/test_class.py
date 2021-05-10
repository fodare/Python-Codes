class SimpleInterest:
    def __init__(self, p_amount, i_amount, r_amount):
        self.principal_amount = p_amount
        self.Interest = i_amount
        self.Rate_amount = r_amount

    def calculate_Simple_Interest(self):
        simple_interest = self.principal_amount * self.Interest * self.Rate_amount
        return print(f"Simple interest is: ${simple_interest}")


businees_1 = SimpleInterest(4500, 0.095, 6)
businees_1.calculate_Simple_Interest()