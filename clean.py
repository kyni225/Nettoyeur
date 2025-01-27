import os
import shutil


def cree_subfolder_if_needed(chemin_dossier, subfolder_name):
    subfolder_path = os.path.join(chemin_dossier, subfolder_name)
    if not os.path.exists(subfolder_path):
          os.makedirs(subfolder_path)
    return subfolder_path
def move_file_to_subfolder(chemin_dossier, subfolder_path):

 def clean_dossier(chemin_dossier):
      
      for nomfichier in os.listdir(chemin_dossier):
           if os.path.isfile(os.path.join(chemin_dossier, nomfichier)):
                extension_fichier = nomfichier.split('.')[-1].lower()
                if extension_fichier:
                     subfolder_name =f"{extension_fichier.upper()} fichier"
                     subfolder_path = cree_subfolder_if_needed(chemin_dossier, subfolder_name)
                     chemin_fichier = os.path.join(chemin_dossier, nomfichier)
                     nouveau_localisation = os.path.join(subfolder_path, nomfichier)

                     if not os.path.exists(nouveau_localisation):
                        
                        print(f" deplacez vous dans:{nomfichier} -> {subfolder_name}/")
                     else:
                        print(f"skipped:{nomfichier} al {subfolder_name}/")


if __name__ == "__main__":
    print("Nettoyer la machine")
    chemin_dossier ='/Users/hp/Downloads'
    if os.path.isdir(chemin_dossier):
        
        print("Nettoyer completement.")
    else:
        print(" Chemin du dossier est invalide. Assurez vous que le chemin est correct et reessayer.")