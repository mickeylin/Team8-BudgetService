class BudgetRepo:
    def __init__(self, all_budget):
        self.data = all_budget
    def get_all(self) -> list:
        return self.data


class Budget:
    def __init__(self, year_month: str, amount: int):
        self.year_month = year_month
        self.amount = amount

    def get_yearmonth(self):
        return self.year_month

    def get_amount(self):
        return self.amount
