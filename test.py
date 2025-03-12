import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration de Selenium
options = Options()
options.add_argument("--headless")  # Exécuter sans interface graphique
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Installer et lancer ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration de Selenium
options = Options()
options.add_argument("--headless")  # Exécuter sans interface graphique
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Installer et lancer ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def ligueChampion():
    # URL de la page
    url = "https://www.betclic.fr/football-sfootball/ligue-des-champions-c8"
    driver.get(url)

    # Attendre que la page charge (ajuste si besoin)
    time.sleep(3)

    # Créer la fenêtre Tkinter
    root = tk.Tk()
    root.title("Résultats des Cotes de Matchs")
    root.geometry("600x400")  # Ajuster la taille de la fenêtre

    # Créer un widget Text pour afficher les résultats
    results_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
    results_text.pack(padx=10, pady=10)

    # Ajouter un titre dans la fenêtre
    results_text.insert(tk.END, "Résultats des cotes de matchs :\n\n")
    results_text.insert(tk.END, "-" * 50 + "\n")

    i = 1  # Démarre à 1 pour le premier match

    while i < 10:
        try:
            # Localiser l'élément avec le sélecteur CSS en utilisant By
            element = driver.find_element(By.CSS_SELECTOR,
                                          f'body > app-desktop > app-desktop-sports-layout > div.layout > div > bcdk-content-scroller > div > sports-competition > div:nth-child(5) > sports-events-list > bcdk-vertical-scroller > div > div.verticalScroller_wrapper > div > div > div:nth-child(2) > div.groupEvents_content > sports-events-event-card:nth-child({i}) > a > div > sports-events-event-markets > sports-default-markets > div > div > button:nth-child(1)')

            element2 = driver.find_element(By.CSS_SELECTOR,
                                           f'body > app-desktop > app-desktop-sports-layout > div.layout > div > bcdk-content-scroller > div > sports-competition > div:nth-child(5) > sports-events-list > bcdk-vertical-scroller > div > div.verticalScroller_wrapper > div > div > div:nth-child(2) > div.groupEvents_content > sports-events-event-card:nth-child({i}) > a > div > sports-events-event-markets > sports-default-markets > div > div > button:nth-child(2)')

            element3 = driver.find_element(By.CSS_SELECTOR,
                                           f'body > app-desktop > app-desktop-sports-layout > div.layout > div > bcdk-content-scroller > div > sports-competition > div:nth-child(5) > sports-events-list > bcdk-vertical-scroller > div > div.verticalScroller_wrapper > div > div > div:nth-child(2) > div.groupEvents_content > sports-events-event-card:nth-child({i}) > a > div > sports-events-event-markets > sports-default-markets > div > div > button:nth-child(3)')

            # Récupérer le texte contenu dans les éléments
            text = element.text.strip()
            text2 = element2.text.strip()
            text3 = element3.text.strip()

            # Affichage formaté dans la fenêtre Tkinter
            if text and text2 and text3:
                results_text.insert(tk.END, f"Match {i} :\n")
                results_text.insert(tk.END, f"  - Cote 1: {text}\n")
                results_text.insert(tk.END, f"  - Cote Nul: {text2}\n")
                results_text.insert(tk.END, f"  - Cote 2: {text3}\n")
                results_text.insert(tk.END, "-" * 50 + "\n")
            else:
                results_text.insert(tk.END, f"Match {i} : Aucune cote disponible.\n")
                results_text.insert(tk.END, "-" * 50 + "\n")

            i += 1  # Incrémenter l'index

        except Exception:
            # Ne rien faire si une erreur se produit, on continue avec le match suivant
            i += 1  # Incrémenter même en cas d'erreur pour essayer les autres matchs

    # Fermer le navigateur après avoir récupéré les données
    driver.quit()

    # Lancer l'interface Tkinter
    root.mainloop()

def ligueEurope():
    # URL de la page
    url = "https://www.betclic.fr/football-sfootball/ligue-europa-c3453"
    driver.get(url)

    # Attendre que la page charge (ajuste si besoin)
    time.sleep(3)

    # Créer la fenêtre Tkinter
    root = tk.Tk()
    root.title("Résultats des Cotes de Matchs")
    root.geometry("600x400")  # Ajuster la taille de la fenêtre

    # Créer un widget Text pour afficher les résultats
    results_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
    results_text.pack(padx=10, pady=10)

    # Ajouter un titre dans la fenêtre
    results_text.insert(tk.END, "Résultats des cotes de matchs :\n\n")
    results_text.insert(tk.END, "-" * 50 + "\n")

    i = 1  # Démarre à 1 pour le premier match

    while i < 10:
        try:
            # Localiser l'élément avec le sélecteur CSS en utilisant By
            element = driver.find_element(By.CSS_SELECTOR,
                                          f'body > app-desktop > app-desktop-sports-layout > div.layout > div > bcdk-content-scroller > div > sports-competition > div:nth-child(5) > sports-events-list > bcdk-vertical-scroller > div > div.verticalScroller_wrapper > div > div > div:nth-child(1) > div.groupEvents_content > sports-events-event-card:nth-child({i}) > a > div > sports-events-event-markets > sports-default-markets > div > div > button:nth-child(1)')

            element2 = driver.find_element(By.CSS_SELECTOR,
                                           f'body > app-desktop > app-desktop-sports-layout > div.layout > div > bcdk-content-scroller > div > sports-competition > div:nth-child(5) > sports-events-list > bcdk-vertical-scroller > div > div.verticalScroller_wrapper > div > div > div:nth-child(1) > div.groupEvents_content > sports-events-event-card:nth-child({i}) > a > div > sports-events-event-markets > sports-default-markets > div > div > button:nth-child(2)')

            element3 = driver.find_element(By.CSS_SELECTOR,
                                           f'body > app-desktop > app-desktop-sports-layout > div.layout > div > bcdk-content-scroller > div > sports-competition > div:nth-child(5) > sports-events-list > bcdk-vertical-scroller > div > div.verticalScroller_wrapper > div > div > div:nth-child(1) > div.groupEvents_content > sports-events-event-card:nth-child({i}) > a > div > sports-events-event-markets > sports-default-markets > div > div > button:nth-child(3)')

            # Récupérer le texte contenu dans les éléments
            text = element.text.strip()
            text2 = element2.text.strip()
            text3 = element3.text.strip()

            # Affichage formaté dans la fenêtre Tkinter
            if text and text2 and text3:
                results_text.insert(tk.END, f"Match {i} :\n")
                results_text.insert(tk.END, f"  - Cote 1: {text}\n")
                results_text.insert(tk.END, f"  - Cote Nul: {text2}\n")
                results_text.insert(tk.END, f"  - Cote 2: {text3}\n")
                results_text.insert(tk.END, "-" * 50 + "\n")
            else:
                results_text.insert(tk.END, f"Match {i} : Aucune cote disponible.\n")
                results_text.insert(tk.END, "-" * 50 + "\n")

            i += 1  # Incrémenter l'index

        except Exception:
            # Ne rien faire si une erreur se produit, on continue avec le match suivant
            i += 1  # Incrémenter même en cas d'erreur pour essayer les autres matchs

    # Fermer le navigateur après avoir récupéré les données
    driver.quit()

    # Lancer l'interface Tkinter
    root.mainloop()

# Créer une fenêtre Tkinter principale avec les choix
def choixCompetition():
    choix_window = tk.Tk()
    choix_window.title("Choix de la compétition")
    choix_window.geometry("300x200")

    label = tk.Label(choix_window, text="Choisissez la compétition :")
    label.pack(pady=20)

    bouton_champion = tk.Button(choix_window, text="Ligue des Champions", command=ligueChampion)
    bouton_champion.pack(pady=10)

    bouton_europe = tk.Button(choix_window, text="Ligue Europa", command=ligueEurope)
    bouton_europe.pack(pady=10)

    # Lancer l'interface Tkinter principale
    choix_window.mainloop()

# Lancer la fenêtre de choix
choixCompetition()
