import matplotlib.pyplot as plt

def show_expense_chart(rent, food, transport, shopping, other):

    categories = ['Rent', 'Food', 'Transport', 'Shopping', 'Other']
    values = [rent, food, transport, shopping, other]

    plt.figure(figsize=(6,6))

    plt.pie(
        values,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140
    )

    plt.title("Monthly Expense Distribution")

    plt.show()
