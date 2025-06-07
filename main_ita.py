# Software Name: Wikipedia Search
# Author: Bocaletto Luca
# Language: Italian
# Licenza: GPLv3

# Importa le librerie necessarie
import tkinter as tk
from tkinter import ttk
import wikipediaapi

# Imposta un user agent personalizzato per le richieste
user_agent = "MyWikipediaSearchApp/1.0 (YourEmailAddress@example.com)"

# Definisci una funzione per effettuare la ricerca nella Wikipedia
def search_wikipedia():
    query = entry.get()  # Ottieni la query dalla casella di testo
    selected_language = language_var.get()  # Ottieni la lingua selezionata
    language_mapping = {
        "Italiano": "it",
        "Inglese": "en",
        "Francese": "fr",
        "Spagnolo": "es",
        "Tedesco": "de",
        "Portoghese": "pt",
        "Olandese": "nl",
        "Arabo": "ar",
        "Cinese": "zh",
        "Giapponese": "ja",
        "Russo": "ru",
        "Rumeno": "ro",
        "Albanese": "sq"
    }
    selected_language_code = language_mapping.get(selected_language, "it")  # Ottieni il codice della lingua
    wiki_wiki = wikipediaapi.Wikipedia(
        language=selected_language_code,
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )
    page = wiki_wiki.page(query)
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, page.text)
    result_text.config(state='disabled')

# Inizializza la finestra principale dell'applicazione
root = tk.Tk()
root.title("Wikipedia Search")

# Aumenta la dimensione del carattere per l'etichetta del titolo
title_label = ttk.Label(root, text="Wikipedia Search", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Etichetta per la casella di testo di input
label = ttk.Label(root, text="Inserisci una parola e cerca su Wikipedia:", font=("Helvetica", 12))
label.grid(row=1, column=0, columnspan=2)

# Casella di testo per l'inserimento della query
entry = ttk.Entry(root, font=("Helvetica", 12))
entry.grid(row=2, column=0, columnspan=2)

# Menù a discesa per la selezione della lingua
language_var = tk.StringVar()
language_var.set("Inglese")  # Imposta l'inglese come lingua predefinita
languages = [
    "Italiano", "Inglese", "Francese", "Spagnolo", "Tedesco", "Portoghese",
    "Olandese", "Arabo", "Cinese", "Giapponese", "Russo", "Rumeno", "Albanese"
]
language_menu = ttk.OptionMenu(root, language_var, *languages)
language_menu.grid(row=3, column=0, columnspan=2)

# Bottone di ricerca
search_button = ttk.Button(root, text="Cerca", command=search_wikipedia)
search_button.grid(row=4, column=0, columnspan=2)

# Utilizza il layout a griglia per il widget result_text
result_text = tk.Text(root, height=20, width=40, state='disabled', font=("Helvetica", 12))
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configura la griglia per consentire il ridimensionamento del widget Text con la finestra
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

# Avvia l'applicazione
root.mainloop()
