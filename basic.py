"""

Check On Cmd Git is Intall or Not 
- git

Extension
- git blame
- git autoconfig
optional - git theme


start
-----------------------------------------------------------------------------------------------------

git config --global user.name "name"
- git should need to now your name, global user name setup

git config --global user.email "email@gmail.com"
- git set global email

git config --global core.editor "code --wait"
- "code --wait" => code means vs code mai chalu karna and wait matlab jab tak vs code mai chalu nhi hota tab tak wait likh ke aayega

git config --global core.autocrlf "input"
- map se data push hoga, varna windows se puch hoga toh central mai jake kaise data save hoga

git config --global -e
- to check and edit the global value and see the global value


------------------------------------------------------------------------------------------------------

git init -> to init project
git add . -> to add a file, but not pushed "A"
git commit -m "first commit" => save point of git the folder was added before

to now current status of save point run cmd 
- git log --oneline
- git log => show every thing with date, time author etc.
- git log --oneline --graph => 

to ignore such file that does not need to push, write that particular file name inside that file
- create file => .gitignore

to reset or go back to previous code
hard => jitna bhi commit the pichla voh sab data do aur direct voh wala dikhao jaise tab har ek file folder tha
soft, mixed
- git reset --hard HEAD~1 => ek step piche jayega


check kr skte ho aap konsi file kis stage mein hai
- git status -s => show only maine think
- git status => show every thing

check karna ki kitne save checkpoints hai
- git log



"""