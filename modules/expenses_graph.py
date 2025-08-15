import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EXPENSES:
    df = pd.read_csv('data\\expenses.csv')
    df['cumulative_expense'] = df['Amount'].cumsum()

    sns.lineplot(data=df, x='Date', y='cumulative_expense', marker='o')

    plt.title('Total Monthly Expenses Overview')

    plt.show()