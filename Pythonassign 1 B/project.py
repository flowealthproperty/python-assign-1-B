def calculate_total_monthly_expenses(loan_payment, insurance, gas, maintenance):
    total_monthly_expenses = loan_payment + insurance + gas + maintenance
    return total_monthly_expenses

def calculate_total_annual_expenses(total_monthly_expenses):
    total_annual_expenses = total_monthly_expenses * 12
    return total_annual_expenses

def main():
    try:
        loan_payment = float(input("Enter monthly loan payment for your automobile: "))
        insurance = float(input("Enter monthly insurance cost for your automobile: "))
        gas = float(input("Enter monthly gas expenses for your automobile: "))
        maintenance = float(input("Enter monthly maintenance expenses for your automobile: "))

        total_monthly_expenses = calculate_total_monthly_expenses(loan_payment, insurance, gas, maintenance)
        total_annual_expenses = calculate_total_annual_expenses(total_monthly_expenses)

        print("\nTotal Monthly Expenses:")
        print(f"Loan Payment: ${loan_payment:.2f}")
        print(f"Insurance: ${insurance:.2f}")
        print(f"Gas: ${gas:.2f}")
        print(f"Maintenance: ${maintenance:.2f}")
        print(f"\nTotal Monthly Expenses: ${total_monthly_expenses:.2f}")
        print(f"Total Annual Expenses: ${total_annual_expenses:.2f}")

    except ValueError:
        print("Please enter valid numeric values for expenses.")

if __name__ == "__main__":
    main()
