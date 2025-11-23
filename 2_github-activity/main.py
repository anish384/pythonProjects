import requests

class GitHubActivity:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.github.com/users/{username}/events"
        self.events = []  # Store the list of events here
        self.is_valid = False

    def fetch_events(self):
        """
        Encapsulation: The class handles the complexity of 
        connecting to the API and checking errors.
        """
        try:
            response = requests.get(self.url, timeout=10)
            
            if response.status_code == 200:
                self.events = response.json()
                self.is_valid = True
            elif response.status_code == 404:
                print(f"Error: User '{self.username}' not found.")
            else:
                print(f"Error: API returned status {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Connection Error: {e}")

    def display_activity(self):
        """
        Polymorphism/Logic: This method processes the raw data
        and presents it in a human-readable format.
        """
        if not self.is_valid:
            return

        if not self.events:
            print(f"No recent activity found for {self.username}.")
            return

        print(f"\nOutput for {self.username}:")
        print("-" * 30)

        for event in self.events:
            self._print_single_event(event)

    def _print_single_event(self, event):
        """
        Helper method to handle specific event types.
        """
        event_type = event.get('type')
        repo_name = event.get('repo', {}).get('name')

        if event_type == "PushEvent":
            commits = len(event.get('payload', {}).get('commits', []))
            print(f"- Pushed {commits} commits to {repo_name}")
            
        elif event_type == "IssuesEvent":
            action = event.get('payload', {}).get('action')
            print(f"- {action.capitalize()} an issue in {repo_name}")
            
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
            
        elif event_type == "CreateEvent":
            print(f"- Created a repository/branch in {repo_name}")
            
        else:
            # Handle other generic events
            print(f"- {event_type} on {repo_name}")

# --- Main Execution ---

user_input = input("Enter your github username: ")

activity_checker = GitHubActivity(user_input)

activity_checker.fetch_events()

activity_checker.display_activity()
