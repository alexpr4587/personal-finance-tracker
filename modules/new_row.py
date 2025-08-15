import pandas as pd

#agregar datos nuevos
def new_row():
    df = pd.read_csv('data\\expenses.csv')
    df2 = pd.read_csv('data\\income.csv')

    new_date = input("Enter a date (YYYY-MM-DD): ")

    income_or_expense = input("Enter 'income' or 'expense': ")

    if income_or_expense == 'expense':
        new_expense = float(input("Enter expense amount: "))
    else:
        new_income = float(input("Enter income amount: "))

    category = input("Enter category: ")

    description = input("Enter description: ")

    if income_or_expense == 'expense':
        df = pd.concat([df, pd.DataFrame({'Date': new_date, 'Type': 'Expense', 'Amount': new_expense, 'Category': category, 'Description': description}, index=[0])], ignore_index=True)
    else:
        df2 = pd.concat([df2, pd.DataFrame({'Date': new_date, 'Type': 'Income', 'Amount': new_income, 'Category': category, 'Description': description}, index=[0])], ignore_index=True)

    df.to_csv('data\\expenses.csv', index=False)
    df2.to_csv('data\\income.csv', index=False)

    print("New data added successfully!")
