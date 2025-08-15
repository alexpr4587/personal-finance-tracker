import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class INCOME:
    df = pd.read_csv('data\\income.csv')
    df['cumulative_income'] = df['Amount'].cumsum()

    sns.lineplot(data=df, x='Date', y='cumulative_income', marker='o')

    plt.title('Total Monthly Income Overview')

    plt.show()