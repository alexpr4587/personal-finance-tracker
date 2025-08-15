import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from modules.new_row import new_row

while True:
    select_action = input("Select action (add/view/exit): ")
    if select_action == "add":
        new_row()
    elif select_action == "view":
        def EXPENSES():
            from modules.expenses_graph import EXPENSES
            EXPENSES()
        def INCOME():
            from modules.income_graph import INCOME
            INCOME()
        EXPENSES()
        INCOME()
    elif select_action == "exit":
        break
    else:
        print("Invalid action. Please try again.")