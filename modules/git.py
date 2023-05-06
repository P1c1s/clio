from colors import *
import sys


def show():

 
  print("+********************************************************************+")
  print("********************QUICK LIST OF GIT COMMANDS*********************")
  print("+********************************************************************+")
  print("\n")
  print("Git is a popular version control system. It was created by Linus Torvalds in 2005,")
  print("and has been maintained by Junio Hamano since then. It is used for: ")
  print("+ Tracking code changes")
  print("+ Tracking who made changes")
  print("+ Coding collaboration")
  print("\n")
  print("The fils about a git project can be in three different status: ")
  print("Committed: The files have been stored in the database.")
  print("Modified: The files have been changed but they have not been commited yet.")
  print("In stage: The files have been affected by changes and will be included in a snapshot with the next commit.")
  print("etc/gitconfig  -  ~/.gitconfig  -  .git/config")

  scheme= """


                  STATUS SCHEME

    * * * * * * *                * * * * * * *
   *             *              *             *
  *               *            *               *
 *       WORK      *          *      STAGE      *
 *    DIRECTORY    *   ---+   *      AREA       *
 *                 *          *                 *
  *               *            *               *
   *             *              *             *
    * * * * * * *                * * * * * * *

               +                    /
                \                  /
                 \                +

                  * * * * * * *
                 *             *
                *               *
               *       GIT       *
               *    DIRECTORY    *
               *                 *
                *               *
                 *             *
                  * * * * * * *
  """
  print(scheme)

  print(YELLOWBOLD, "About Git")
  print("git --version  -  Check if git is properly installed and if true return the current version of git")
  print("git command -help  -  See all the available options for the specific command")
  print("git help --all  -  See all possible commands")
  print("git config <--global or --local> user.name <username>  -  ")
  print("git config <--global or --local> user.email <name@email.it>  -  ")
  print("git config <--global or --local> core.editor emacs  -  Define a default editor")
  print("git config --list  -  Print the list of settings about git")
  print("git status  -  ")
  print("\n")

  print(GREENBOLD,"First Steps",GREEN)
  print("git init  -  Initialize a new a git project")
  print("git status  -  ...")
  print("git add <file/files>")
  print("git commit -m <comment>")
  print("git commit rm --cached <file>  -  Remove file from Stage Area")
  print("git log  -  Commits history")
  print("git checkout -- <file>  -  Return to last commit ")
  print("git push  -  ")
  print("git pull  -  ")
  print("git clone  -  ")
  print("git add remote origin <site>  -  ")
  print("git remote -v   -  ")
  print("\n")


  print(WHITEBOLD,"Manage Branches",WHITE)
  print("git branch  -  ")
  print("git branch <branch name> -  ")
  print("git show-branch  -  ")
  print("git merge")
  print("git checkout <branch name>  -  Switch branches or restore working tree files")
  print("git reset ")

  print(PURPLE,"                             ***            ")
  print(PURPLE,"                +--------------*****-------------+            ")
  print(PURPLE,"                |               ***              |")
  print(GREENBOLD,"     ***        ${PURPLE}|${GREENBOLD}                     ${GREENBOLD}***${PURPLE}        |")
  print(GREENBOLD,"*---*****----------------------------*****----------*")
  print(GREENBOLD,"     ***                              ***              ")


  print(WHITEBOLD, "Others", WHITE)
  print("git <command> -help")
  print("git <command> --short")
  

def list():
  print("[...]")

# get the name of file from the path e.g. path="/home/user/script.py" return script.py
app=sys.argv[0].split("/")
file_name = app[len(sys.argv[0].split("/"))-1]

if file_name == "git.py" and len(sys.argv) > 1 and sys.argv[1] == "list":
  show()