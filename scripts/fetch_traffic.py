import requests
import os
import datetime
import csv

repo = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {token}"}

views_url = f"https://api.github.com/repos/{repo}/traffic/views"
clones_url = f"https://api.github.com/repos/{repo}/traffic/clones"

views = requests.get(views_url, headers=headers).json()
clones = requests.get(clones_url, headers=headers).json()

today = datetime.date.today()

row = [
    str(today),
    views.get("count", 0),
    views.get("uniques", 0),
    clones.get("count", 0),
    clones.get("uniques", 0),
]

csv_file = "traffic-log.csv"

write_header = not os.path.exists(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if write_header:
        writer.writerow(["Date", "Views", "Unique Views", "Clones", "Unique Clones"])
    writer.writerow(row)
