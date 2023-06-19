import os

commit_message = input("Enter commit message: ")

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")
