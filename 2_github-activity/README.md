# 📂 GitHub User Activity Fetcher

A Python command-line interface (CLI) tool that fetches and displays recent activity for any GitHub user using the GitHub API.

This project was built to practice **Object-Oriented Programming (OOP)** principles in Python and to demonstrate how to interact with external APIs.

## 🚀 Features

* **API Integration:** Connects to the GitHub Events API to retrieve real-time data.
* **Error Handling:** Gracefully handles invalid usernames (404), API errors, and connection issues.
* **Structured Output:** Parses raw JSON data into human-readable activity logs (e.g., Pushes, Stars, Issue creation).
* **OOP Design:** distinct separation of concerns using classes and methods.

## 🛠️ Prerequisites

To run this project, you need:
* Python 3.x installed on your system.
* The `requests` library.

## 📦 Installation & Usage

1.  **Clone the repository** (or download the script):
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2.  **Install the required library:**
    ```bash
    pip install requests
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```

4.  **Enter a username** when prompted:
    ```text
    Enter your github username: torvalds
    ```

## 🏗️ Code Structure & Concepts

This project demonstrates the following Python concepts:

* **Encapsulation:** The `GitHubActivity` class encapsulates the data (username, URL, events) and the logic for fetching it (`fetch_events`), keeping the main execution flow clean.
* **Abstraction:** The `_print_single_event` helper method hides the complexity of parsing different event types (PushEvent, WatchEvent, etc.) from the main display loop.
* **JSON Parsing:** processing nested dictionaries from the API response.

## 📝 Example Output

```text
Enter your github username: anish384

Output for anish384:
------------------------------
- Pushed 3 commits to anish384/pythonProjects
- Starred roadmapsh/roadmap
- Created a repository/branch in anish384/task-cli
- Closed an issue in anish384/expense-tracker
```

## 🔗 Project Reference

This project is based on the **GitHub User Activity** project idea from roadmap.sh:

👉 [https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)

