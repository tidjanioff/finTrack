from simple_colors import *
from datetime import date
from months import give_month, give_month_number
import sys
import csv
from tabulate import tabulate

current_month = give_month(int(str(date.today()).split('-')[1]))
valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                "October", "November", "December"]
income_headers = ["Source", "Amount", "Category", "Depository", "Date"]
expenses_headers = ["Source", "Amount", "Category", "Payment Method", "Date"]


def main():
    welcome()
    while True:
        try:
            users_option = int(input("$ "))
            if users_option in valid_options(1):
                break
            error_message(1)
        except ValueError:
            error_message(1)
    if users_option == 0:
        end_program()
    elif users_option == 3:
        month_summary(current_month, 1)
    elif users_option == 4:
        month_option = month_prompt()
        month_summary(month_option, 2)
    elif users_option == 5:
        year_summary()
    elif users_option == 6:
        users_option2 = inc_or_exp_prompt()
        if users_option2 == 1:
            print_table(current_month, "income")
        elif users_option2 == 2:
            print_table(current_month, "expenses")
    elif users_option == 7:
        month_option = month_prompt()
        users_option2 = inc_or_exp_prompt()
        if users_option2 == 1:
            print_table(month_option,"income")
        elif users_option2 == 2:
            print_table(month_option, "expenses")
    elif users_option == 1:
        new_income()
    elif users_option == 2:
        new_expense()


def welcome():
    print("", f"This is {special('© FinTrack', 'cyan')}",
          "We help you keep an eye on your finances.", "",
          f"Current month : {current_month}",
          "", f"{special('Summary options :', 'magenta')}",
          f"→ Tap 3 to display a summary of your {current_month}'s finances (Income, Expenses, Balance)",
          "→ Tap 4 to display a summary of any month's finances (Income, Expenses)",
          "→ Tap 5 to display a summary of this year's finances", "",
          f"{special('Details options :', 'magenta')}",
          f"→ Tap 6 to get access to the details of your {current_month}'s finances (Income, Expenses)",
          "→ Tap 7 to get access to the details of any month's finances (Income, Expenses)", "",
          f"{special('Tools :', 'magenta')}",
          "→ Tap 1 to add a new income",
          "→ Tap 2 to add a new expense",
          "→ Tap 0 to end the program","",
          f"{special('2024 © FinTrack | Built by Tidjani. All rights reserved.', 'cyan')}", "", sep='\n')


def month(a_date):
    return give_month(int(a_date.split('-')[1]))


# if user want to end the program
def end_program():
    sys.exit(f"\nThank you for using FinTrack !\n{special('2024 © FinTrack | Built by Tidjani. All rights reserved.','cyan')}\n")


def special(string, color):
    if color == 'cyan':
        return cyan(string, 'bold')
    elif color == 'magenta':
        return magenta(string, 'bold')


def total_income(a_month):
    temp_income = []
    total = 0
    with open(f'income/{a_month}.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp_income.append(row["amount"])
        for _ in temp_income:
            total += float(_)
    total = round(total, ndigits=2)
    return total


def total_expenses(a_month):
    temp_expenses = []
    total = 0
    with open(f'expenses/{a_month}.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp_expenses.append(row["amount"])
        for _ in temp_expenses:
            total += float(_)
    total = round(total, ndigits=2)
    return total


def balance(a_month):
    return total_income(a_month) - total_expenses(a_month)


def month_summary(a_month, option):
    _income = total_income(f"{a_month}")
    _expenses = total_expenses(f"{a_month}")
    if option == 1:
        _balance = balance(f"{a_month}")
        print("", f"{special(a_month + ' Summary ↓','magenta')}",
              f"Income: ${_income}\nExpenses: ${_expenses}\nBalance: ${_balance}\n",
              f"{special('© FinTrack', 'cyan')}", sep='\n')
    elif option == 2:
        print("", f"{special(a_month + ' Summary ↓', 'magenta')}",
              f"Income: ${_income}\nExpenses: ${_expenses}\n",
              f"{special('© FinTrack', 'cyan')}", sep='\n')


def error_message(option):
    if option == 1:
        print("Please tap a valid number.")
    elif option == 2:
        print("Please enter a valid month.")
    elif option == 3:
        print("Please enter a valid day.")
    elif option == 4:
        print("Please tap a valid amount.")


def valid_options(option):
    if option == 1:
        return [1, 2, 3, 4, 5, 6, 7, 0]
    elif option == 2:
        return [1, 2]
    elif option == 3:
        return list(range(1,32))


def details_incomes(a_month):
    details_income_final = []
    details_income_final.append(list(map(lambda i:special(i, "magenta"), income_headers)))
    with open(f"income/{a_month}.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            details_income_temp = []
            for i in row:
                if i == "date":
                    details_income_temp.append(date_format(int(row[i]),give_month_number(a_month)))
                elif i == "amount":
                    details_income_temp.append(f"${row[i]}")
                else:
                    details_income_temp.append(row[i])
            details_income_final.append(details_income_temp)
    return details_income_final


def date_format(a_date, a_month):
    if a_date < 10:
        if a_month < 10:
            return "0" + str(a_date) + "-" + "0" + str(a_month) + "-2024"
        else:
            return "0" + str(a_date) + "-" + str(a_month) + "-2024"
    else:
        if a_month < 10:
            return str(a_date) + "-" + "0" + str(a_month) + "-2024"
        else:
            return str(a_date) + "-" + str(a_month) + "-2024"


def details_expenses(a_month):
    details_expense_final = []
    details_expense_final.append(list(map(lambda i:special(i, "magenta"), expenses_headers)))
    with open(f"expenses/{a_month}.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            details_expense_temp = []
            for i in row:
                if i == "date":
                    details_expense_temp.append(date_format(int(row[i]),give_month_number(a_month)))
                elif i == "amount":
                    details_expense_temp.append(f"${row[i]}")
                else:
                    details_expense_temp.append(row[i])
            details_expense_final.append(details_expense_temp)
    return details_expense_final


def month_prompt():
    first_time = True
    while True:
        try:
            if first_time:
                month_option = ((str(input("\nEnter the month for which you want to display the finances\n$ ")))
                                .capitalize())
                first_time = False
            else:
                month_option = str(input("$ ")).capitalize()
            if month_option in valid_months:
                break
            error_message(2)
        except ValueError:
            error_message(2)
    return month_option


def inc_or_exp_prompt():
    first_time_bis = True
    while True:
        try:
            if first_time_bis:
                users_option2 = int(input("\n→ Tap 1 for Income\n→ Tap 2 for Expenses\n\n$ "))
                first_time_bis = False
            else:
                users_option2 = int(input("$ "))
            if users_option2 in valid_options(2):
                break
            error_message(1)
        except ValueError:
            error_message(1)
    return users_option2


def print_table(a_month, option):
    if option == "income":
        print("", f"{special(a_month + ' income Details ↓', 'cyan')}", "",
              tabulate(details_incomes(f"{a_month}"), tablefmt="grid"), "",
              f"{special('→ TOTAL: ', 'magenta')}${total_income(a_month)}", "",
              f"{special('© FinTrack', 'cyan')}", "", sep='\n')
    elif option == "expenses":
        print("", f"{special(a_month + ' expenses Details ↓', 'cyan')}", "",
              tabulate(details_expenses(f"{a_month}"), tablefmt="grid"), "",
              f"{special('→ TOTAL SPENT: ', 'magenta')}${total_expenses(a_month)}", "",
              f"{special('© FinTrack', 'cyan')}", "", sep='\n')


def total_income_year():
    total = 0
    for _ in range(1, 13):
        total += total_income(give_month(_))
    total = round(total, ndigits=2)
    return total


def total_expenses_year():
    total = 0
    for _ in range(1, 13):
        total += total_expenses(give_month(_))
    total = round(total, ndigits=2)
    return total


def balance_year():
    return total_income_year() - total_expenses_year()


def year_summary():
    _income = total_income_year()
    _expenses = total_expenses_year()
    _balance = balance_year()
    print("", f"{special('THIS YEAR Summary ↓', 'magenta')}",
          f"Total Income: ${_income}\nTotal Spent: ${_expenses}\nBalance: ${_balance}\n",
          f"{special('© FinTrack', 'cyan')}", sep='\n')


def income_writer(a_month):
    source = input("\n→ What's the source of this income ?\n$ ").title()
    while True:
        try:
            amount = float(input("\n→ What's the amount of this income ?\n$ "))
            break
        except ValueError:
            error_message(4)
    category = input("\n→ What's the category of this income ?\n$ ").title()
    depository = input("\n→ What's the depository of this income ?\n$ ").title()
    while True:
        try:
            date = int(input("\n→ When did you receive this income ?\nPlease just write the day (ex. if the date is \
13-07-2024, just write 13. Or if it's 09-07-2024, write 9)\n$ "))
            if date in valid_options(3):
                break
            error_message(3)
        except ValueError:
            error_message(3)
    with open(f'income/{a_month}.csv', 'a') as file:
        file.write(f"\n{source},{amount},{category},{depository},{date}")


def new_income():
    while True:
        try:
            users_option = int(input("\n→ Tap 1 if you want to add a new income for the current month\n→ \
Tap 2 if you want to add a new income for any month\n\n$ "))
            if users_option in valid_options(2):
                break
            error_message(1)
        except ValueError:
            error_message(1)
    if users_option == 1:
        income_writer(current_month)
    elif users_option == 2:
        income_writer(month_prompt())
    print("\nYour income has been successfully added to the database.",
          f"\n{special('© FinTrack','cyan')}\n")


def expense_writer(a_month):
    source = input("\n→ What's the source of this expense ?\n$ ").title()
    while True:
        try:
            amount = float(input("\n→ What's the amount of this expense ?\n$ "))
            break
        except ValueError:
            error_message(4)
    category = input("\n→ What's the category of this expense ?\n$ ").title()
    payment_method = input("\n→ What payment method did you use for this expense ?\n$ ").title()
    while True:
        try:
            date = int(input("\n→ When did you do this expense ?\nPlease just write the day (ex. if the date is \
13-07-2024, just write 13. Or if it's 09-07-2024, write 9)\n$ "))
            if date in valid_options(3):
                break
            error_message(3)
        except ValueError:
            error_message(3)
    with open(f'expenses/{a_month}.csv', 'a') as file:
        file.write(f"\n{source},{amount},{category},{payment_method},{date}")


def new_expense():
    while True:
        try:
            users_option = int(input("\n→ Tap 1 if you want to add a new expense for the current month\n→ \
Tap 2 if you want to add a new expense for any month\n\n$ "))
            if users_option in valid_options(2):
                break
            error_message(1)
        except ValueError:
            error_message(1)
    if users_option == 1:
        expense_writer(current_month)
    elif users_option == 2:
        expense_writer(month_prompt())
    print("\nYour expense has been successfully added to the database.",
          f"\n{special('© FinTrack','cyan')}\n")


if __name__ == "__main__":
    main()
