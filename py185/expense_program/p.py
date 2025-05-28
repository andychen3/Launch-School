import psycopg2
from psycopg2 import extras
import sys
from textwrap import dedent
from datetime import date





def list_expenses():
    connection = psycopg2.connect(dbname="expenses")
    try:
        with connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor.execute("""SELECT * FROM expenses""")
                expenses = cursor.fetchall()
    finally:
        connection.close()

    for expense in expenses:
        columns = [
            str(expense["id"]).rjust(3),
            str(expense["created_on"]),
            str(expense["amount"]).rjust(12),
            str(expense["memo"])
        ]
        print(" | ".join(columns))

def display_help():
    print(dedent("""
    An expense recording system

    Commands:

    add AMOUNT MEMO [DATE] - record a new expense
    clear - delete all expenses
    list - list all expenses
    delete NUMBER - remove expense with id NUMBER
    search QUERY - list expenses with a matching memo field
    """).strip("\n"))

def add_expense(amount, memo):
    connection = psycopg2.connect(dbname="expenses")
    try:
        with connection:
            with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor.execute("""INSERT INTO expenses (amount, memo, created_on)
                                    VALUES (%s, %s, %s)
                                """, (amount, memo, date.today()))
    finally:
        connection.close()

def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None
    if command == 'list':
        list_expenses()
        return
    elif command == 'add':
        amount = sys.argv[2] if len(sys.argv) >= 3 else None
        memo = sys.argv[3] if len(sys.argv) >= 4 else None

        try:
            amount = float(amount)
        except:
            print("Amount must be a number.")

        if isinstance(amount, float) and isinstance(memo, str):
            add_expense(amount, memo)
            return
        else:
            print("You must provide an amount and memo.")
            return
    display_help()


./expense add 14.56 Pencils
./expense add 3.29 Coffee
./expense add 49.99 "Text Editor"
./expense add 3.59 "More Coffee"