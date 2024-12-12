import os
import datetime
from random import randint

# Configuration
total_day = 365  # How far back to start commits
commit_freq = 10  # Number of commits per day
variability = False  # Set to True for random commits per day
repo_link = "https://github.com/arunmhh/gitquarto.git"  # Repository link

# Initialize variables
now = datetime.datetime.now()
pointer = 0
ctr = 1

# Initialize repository
if not os.path.exists(".git"):
    os.system("git init")
os.system("git config user.name 'Your Name'")
os.system("git config user.email 'your.email@example.com'")

with open("commit.txt", "a") as f:
    while total_day > 0:
        commits_today = randint(0, commit_freq) if variability else commit_freq
        
        for _ in range(commits_today):
            l_date = now - datetime.timedelta(days=pointer)
            formatdate = l_date.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Commit #{ctr}: {formatdate}\n")
            
            os.system("git add .")
            os.system(f'git commit --date="{formatdate}" -m "Commit #{ctr}"')
            print(f"Commit #{ctr}: {formatdate}")
            ctr += 1
        
        pointer += 1
        total_day -= 1

# Add remote and push
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")

