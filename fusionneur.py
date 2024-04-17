import PyPDF2
import argparse
import os

parser = argparse.ArgumentParser(description='Fusionne plusieurs PDF en un seul.')
parser.add_argument('-name', '--name', help='Nom du fichier de sortie, ne pas indiquer d\'extension svp (par défaut : fusion.pdf)')

args = parser.parse_args()

fusionneur = PyPDF2.PdfMerger()

chemin_fichiers = 'fichiers_pre_fusion/'

fichiers = sorted(os.listdir(chemin_fichiers), key=str.lower)

for fichier in fichiers:
    if fichier.endswith(".pdf"):
        # print(fichier)
        fusionneur.append(open(chemin_fichiers +fichier, 'rb'))

if not args.name:
    nom_sortie = 'fusion.pdf'
else:
    nom_sortie = args.name + '.pdf'

with open(nom_sortie, 'wb') as fichier_sortie:
    fusionneur.write(fichier_sortie)

print(f'Fusion effectuée avec succès dans le fichier {nom_sortie}.')