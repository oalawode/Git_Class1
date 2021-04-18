class Category:
    def __init__(self, category_name, balance=0):
        self.name = category_name
        self.balance = balance


class BudgetApp:
    def __init__(self):
        self.budget_categories = {}

    def deposit(self, category_name, amount):
        budget_category = self.budget_categories.get(category_name)
        if not budget_category:
            budget_category = Category(category_name)
        budget_category.balance += amount
        self.budget_categories[category_name] = budget_category

    def withdraw(self, category_name, amount):
        budget_category = self.budget_categories.get(category_name)
        if budget_category is None:
            raise Exception("No budget has been set for this category")
        budget_category.balance -= amount
        self.budget_categories[category_name] = budget_category

    def balances(self):
        result = {}
        for name, cat in self.budget_categories.items():
            result[name] = cat.balance
        return result

    def transfer(self, amount, from_category, to_category):
        source_category = self.budget_categories[from_category]
        destination_category = self.budget_categories[to_category]
        if source_category.balance < amount:
            raise Exception(f"Insufficient funds in{source_category.name}")
        source_category.balance -= amount
        destination_category.balance += amount
        self.budget_categories[from_category] = source_category
        self.budget_categories[to_category] = destination_category


if __name__ == "__main__":
    app = BudgetApp()
    app.deposit("internet", 9000)
    assert app.balances() == {"internet": 9000}
    app.deposit("netflix", 4000)
    assert app.balances() == {"internet": 9000, "netflix": 4000}
    app.transfer(500, "internet", "netflix")
    assert app.balances() == {"internet": 8500, "netflix": 4500}
    app.deposit("internet", 1500)
    assert app.balances() == {"internet": 10000, "netflix": 4500}
