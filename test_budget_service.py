import unittest
from datetime import datetime
from budget_service import BudgetService
from budget_repo import BudgetRepo, Budget

# class FakeRepo(BudgetRepo):
#     def get_all(self) -> list:



class TestBudgetService(unittest.TestCase):
    def test_partial_month(self):
        # def fake_get_all():
        #     return [Budget("202306", 3000)]

        repo = BudgetRepo(
            [Budget("202306", 3000)]
        )
        budget_service = BudgetService(repo)
        budget = budget_service.query(datetime(2023,6,1), datetime(2023,6,2))
        self.assertEqual(budget, 200)  # add assertion here

    def test_whole_month(self):
        # def fake_get_all():
        #     return [Budget("202306", 3000)]

        repo = BudgetRepo(
            [Budget("202306", 3000)]
        )
        budget_service = BudgetService(repo)
        budget = budget_service.query(datetime(2023,6,1), datetime(2023,6,30))
        self.assertEqual(budget, 3000)  # add assertion here

    def test_invalid_month(self):
        repo = BudgetRepo(
            [Budget("202306", 3000)]
        )
        budget_service = BudgetService(repo)
        budget = budget_service.query(datetime(2023, 6, 2), datetime(2023, 6, 1))
        self.assertEqual(budget, 0)  # add assertion here

    def test_cross_month(self):
        repo = BudgetRepo(
            [Budget("202306", 3000),
             Budget("202307", 31),
             Budget("202308", 310)
             ]
        )
        budget_service = BudgetService(repo)
        budget = budget_service.query(datetime(2023, 6, 29), datetime(2023, 8, 1))
        self.assertEqual(budget, 200+31+10)  # add assertion here

    def test_cross_five_month(self):
        repo = BudgetRepo(
            [Budget("202306", 3000),
             Budget("202307", 31),
             Budget("202308", 310),
             Budget("202305", 31),
             Budget("202309", 30)
             ]
        )
        budget_service = BudgetService(repo)
        budget = budget_service.query(datetime(2023, 5, 31), datetime(2023, 8, 1))
        self.assertEqual(budget, 1+3000+31+10)  # add assertion here

    def test_no_data(self):
        repo = BudgetRepo([])
        budget_service = BudgetService(repo)
        budget = budget_service.query(datetime(2022, 6, 2), datetime(2022, 6, 1))
        self.assertEqual(budget, 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
