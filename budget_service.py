from datetime import datetime, date
from budget_repo import BudgetRepo
import calendar


class BudgetService:

    def __init__(self, repo: BudgetRepo) -> None:
        super().__init__()
        self.repo = repo

    def query(self, start: datetime, end: datetime) -> float:
        all_budget = self.repo.get_all()
        start_year_month = start.strftime("%Y%m")
        end_year_month = end.strftime("%Y%m")
        total = 0

        if self.is_invalid(start, end):
            return 0

        for budget_item in all_budget:
            if budget_item.get_yearmonth() == start_year_month:
                if start_year_month == end_year_month:
                    days_of_mon = calendar.monthrange(start.year, start.month)[1]
                    shift_day = end.day - start.day + 1
                    one_day_budget = budget_item.get_amount()/days_of_mon
                    total += shift_day * one_day_budget
                    return total

                else:
                    days_of_mon = calendar.monthrange(start.year, start.month)[1]
                    shift_day = days_of_mon - start.day + 1
                    one_day_budget = budget_item.get_amount() / days_of_mon
                    total += shift_day * one_day_budget

            elif budget_item.get_yearmonth() == end_year_month:
                days_of_mon = calendar.monthrange(end.year, end.month)[1]
                one_day_budget = budget_item.get_amount() / days_of_mon
                total += end.day * one_day_budget

            elif start_year_month < budget_item.get_yearmonth() < end_year_month:
                total += budget_item.get_amount()

        return total

    def is_invalid(self, start, end):
        if start > end:
            return 0

