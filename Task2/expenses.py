
expenses = []



def add_expense(name, amount, category):

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)



def show_expenses():

    return expenses


def show_total():

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    return total



def update_expense(
    expense_number,
    new_name,
    new_amount,
    new_category
):

    if (
        expense_number >= 0
        and expense_number < len(expenses)
    ):

        expenses[expense_number]["name"] = new_name

        expenses[expense_number]["amount"] = new_amount

        expenses[expense_number]["category"] = new_category

        return True

    else:

        return False


def delete_expense(expense_number):

    if (
        expense_number >= 0
        and expense_number < len(expenses)
    ):

        deleted_expense = expenses.pop(expense_number)

        return deleted_expense

    else:

        return None
