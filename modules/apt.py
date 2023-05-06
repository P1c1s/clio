import sys
from colors import *

def show_descriprion():
  print("list - List packages based on package names")
  print("search - Cerca tra le descrizioni dei pacchetti")
  print("show - Mostra dettagli di un pacchetto")
  print("install - Installa pacchetti")
  print("reinstall - Installa nuovamente pacchetti")
  print("remove - Rimuove pacchetti")
  print("autoremove - Rimuove automaticamente i pacchetti inutilizzati")
  print("update - Aggiorna l'elenco dei pacchetti disponibili")
  print("upgrade - Esegue l'avanzamento di versione del sistema installando e aggiornando i pacchetti")
  print("full-upgrade - Esegue l'avanzamento di versione del sistema rimuovendo, installando e aggiornando i pacchetti")
  print("edit-sources - Modifica il file sulle informazioni delle sorgenti")
  print("  satisfy - satisfy dependency strings")

#Classic Functions 
def about():
  print("This is apt")
def show():
  show_descriprion()
def list():
  print("[...]")


#get the name of file from the path e.g. path="/home/user/script.py" return script.py
app=sys.argv[0].split("/")
file_name = app[len(sys.argv[0].split("/"))-1]

if file_name == "docker.py" and len(sys.argv) > 1 and sys.argv[1] == "show":
  show()
if file_name == "docker.py" and len(sys.argv) > 1 and sys.argv[1] == "list":
  list()