# 💰 Expense Tracker CLI

A simple, robust command-line application to manage your personal finances. This tool allows you to add, view, and analyze your expenses directly from the terminal.

This project was built to practice file handling, JSON manipulation, and argument parsing in Python.

## 🚀 Features

* **Add Expenses:** Record new expenses with a description and amount.
* **List Records:** View a formatted table of all recorded expenses.
* **Summary Stats:** View total expenses overall or filtered by a specific month.
* **Delete Records:** Remove specific entries using their unique ID.
* **Data Persistence:** Automatically saves all data to a local `data.json` file.

## 🛠️ Prerequisites

* Python 3.x
* No external libraries required (uses standard `argparse`, `json`, `os`, etc.)

## 📖 Usage Guide

Save your script as `expense_tracker.py` and run the following commands in your terminal.

### 1. Add an Expense
Use the `add` command with a description (`-d`) and amount (`-a`).
```bash
python expense_tracker.py add --description "Lunch with friends" --amount 250
# OR
python expense_tracker.py add -d "Coffee" -a 50
```

### 2. List All Expenses

View a clean table of all your transactions.

Bash

```
python expense_tracker.py list
```

_Example Output:_

Plaintext

```
ID    Date         Description                    Amount   Month
------------------------------------------------------------------
1     2025-11-23   Lunch with friends             250.00   November
2     2025-11-23   Coffee                          50.00   November
------------------------------------------------------------------
```

### 3. View Summary

Get the total sum of your expenses.

**Overall Total:**

Bash

```
python expense_tracker.py summary
```

**Specific Month (e.g., August = 8):**

Bash

```
python expense_tracker.py summary --month 8
```

### 4. Delete an Expense

Remove an entry using its ID (found in the `list` command).

Bash

```
python expense_tracker.py delete --id 1
```

## 🏗️ Technical Details

This project uses the `argparse` library to handle subcommands (`add`, `list`, etc.). Data is stored persistently in a `data.json` file, which the script automatically creates if it doesn't exist.

## 🔗 Project Reference

This project implements the requirements for the **Expense Tracker** project from roadmap.sh:

👉 [https://roadmap.sh/projects/expense-tracker](https://roadmap.sh/projects/expense-tracker)
