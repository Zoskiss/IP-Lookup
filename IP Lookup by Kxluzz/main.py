import os
import requests
import logging
import msvcrt
import sys

# Configuration du logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Définit le niveau global des logs

# Crée un handler pour afficher les logs dans la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)  # Niveau pour la console (warnings et erreurs)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Crée un handler pour écrire les erreurs dans le fichier erreur.log
error_file_handler = logging.FileHandler('erreur.log')
error_file_handler.setLevel(logging.ERROR)  # Niveau pour le fichier (erreurs uniquement)
error_file_formatter = logging.Formatter('%(asctime)s - %(levellevel)s - %(message)s')
error_file_handler.setFormatter(error_file_formatter)

# Ajoute les handlers au logger
logger.addHandler(console_handler)
logger.addHandler(error_file_handler)

def get_ip_info(ip_address):
    """Utilise l'API ipinfo.io pour obtenir des informations sur l'IP."""
    try:
        logging.debug(f"Envoi de la requête à l'API pour l'adresse IP: {ip_address}")
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Vérifie les erreurs HTTP
        logging.debug(f"Réponse de l'API: {response.text}")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erreur lors de la récupération des informations pour l'IP {ip_address}: {e}")
        return None

def generate_single_color_text(text, color):
    """Génère un texte avec une couleur unie."""
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[0m"

def print_banner():
    """Affiche la bannière avec une couleur bleue claire et le texte à droite."""
    # Couleur bleue claire pour la bannière
    blue_light = (173, 216, 230)  # Bleu clair

    banner_lines = [
        "   ██╗  ██╗██╗  ██╗██╗     ██╗   ██╗███████╗███████╗",
        "   ██║ ██╔╝╚██╗██╔╝██║     ██║   ██║╚══███╔╝╚══███╔╝",
        "   █████╔╝  ╚███╔╝ ██║     ██║   ██║  ███╔╝   ███╔╝",
        "   ██╔═██╗  ██╔██╗ ██║     ██║   ██║ ███╔╝   ███╔╝",
        "██╗██║  ██╗██╔╝ ██╗███████╗╚██████╔╝███████╗███████╗",
        "╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝"
    ]

    # Affichage du texte avec la couleur bleue claire
    for line in banner_lines:
        print(generate_single_color_text(line, blue_light))

    # Réajuster le texte "Réalisé par : .Kxluzz" vers la gauche sous la bannière
    print(generate_single_color_text("Réalisé par : .Kxluzz [+] .gg/kfshop [+]", blue_light))

def print_ip_request_prompt():
    """Affiche le texte de demande d'IP avec la couleur bleu clair."""
    prompt_text = "Entrez une adresse IP pour obtenir des informations : "
    print("\n")  # Ligne vide pour l'espace entre la bannière et le prompt
    print("\033[94m" + prompt_text + "\033[0m", end='')
    sys.stdout.flush()  # Assure que le texte est affiché avant la saisie de l'utilisateur


def print_ip_info(ip_info):
    """Affiche les informations de l'IP en bleu clair."""
    if ip_info:
        # Couleur bleue claire pour le texte
        blue_light = (173, 216, 230)  # Bleu clair

        # Texte unicolore
        info_text = [
            "Informations sur l'IP :",
            "",  # Ligne vide pour l'espace
            f"Adresse IP: {ip_info.get('ip')}",
            f"Ville: {ip_info.get('city')}",
            f"Région: {ip_info.get('region')}",
            f"Pays: {ip_info.get('country')}",
            f"Organisation: {ip_info.get('org')}"
        ]

        # Application de la couleur bleue claire à tout le texte
        for line in info_text:
            print(generate_single_color_text(line, blue_light))
    else:
        print(generate_single_color_text("Aucune information disponible.", blue_light))

def clear_screen():
    """Efface l'écran en fonction du système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_continue_prompt():
    """Affiche la demande de continuation avec une couleur spécifique pour 'y' et 'n'."""
    prompt_text = "Voulez-vous effectuer une autre recherche ? ("
    prompt_text_colored = (
        f"\033[94m{prompt_text}\033[0m"  # Bleu clair pour le début du texte
        "\033[92my\033[0m"  # Vert pour 'y'
        "\033[94m/\033[0m"  # Bleu clair pour '/'
        "\033[91mn\033[0m"  # Rouge pour 'n'
        "\033[94m) : \033[0m"  # Bleu clair pour la fin du texte
    )
    print("\n")  # Ligne vide pour l'espace avant la demande de continuation
    print(prompt_text_colored, end='')
    sys.stdout.flush()  # Assure que le texte est affiché avant la saisie de l'utilisateur

def print_thank_you_message():
    """Affiche le message de remerciement en vert."""
    thank_you_text = "Merci d'avoir utilisé l'outil. À bientôt !"
    print("\n")  # Ligne vide pour l'espace avant le message de remerciement
    print("\033[92m" + thank_you_text + "\033[0m")

def main():
    clear_screen()
    print("\n")  # Ajoute une ligne vide
    print_banner()  # Affiche la bannière avec une couleur bleue claire

    while True:
        print_ip_request_prompt()  # Affiche le texte de demande d'IP en bleu clair
        ip_address = input()  # L'utilisateur entre l'adresse IP
        print()  # Ligne vide pour séparer l'input du reste de la sortie
        
        if not ip_address.strip():
            print(generate_single_color_text("L'adresse IP n'est pas valide. Veuillez réessayer.", (173, 216, 230)))
            continue

        ip_info = get_ip_info(ip_address)
        print_ip_info(ip_info)
        
        # Réduire l'espace entre les informations IP et la demande de continuation
        print("")  # Réduction de l'espace à une seule ligne vide


        # Demander à l'utilisateur s'il souhaite faire une autre recherche ou quitter
        print_continue_prompt()
        
        # Lire la réponse de l'utilisateur caractère par caractère
        while True:
            ch = msvcrt.getch().decode()  # Lire un caractère
            if ch.lower() == 'y':
                print("\033[92my\033[0m")  # Affiche 'y' en vert
                break
            elif ch.lower() == 'n':
                print("\033[91mn\033[0m")  # Affiche 'n' en rouge
                print_thank_you_message()  # Affiche le message de remerciement
                return  # Quitter le programme
            else:
                print("\033[91mEntrée invalide. Veuillez entrer 'y' ou 'n'.\033[0m", end='')

if __name__ == "__main__":
    main()
