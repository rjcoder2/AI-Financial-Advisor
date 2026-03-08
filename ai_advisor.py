def generate_financial_advice(income, savings, rent, food, transport, shopping, other):

    total_expenses = rent + food + transport + shopping + other
    balance = income - total_expenses
    savings_rate = (savings / income) * 100 if income > 0 else 0

    advice = "📊 FINANCIAL SUMMARY\n"
    advice += "----------------------------\n"
    advice += f"Monthly Income: ₹{income}\n"
    advice += f"Total Expenses: ₹{total_expenses}\n"
    advice += f"Remaining Balance: ₹{balance}\n"
    advice += f"Savings Rate: {savings_rate:.2f}%\n\n"

    advice += "💡 AI FINANCIAL GUIDANCE\n"
    advice += "----------------------------\n"

    # Savings advice
    if savings_rate < 20:
        advice += "⚠️ Your savings are below the recommended 20% of income.\n"
        advice += "Try setting aside more money for emergency savings.\n\n"
    else:
        advice += "✅ Great! Your savings rate is healthy.\n\n"

    # Expense ratio
    expense_ratio = (total_expenses / income) * 100 if income > 0 else 0

    if expense_ratio > 80:
        advice += "❌ Your expenses are extremely high compared to your income.\n"
        advice += "You should reduce spending immediately.\n\n"
    elif expense_ratio > 60:
        advice += "⚠️ Your expenses are moderately high.\n"
        advice += "Try optimizing unnecessary spending.\n\n"
    else:
        advice += "✅ Your spending level is within a healthy range.\n\n"

    # Category-specific suggestions
    if rent > income * 0.35:
        advice += "🏠 Rent is consuming a large portion of your income.\n"
        advice += "Consider cheaper housing options if possible.\n\n"

    if shopping > income * 0.15:
        advice += "🛍️ Shopping expenses are relatively high.\n"
        advice += "Try reducing impulse purchases.\n\n"

    if food > income * 0.20:
        advice += "🍔 Food spending is higher than recommended.\n"
        advice += "Cooking at home more often could help reduce costs.\n\n"

    # Balance suggestions
    if balance < 0:
        advice += "🚨 You are spending more than you earn.\n"
        advice += "Create a strict budget and reduce discretionary expenses.\n\n"
    else:
        advice += f"💰 You still have ₹{balance} remaining after expenses.\n\n"

    # Investment advice
    if balance > income * 0.20:
        advice += "📈 You have a good surplus. Consider investing in:\n"
        advice += "- Mutual Funds\n"
        advice += "- SIP investments\n"
        advice += "- Fixed deposits\n"
        advice += "- Emergency fund building\n"

    advice += "\n📌 Tip: Follow the 50-30-20 budgeting rule:\n"
    advice += "50% Needs | 30% Wants | 20% Savings\n"

    return advice
