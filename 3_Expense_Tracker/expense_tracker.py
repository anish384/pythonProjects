import argparse
import json
import calendar
from datetime import datetime
import os
import textwrap

FILE_NAME = "data.json"

class ExpenseTracker:
    def __init__(self):
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w") as f:
                json.dump([], f)

    def get_data(self):
        try:
            with open(FILE_NAME, "r") as f:
                content = f.read()
                # Handle empty file case
                if not content:
                    return []
                return json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_data(self, tasks):
        try:
            with open(FILE_NAME, "w") as f:
                json.dump(tasks, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add(self, args):
        tasks = self.get_data()
        
        if tasks:
            new_id = max(task["id"] for task in tasks) + 1
        else:
            new_id = 1

        now = datetime.now()
        data = {
            "id": new_id,
            "desc": args.description,
            "amt": args.amount,
            "date": now.strftime("%Y-%m-%d"),
            "month": now.strftime("%B")
        }
        
        tasks.append(data)
        self.save_data(tasks)
        print(f"Success: Added expense '{args.description}' with ID {new_id}")

    def list_expenses(self):
        tasks = self.get_data()
        if not tasks:
            print("No expenses found.")
            return

        ID_W, DATE_W, DESC_W, AMT_W = 5, 12, 30, 10
        
        header = f"{'ID':<{ID_W}} {'Date':<{DATE_W}} {'Description':<{DESC_W}} {'Amount':>{AMT_W}}  {'Month'}"
        
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for task in tasks:
            t_id = str(task['id'])
            t_date = task['date']
            t_desc = task['desc']
            t_amt = f"{task['amt']:.2f}"
            t_month = task['month']

            wrapped_lines = textwrap.wrap(t_desc, width=DESC_W) or [""]

            print(f"{t_id:<{ID_W}} {t_date:<{DATE_W}} {wrapped_lines[0]:<{DESC_W}} {t_amt:>{AMT_W}}  {t_month}")

            for line in wrapped_lines[1:]:
                print(f"{'':<{ID_W}} {'':<{DATE_W}} {line:<{DESC_W}} {'':>{AMT_W}}")

        print("-" * len(header))

    def summary(self, args):
        tasks = self.get_data()
        total = 0
        
        if args.month:
            if args.month < 1 or args.month > 12:
                print("Error: Please enter valid month number (1-12)")
                return
            
            target_month = calendar.month_name[args.month]
            filtered_tasks = [t for t in tasks if t["month"] == target_month]
            
            total = sum(t["amt"] for t in filtered_tasks)
            print(f"Total Expense for {target_month}: {total:.2f}")
        else:
            total = sum(t["amt"] for t in tasks)
            print(f"Total Overall Expense: {total:.2f}")

    def delete(self, args):
        tasks = self.get_data()
        
        task_exists = any(task['id'] == args.id for task in tasks)
        if not task_exists:
            print(f"Error: ID {args.id} not found")
            return

        new_tasks = [task for task in tasks if task['id'] != args.id]
        self.save_data(new_tasks)
        print(f"Success: Deleted expense with ID {args.id}")

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for ADD
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", "-d", required=True, help="Description of expense")
    add_parser.add_argument("--amount", "-a", required=True, type=float, help="Amount spent") # Changed to float

    # Subparser for LIST
    subparsers.add_parser("list", help="List all expenses")

    # Subparser for SUMMARY
    sum_parser = subparsers.add_parser("summary", help="Show expense summary")
    sum_parser.add_argument("--month", "-m", type=int, help="Month number (1-12)")

    # Subparser for DELETE
    del_parser = subparsers.add_parser("delete", help="Delete an expense")
    del_parser.add_argument("--id", required=True, type=int, help="ID of expense to delete")

    args = parser.parse_args()
    
    tracker = ExpenseTracker()

    if args.command == "add":
        tracker.add(args)
    elif args.command == "list":
        tracker.list_expenses()
    elif args.command == "summary":
        tracker.summary(args)
    elif args.command == "delete":
        tracker.delete(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
