# 📘 Git Complete Notes

## 🔍 Installation & Configuration
```bash
git --version                           # Check Git is installed
git config --global user.name "Your Name"    # Set global username
git config --global user.email "your_email@gmail.com"   # Set global email
git config --global core.editor "code --wait"   # VS Code as editor
git config --global core.autocrlf input        # Handle line endings (Windows/Linux)
git config --global -e                  # Open global config for edit

🚀 Start a New Project
git init                                # Initialize new Git repo
git add .                               # Stage all files
git commit -m "first commit"            # Save point (commit)
git log                                 # Show full commit history
git log --oneline                       # Show commits in one line
git log --oneline --graph               # Show commits with graph

🛑 Ignore Files
# Create a .gitignore file
# Add file/folder names inside it to prevent pushing them to GitHub

🔄 Resetting Commits
git reset --hard HEAD~1                 # Reset to 1 commit back (delete changes)
git reset --soft HEAD~1                 # Reset but keep changes staged
git reset --mixed HEAD~1                # Reset but keep changes unstaged

📌 Git Status
git status                              # Show current changes status
git status -s                           # Show short status

🌿 Branching & Switching
git branch branchname                   # Create new branch
git branch                              # List all branches
git switch branchname                   # Switch branch
git switch -C branchname                # Create + switch branch

🔀 Merging Branches
git switch main                         # Move to main branch
git merge branchname                    # Merge branch into main

⚔️ Conflict Handling
# Fix conflicts manually in editor, then:
git add .                               # Stage resolved files
git commit                              # Commit after fixing conflicts

🧹 Branch Management
git branch -d branchname                # Delete branch

📦 Stashing
git stash                               # Save changes temporarily
git stash apply                         # Re-apply stashed changes
git stash clear                         # Delete all stashes


👥 Collaboration Workflow

🏆 Main Person (Example: Suresh)
git init                                # Initialize repo
git add .                               # Stage files
git commit -m "initial commit"          # First commit
git remote add origin <repo-url>        # Add remote repo
git push origin main                    # Push to GitHub

🤝 Collaborator (Example: Pritam)
git clone <repo-url>                    # Clone repo
git checkout -b feature/branch          # Create + switch to new branch
git add .                               # Stage changes
git commit -m "work done"               # Commit changes
git push -u origin feature/branch       # Push to GitHub branch

🔄 Merge Process
# Main Person (Suresh)
git switch main                         # Switch to main
git merge feature/branch                # Merge collaborator branch
git push origin main                    # Push merged code

# Collaborator (Pritam)
git fetch                               # Fetch updates
git pull                                # Pull latest code


🚀 Advanced Git Commands
# 🔗 Remote Management
git remote -v                           # Show remote URLs
git remote add origin <url>             # Add remote repo
git remote remove origin                # Remove remote repo

# ⏪ Undo Changes
git restore file.txt                    # Undo changes in file
git restore --staged file.txt           # Unstage file
git checkout commitID file.txt          # Restore file from old commit

# 🔁 Rebase
git rebase main                         # Rebase current branch with main

# 📝 Amend Last Commit
git commit --amend                      # Edit last commit or add changes

# 🏷️ Tagging
git tag v1.0.0                          # Create tag
git tag                                 # List tags
git push origin v1.0.0                  # Push specific tag
git push origin --tags                  # Push all tags

# ⚡ Aliases (Shortcuts)
git config --global alias.st status     # 'git st' instead of 'git status'
git config --global alias.ci commit     # 'git ci' instead of 'git commit'
git config --global alias.co checkout   # 'git co' instead of 'git checkout'
git config --global alias.br branch     # 'git br' instead of 'git branch'
