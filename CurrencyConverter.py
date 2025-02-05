import tkinter as tk
from tkinter import messagebox

class CurrencyConverterApp:
    def __init__(self, root):
        root.title("Currency Converter App")
        root.geometry("400x400")
        root.resizable(False, False)

        root.configure(bg="#f0f0f0")

        container = tk.Frame(root, bg="#f0f0f0")
        container.grid(sticky="nsew", padx=20, pady=20)

        container.columnconfigure(0, weight=1)

        tk.Label(container, text="Currency Converter App", font=("Arial", 24, "bold"), bg="#f0f0f0").grid(row=0, column=0, pady=10)

        tk.Label(container, text="Enter Amount (e.g., 100):", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, pady=5, sticky="w")
        self.amount_entry = tk.Entry(container, font=("Arial", 12))
        self.amount_entry.grid(row=2, column=0, padx=10, sticky="ew")

        tk.Label(container, text="From Currency (e.g., USD):", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, pady=5, sticky="w")
        self.from_currency_entry = tk.Entry(container, font=("Arial", 12))
        self.from_currency_entry.grid(row=4, column=0, padx=10, sticky="ew")

        tk.Label(container, text="To Currency (e.g., INR):", font=("Arial", 12), bg="#f0f0f0").grid(row=5, column=0, pady=5, sticky="w")
        self.to_currency_entry = tk.Entry(container, font=("Arial", 12))
        self.to_currency_entry.grid(row=6, column=0, padx=10, sticky="ew")

        tk.Button(container, text="Convert", command=self.convert_currency, font=("Arial", 14), bg="#4CAF50", fg="white").grid(row=7, column=0, pady=15, sticky="ew")

        self.result_label = tk.Label(container, text="", font=("Arial", 16, "bold"), bg="#d1ffd1", fg="#333", relief="sunken", padx=10, pady=10)
        self.result_label.grid(row=8, column=0, pady=10, sticky="ew")

        container.grid_columnconfigure(0, weight=1)

    def get_exchange_rate(self, from_currency, to_currency):
        exchange_rates = {
            "USD": {"INR": 82.50, "EUR": 0.92, "GBP": 0.75},
            "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.009},
            "EUR": {"USD": 1.09, "INR": 89.74, "GBP": 0.82},
            "GBP": {"USD": 1.33, "INR": 100.20, "EUR": 1.22}
        }

        rates = exchange_rates.get(from_currency, {})
        return rates.get(to_currency)

    def convert_currency(self):
        from_currency = self.from_currency_entry.get().upper().strip()
        to_currency = self.to_currency_entry.get().upper().strip()
        amount = self.amount_entry.get().strip()

        if not from_currency or not to_currency or not amount:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
            return

        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate:
            converted_amount = amount * rate
            result_text = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
            self.result_label.config(text=result_text)
        else:
            messagebox.showerror("Conversion Error", "Unable to perform currency conversion.")

if __name__ == "__main__":
    root = tk.Tk()
    CurrencyConverterApp(root)
    root.mainloop()