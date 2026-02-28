"""from app import create_app
from app.routes.adresse_mac import verify_machine_guid
from app.utils import show_window

app = create_app()
if __name__=="__main__":
    if  not verify_machine_guid():
        show_window("Une erreur est survenue")
        print("401")
        exit()
    show_window("La ")
    app.run(host="127.0.0.1",
        port=5000,debug=True)"""

from app import create_app
import tkinter as tk
from threading import Thread
import sys

from app.utils import show_window

app = create_app()

def start_flask_server():
    """Fonction qui lance le serveur Flask"""
    print("Démarrage du serveur Flask sur http://127.0.0.1:5000")
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,          # Mettez True seulement en développement
        use_reloader=False,   # Très important : évite les problèmes avec Tkinter
        threaded=True         # Permet au serveur de répondre pendant que Tkinter tourne
    )

def show_window_and_control_app(message: str, title: str = "Information"):
    """
    Crée une fenêtre avec un label.
    Quand la fenêtre est fermée → arrête le serveur Flask et quitte le programme.
    """
    root = tk.Tk()
    root.title(title)
    root.geometry("400x200")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))  # Intercepte la fermeture

    label = tk.Label(
        root,
        text=message,
        font=("Helvetica", 12),
        wraplength=350,
        pady=50
    )
    label.pack(expand=True)

    def on_close(window):
        """Appelée quand l'utilisateur ferme la fenêtre"""
        print("Fenêtre fermée par l'utilisateur → arrêt du serveur et du programme.")
        window.destroy()                    # Ferme la fenêtre Tkinter
        # Flask n'a pas de méthode shutdown directe simple, donc on utilise sys.exit
        # Cela arrête proprement le thread principal
        sys.exit(0)

    # Lancer le serveur Flask dans un thread séparé
    flask_thread = Thread(target=start_flask_server, daemon=True)
    flask_thread.start()

    # Centrer la fenêtre
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")

    # Lancer la boucle principale Tkinter (bloque jusqu'à fermeture)
    root.mainloop()

    # Ce code ne s'exécute QUE si mainloop() se termine (c'est-à-dire fermeture)
    print("Programme terminé.")

if __name__ == "__main__":
    """if  not verify_machine_guid():
        show_window( "Accès refusé : cette copie n'est pas autorisée sur cette machine.")
        sys.exit(1)"""

    # Affichage de la fenêtre qui contrôle tout
    show_window_and_control_app(
        message="La base de données est prête.\n\nLe serveur local est en cours de démarrage...\n\n"
                "Fermez cette fenêtre pour arrêter l'application.",
        title="Application prête"
    )