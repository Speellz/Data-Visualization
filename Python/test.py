import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Test
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [15000, 18000, 17000, 16000, 21000, 22000, 19000, 23000, 20000, 25000, 24000, 26000],
    'Expenses': [5000, 6000, 5500, 7000, 7500, 8000, 6500, 8500, 7000, 9000, 8500, 9000]
}
df = pd.DataFrame(data)
df['Profit'] = df['Revenue'] - df['Expenses']

def create_charts():
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))

    # Revenue
    sns.lineplot(ax=axes[0, 0], x='Month', y='Revenue', data=df, marker='o')
    axes[0, 0].set_title('Monthly Revenue')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Revenue')

    # Expenses
    sns.lineplot(ax=axes[0, 1], x='Month', y='Expenses', data=df, marker='o', color='r')
    axes[0, 1].set_title('Monthly Expenses')
    axes[0, 1].set_xlabel('Month')
    axes[0, 1].set_ylabel('Expenses')

    # Profit
    sns.lineplot(ax=axes[1, 0], x='Month', y='Profit', data=df, marker='o', color='g')
    axes[1, 0].set_title('Monthly Profit')
    axes[1, 0].set_xlabel('Month')
    axes[1, 0].set_ylabel('Profit')

    # Overview
    sns.lineplot(ax=axes[1, 1], x='Month', y='Revenue', data=df, marker='o', label='Revenue')
    sns.lineplot(ax=axes[1, 1], x='Month', y='Expenses', data=df, marker='o', color='r', label='Expenses')
    sns.lineplot(ax=axes[1, 1], x='Month', y='Profit', data=df, marker='o', color='g', label='Profit')
    axes[1, 1].set_title('Monthly Financial Overview')
    axes[1, 1].set_xlabel('Month')
    axes[1, 1].set_ylabel('Amount')
    axes[1, 1].legend()

    # Correlation matrix
    correlation_matrix = df[['Revenue', 'Expenses', 'Profit']].corr()
    sns.heatmap(ax=axes[2, 0], data=correlation_matrix, annot=True, cmap="coolwarm")
    axes[2, 0].set_title("Correlation Matrix")

    fig.delaxes(axes[2, 1])

    plt.tight_layout()
    return fig

# Tkinter
root = Tk()
root.title("Financial Data Analysis")

fig = create_charts()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()
