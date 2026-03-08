import tkinter as tk
from tkinter import ttk, filedialog
from finance_analysis import analyze_finances as analyze_financial_data
from ai_advisor import generate_financial_advice
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualization import show_expense_chart

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

# Create a container frame that will hold all pages
container = tk.Frame(window, bg="#f0f8ff")
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Dictionary to hold all frames
frames = {}

# ===== HOME PAGE FRAME =====
home_frame = tk.Frame(container, bg="#f0f8ff")
home_frame.grid(row=0, column=0, sticky="nsew")
frames['home'] = home_frame

# Home page content
home_title = tk.Label(home_frame, text="🏦 AI Financial Advisor", font=('Helvetica', 36, 'bold'), 
                      bg="#f0f8ff", fg="#2c3e50")
home_title.pack(pady=50)

home_subtitle = tk.Label(home_frame, text="Your Personal Financial Analysis Tool", font=('Helvetica', 16), 
                         bg="#f0f8ff", fg="#34495e")
home_subtitle.pack(pady=20)

home_description = tk.Label(home_frame, text="Analyze your finances, track expenses, and get\nintelligent financial advice powered by AI", 
                           font=('Helvetica', 12), bg="#f0f8ff", fg="#34495e", justify="center")
home_description.pack(pady=30)

def switch_to_main():
    frames['main'].tkraise()

start_button = tk.Button(home_frame, text="Start Now", command=switch_to_main, 
                        bg="#27ae60", fg="white", font=('Helvetica', 14, 'bold'), 
                        padx=40, pady=15, cursor="hand2")
start_button.pack(pady=40)

# ===== MAIN GUI FRAME =====
main_frame = tk.Frame(container, bg="#f0f8ff")
main_frame.grid(row=0, column=0, sticky="nsew")
frames['main'] = main_frame

# Back button at the top
back_button_frame = tk.Frame(main_frame, bg="#f0f8ff")
back_button_frame.pack(side="top", fill="x", padx=10, pady=5)

def go_back_home():
    frames['home'].tkraise()

back_button = tk.Button(back_button_frame, text="←", command=go_back_home, 
                        bg="#3498db", fg="white", font=('Helvetica', 10, 'bold'), padx=15, pady=5)
back_button.pack(side="left")

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

# Analyze Button # ... [keep existing imports and setup code unchanged until the analyze_finances function] ...
def analyze_finances():
    try:
        income = float(income_entry.get() or 0)
        savings = float(savings_entry.get() or 0)
        rent = float(rent_entry.get() or 0)
        food = float(food_entry.get() or 0)
        transport = float(transport_entry.get() or 0)
        shopping = float(shopping_entry.get() or 0)
        other = float(other_entry.get() or 0)

        total_expenses = rent + food + transport + shopping + other

    except ValueError:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "⚠️ Please enter valid numbers for all financial fields.")
        result_text.config(state="disabled")
        return

    summary = analyze_financial_data(income, total_expenses, savings)

    advice = generate_financial_advice(income, savings, rent, food, transport, shopping, other)

    show_expense_chart(rent, food, transport, shopping, other)

    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, "📊 FINANCIAL ANALYSIS\n", "header")
    result_text.insert(tk.END, "----------------------------\n")
    result_text.insert(tk.END, f"Balance: ₹{summary['balance']}\n")
    result_text.insert(tk.END, f"Savings: ₹{summary['savings']}\n")
    result_text.insert(tk.END, f"Savings Rate: {summary['savings_rate']:.2f}%\n")
    result_text.insert(tk.END, f"Expense Ratio: {summary['expense_ratio']:.2f}%\n\n")

    result_text.insert(tk.END, "💡 AI FINANCIAL ADVICE\n", "header")
    result_text.insert(tk.END, advice)

    result_text.config(state="disabled")

def clear_fields():
    income_entry.delete(0, tk.END)
    savings_entry.delete(0, tk.END)
    rent_entry.delete(0, tk.END)
    food_entry.delete(0, tk.END)
    transport_entry.delete(0, tk.END)
    shopping_entry.delete(0, tk.END)
    other_entry.delete(0, tk.END)
    cv_path.set("")
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.config(state="disabled")

analyze_button = tk.Button(input_frame, text="Analyze Finances", command=analyze_finances, bg="#27ae60", fg="white", font=('Helvetica', 11, 'bold'), padx=20, pady=10)
analyze_button.grid(row=4, column=0, columnspan=2, pady=20)

clear_button = tk.Button(input_frame, text="Clear", command=clear_fields, bg="#e74c3c", fg="white", font=('Helvetica', 11, 'bold'), padx=20, pady=10)
clear_button.grid(row=4, column=2, columnspan=2, pady=20)

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

# Show home page first
frames['home'].tkraise()

window.mainloop()
