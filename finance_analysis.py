# finance_analysis.py
"""
Activity 2.1: Financial Data Analysis
Module to analyze user's financial data and provide tips.
"""

import matplotlib.pyplot as plt
from ai_advisor import generate_financial_advice

def analyze_finances(income, expenses, savings, rent, food, transport, shopping, other):
    """
    Detailed analysis of finances.
    Parameters:
        income (float): monthly income
        expenses (float): monthly expenses
        savings (float): current savings
        rent (float): monthly rent expense
        food (float): monthly food expense
        transport (float): monthly transport expense
        shopping (float): monthly shopping expense
        other (float): other monthly expenses
    Returns:
        dict: financial summary, ratios, tips, and advice
    """
    balance = income - expenses
    tips = []

    # --- Basic Analysis ---
    if balance > 0:
        tips.append("✅ You are saving money this month.")
    else:
        tips.append("⚠️ Your expenses exceed your income. Consider reducing spending.")

    if savings < income * 0.2:
        tips.append("💡 Try to save at least 20% of your income monthly.")

    if expenses > income * 0.7:
        tips.append("⚠️ Your spending is high. Track unnecessary expenses.")

    # --- Advanced Analysis ---
    savings_rate = (savings / income) * 100 if income > 0 else 0
    expense_ratio = (expenses / income) * 100 if income > 0 else 0
    emergency_fund_needed = expenses * 3  # 3 months of expenses as emergency fund
    emergency_fund_status = savings - emergency_fund_needed

    if savings_rate >= 20:
        tips.append(f"✅ Your savings rate is good ({savings_rate:.1f}%). Keep it up!")
    else:
        tips.append(f"💡 Savings rate is {savings_rate:.1f}%. Aim for at least 20%.")

    if expense_ratio <= 70:
        tips.append(f"✅ Your expense ratio is healthy ({expense_ratio:.1f}%).")
    else:
        tips.append(f"⚠️ Expense ratio is high ({expense_ratio:.1f}%). Consider cutting non-essential spending.")

    if emergency_fund_status >= 0:
        tips.append("✅ You have enough emergency fund (3 months of expenses).")
    else:
        tips.append(f"⚠️ You need an additional ${-emergency_fund_status:.2f} for a 3-month emergency fund.")

    # --- Visualization ---
    show_expense_chart(rent, food, transport, shopping, other)

    # --- AI-Generated Advice ---
    advice = generate_financial_advice(income, savings, rent, food, transport, shopping, other)

    return {
        "balance": balance,
        "savings": savings,
        "savings_rate": savings_rate,
        "expense_ratio": expense_ratio,
        "emergency_fund_needed": emergency_fund_needed,
        "emergency_fund_status": emergency_fund_status,
        "tips": tips,
        "advice": advice
    }

def show_expense_chart(rent, food, transport, shopping, other):
    """
    Display a pie chart of expense distribution.
    Parameters:
        rent (float): monthly rent expense
        food (float): monthly food expense
        transport (float): monthly transport expense
        shopping (float): monthly shopping expense
        other (float): other monthly expenses
    """
    categories = ['Rent', 'Food', 'Transport', 'Shopping', 'Other']
    values = [rent, food, transport, shopping, other]

    plt.figure(figsize=(6, 6))
    plt.pie(
        values,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title("Monthly Expense Distribution")
    plt.show()

# --- Test the module ---
if __name__ == "__main__":
    test_data = analyze_finances(income=2000, expenses=1500, savings=300, rent=500, food=300, transport=200, shopping=100, other=400)
    print("Financial Summary:", test_data)
