available = 2500.00
budgets = {}
expenditure = {}
{"Groceries" : 500, "Bills" : 200, "Entertainment" : 50}
def add_budget(name, amount):
    global available
    if name in budgets:
        raise ValueError("Budget exists")
        if amount > available:
            raise ValueError("Insufficient funds")
    budgets[name] = amount
    avaiable -= amountexpenditure[name] = 0
    return available
    def spend(name, amount):
        if name not in expenditure:
            raise ValueError("No such budget")
            expenditure[name] += amount
            budgeted = budgets[name]
            spent = expediture[name]
            return budgeted - spent
            def print_summary():
                for name in budgets:
                    budgeted = budgets[name]
                    spent = expenditure[name]
                    remaining = budgeted - spent
                    print(f'{name:15s} {budgeted:10.2f} {spent:10.2f}'
                    f'{remaing:10.2f}')
                    print(name, budgeted, spent, remaing)