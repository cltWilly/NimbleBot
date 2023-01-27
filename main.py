import json
import os
import subprocess

def checkUpdate():
    # Get the current version of the project from the local files
    with open("./version.txt", "r") as file:
        current_version = file.read().strip()

    # Get the latest version of the project from the GitHub API
    url = "https://api.github.com/repos/cltWilly/NimbleBot/releases/latest"
    release_info = json.loads(subprocess.check_output(["curl", url]))
    latest_version = release_info["latest"]

    # Check if a new version is available
    if latest_version != current_version:
        print(f"Updating to version {latest_version}")

        # Remove the existing project files
        subprocess.call(["rm", "-rf", "./"])

        # Clone the latest version of the repository
        subprocess.call(["git", "clone", "https://github.com/cltWilly/NimbleBot.git", "./"])

        # Update the version file
        with open("./version.txt", "w") as file:
            file.write(latest_version)

        # Restart the app
        subprocess.call(["./start_app.sh"])
    else:
        print("No updates available.")

if __name__ == "__main__":
    checkUpdate()
