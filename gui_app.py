import tkinter as tk
from tkinter import ttk, filedialog
from finance_analysis import analyze_finances  # your updated module

# Create main window
window = tk.Tk()
window.title("AI Financial Advisor System")
window.geometry("1000x800")
window.configure(bg="#f0f8ff")  # Light blue background

# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Helvetica', 10), background="#f0f8ff")
style.configure('TButton', font=('Helvetica', 10, 'bold'))
style.configure('TEntry', font=('Helvetica', 10))

# --- Main frame ---
main_frame = tk.Frame(window, bg="#f0f8ff")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# --- Top frame for input ---
input_frame = tk.LabelFrame(main_frame, text="💰 Financial Data Input", font=('Helvetica', 12, 'bold'), bg="#e6f3ff", fg="#2c3e50", padx=10, pady=10)
input_frame.pack(side="top", anchor="center", pady=10)

# Income and Savings
income_label = ttk.Label(input_frame, text="Monthly Income ($):", foreground="#34495e")
income_label.grid(row=0, column=0, sticky="w", pady=5)
income_entry = ttk.Entry(input_frame, width=20)
income_entry.grid(row=0, column=1, pady=5, padx=5)

savings_label = ttk.Label(input_frame, text="Current Savings ($):", foreground="#34495e")
savings_label.grid(row=0, column=2, sticky="w", pady=5)
savings_entry = ttk.Entry(input_frame, width=20)
savings_entry.grid(row=0, column=3, pady=5, padx=5)

# Expenses Breakdown
expenses_frame = tk.LabelFrame(input_frame, text="Monthly Expenses ($)", font=('Helvetica', 11, 'bold'), bg="#e6f3ff", fg="#2c3e50")
expenses_frame.grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

rent_label = ttk.Label(expenses_frame, text="Rent:", foreground="#34495e")
rent_label.grid(row=0, column=0, sticky="w", pady=2)
rent_entry = ttk.Entry(expenses_frame, width=20)
rent_entry.grid(row=0, column=1, pady=2, padx=5)

food_label = ttk.Label(expenses_frame, text="Food:", foreground="#34495e")
food_label.grid(row=1, column=0, sticky="w", pady=2)
food_entry = ttk.Entry(expenses_frame, width=20)
food_entry.grid(row=1, column=1, pady=2, padx=5)

transport_label = ttk.Label(expenses_frame, text="Transportation:", foreground="#34495e")
transport_label.grid(row=2, column=0, sticky="w", pady=2)
transport_entry = ttk.Entry(expenses_frame, width=20)
transport_entry.grid(row=2, column=1, pady=2, padx=5)

shopping_label = ttk.Label(expenses_frame, text="Shopping:", foreground="#34495e")
shopping_label.grid(row=3, column=0, sticky="w", pady=2)
shopping_entry = ttk.Entry(expenses_frame, width=20)
shopping_entry.grid(row=3, column=1, pady=2, padx=5)

other_label = ttk.Label(expenses_frame, text="Other Expenses:", foreground="#34495e")
other_label.grid(row=4, column=0, sticky="w", pady=2)
other_entry = ttk.Entry(expenses_frame, width=20)
other_entry.grid(row=4, column=1, pady=2, padx=5)

# CV Upload
cv_label = ttk.Label(input_frame, text="📄 Upload CV (Optional):", foreground="#34495e")
cv_label.grid(row=2, column=0, sticky="w", pady=(10,0))
cv_path = tk.StringVar()
cv_entry = ttk.Entry(input_frame, textvariable=cv_path, width=40)
cv_entry.grid(row=3, column=0, columnspan=3, pady=3, sticky="ew")

def browse_cv():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
    cv_path.set(file)

browse_button = ttk.Button(input_frame, text="Browse", command=browse_cv)
browse_button.grid(row=3, column=3, pady=3, padx=5)

# Analyze Button
def analyze_button_click():
    try:
        income = float(income_entry.get() or 0)
        savings = float(savings_entry.get() or 0)
        expenses = float(rent_entry.get() or 0) + float(food_entry.get() or 0) \
                   + float(transport_entry.get() or 0) + float(shopping_entry.get() or 0) \
                   + float(other_entry.get() or 0)
    except ValueError:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "⚠️ Please enter valid numbers for all financial fields.")
        result_text.config(state="disabled")
        return

    summary = analyze_finances(income, expenses, savings)

    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "💼 Financial Summary:\n\n", "header")
    result_text.insert(tk.END, f"Balance: ${summary['balance']}\n")
    result_text.insert(tk.END, f"Savings: ${summary['savings']}\n")
    if 'savings_rate' in summary:
        result_text.insert(tk.END, f"Savings Rate: {summary['savings_rate']:.2f}%\n")
    if 'expense_ratio' in summary:
        result_text.insert(tk.END, f"Expense Ratio: {summary['expense_ratio']:.2f}%\n")
    if 'emergency_fund_needed' in summary:
        result_text.insert(tk.END, f"Emergency Fund Needed: ${summary['emergency_fund_needed']}\n")
    if 'emergency_fund_status' in summary:
        result_text.insert(tk.END, f"Emergency Fund Status: ${summary['emergency_fund_status']}\n")
    result_text.insert(tk.END, "\n💡 Tips:\n\n", "header")
    for tip in summary["tips"]:
        result_text.insert(tk.END, f"• {tip}\n")
    result_text.config(state="disabled")

analyze_button = tk.Button(input_frame, text="Analyze Finances", command=analyze_button_click, bg="#27ae60", fg="white", font=('Helvetica', 11, 'bold'), padx=20, pady=10)
analyze_button.grid(row=4, column=0, columnspan=4, pady=20)

# --- Bottom frame for results ---
result_frame = tk.LabelFrame(main_frame, text="📊 Analysis Results", font=('Helvetica', 12, 'bold'), bg="#e6f3ff", fg="#2c3e50", padx=10, pady=10)
result_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

# Result display with scrollbars
result_text = tk.Text(result_frame, width=80, height=20, state="disabled", bg="#ffffff", fg="#2c3e50", font=('Helvetica', 10), wrap="none")
v_scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
h_scrollbar = ttk.Scrollbar(result_frame, orient="horizontal", command=result_text.xview)
result_text.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
result_text.pack(side="left", fill="both", expand=True)
v_scrollbar.pack(side="right", fill="y")
h_scrollbar.pack(side="bottom", fill="x")

# Configure tags for styling text
result_text.tag_configure("header", font=('Helvetica', 11, 'bold'), foreground="#27ae60")

window.mainloop()
