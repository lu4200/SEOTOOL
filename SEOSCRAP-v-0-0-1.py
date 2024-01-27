#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SEOSCRAP v.0.0.1 11/07/2023

import requests
from bs4 import BeautifulSoup
import time

url = input("Entrez un URL de site à analyser: ")  # Remplace avec l'URL du site que tu souhaites analyser
response = requests.get(url)
html_content = response.text



#récuperation du loadtime ✅

start_time = time.time()
end_time = time.time()
page_load_time = end_time - start_time
print("Temps de chargement de la page :", page_load_time, "secondes")





# réuperation du nombre de mots ❌
soup = BeautifulSoup(html_content, "html.parser")
paragraphs = soup.find_all("p")  # Trouver toutes les balises <p>

word_list = []  # Initialise une liste vide pour stocker les mots

for paragraph in paragraphs:
    text = paragraph.get_text()  # Récupèrer le texte de chaque balise <p>
    words = text.split()  # Sépare le texte en mots
    word_list.extend(words)  # Ajoute les mots à la liste

word_count = len(word_list)

print("Nombre de mots dans les balises <p> :", word_count)
# 🆑 vérifier les mots que soup scrap du site car résultats aberrants
print("Liste des mots dans les balises <p> :", word_list)



