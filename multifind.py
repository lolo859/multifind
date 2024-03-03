import os,sys
def clear():
    if str(sys.platform).startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
while True:
    clear()
    choix=(input("Que souhaitez vous faire :\n  1 - rechercher tous les fichiers d'un type\n  2 - rechercher les fichiers avec un certain nom\n  3 - Sortir\nVotre choix : "))
    if choix=="1":
        ext=input("Extension du nom de fichier commençant par un point : ")
        path=input("Chemin d'accès où chercher : ")
        print("Scan du disque...")
        if str(sys.platform).startswith("win"):
            text=[os.path.join(root, file) for root, _, files in os.walk(path) for file in files]
        else:
            text=[os.path.join(root, file) for root, _, files in os.walk(path) for file in files]
        occur=[]
        number=[]
        for i in range(len(text)):
            print("Recherche dans les fichiers... "+str(((i+1)/len(text))*100)+"%")
            print("Ficher "+str(i)+"/"+str(len(text))+" : "+text[i])
            if text[i].endswith(ext):
                number.append(str(i+1))
                occur.append(text[i])
            clear()
        if len(occur)==0:
            print("Nous avons trouvé aucun résultats.")
            input("Entrer pour continuer...")
            clear()
        else:
            print("Nous avons trouvé "+str(len(occur))+" résultats :")
            for i in occur:
                print("  "+i)
            input("Entrer pour continuer...")
            clear()
    elif choix=="2":
        ext=input("Nom de fichier : ")
        path=input("Chemin d'accès où chercher : ")
        print("Scan du disque...")
        if str(sys.platform).startswith("win"):
            text=[os.path.join(root, file) for root, _, files in os.walk(path) for file in files]
        else:
            text=[os.path.join(root, file) for root, _, files in os.walk(path) for file in files]
        occur=[]
        number=[]
        for i in range(len(text)):
            print("Recherche dans les fichiers... "+str(((i+1)/len(text))*100)+"%")
            print("Ficher "+str(i)+"/"+str(len(text))+" : "+text[i])
            if os.path.basename(text[i]).find(ext)!=-1:
                number.append(str(i+1))
                occur.append(text[i])
            clear()
        if len(occur)==0:
            print("Nous avons trouvé aucun résultats.")
            input("Entrer pour continuer...")
            clear()
        else:
            print("Nous avons trouvé "+str(len(occur))+" résultats :")
            for i in occur:
                print("  "+i)
            input("Entrer pour continuer...")
            clear()
    elif choix=="3":
        clear()
        sys.exit()