# Software Name: Wikipedia Search
# Author: Bocaletto Luca
# Language: Dynamically Multilanguage (UI and page content)
# License: GPLv3

import tkinter as tk
from tkinter import ttk
import wikipediaapi
from googletrans import Translator  # Make sure to install googletrans

# Set a custom user agent for requests
user_agent = "MyWikipediaSearchApp/1.0 (YourEmailAddress@example.com)"

# Mapping for Wikipedia language codes based on language names
language_mapping = {
    "Italian": "it",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Arabic": "ar",
    "Chinese": "zh",
    "Japanese": "ja",
    "Russian": "ru",
    "Romanian": "ro",
    "Albanian": "sq"
}

# Dictionary containing UI texts in different languages
UI_TEXTS = {
    "Italian": {
        "title": "Ricerca su Wikipedia",
        "input_label": "Inserisci una parola e cerca su Wikipedia:",
        "search_button": "Cerca",
        "page_not_found": "Pagina non trovata."
    },
    "English": {
        "title": "Wikipedia Search",
        "input_label": "Enter a word and search on Wikipedia:",
        "search_button": "Search",
        "page_not_found": "Page not found."
    },
    "French": {
        "title": "Recherche sur Wikipedia",
        "input_label": "Entrez un mot et recherchez sur Wikipedia:",
        "search_button": "Recherche",
        "page_not_found": "Page non trouvée."
    },
    "Spanish": {
        "title": "Búsqueda en Wikipedia",
        "input_label": "Introduce una palabra y busca en Wikipedia:",
        "search_button": "Buscar",
        "page_not_found": "Página no encontrada."
    },
    "German": {
        "title": "Wikipedia Suche",
        "input_label": "Geben Sie ein Wort ein und suchen Sie in Wikipedia:",
        "search_button": "Suche",
        "page_not_found": "Seite nicht gefunden."
    },
    "Portuguese": {
        "title": "Pesquisa na Wikipedia",
        "input_label": "Insira uma palavra e pesquise na Wikipedia:",
        "search_button": "Pesquisar",
        "page_not_found": "Página não encontrada."
    },
    "Dutch": {
        "title": "Wikipedia Zoeken",
        "input_label": "Voer een woord in en zoek op Wikipedia:",
        "search_button": "Zoeken",
        "page_not_found": "Pagina niet gevonden."
    },
    "Arabic": {
        "title": "بحث ويكيبيديا",
        "input_label": "أدخل كلمة وابحث في ويكيبيديا:",
        "search_button": "ابحث",
        "page_not_found": "الصفحة غير موجودة."
    },
    "Chinese": {
        "title": "维基百科搜索",
        "input_label": "输入一个词并在维基百科中搜索:",
        "search_button": "搜索",
        "page_not_found": "未找到页面。"
    },
    "Japanese": {
        "title": "ウィキペディア検索",
        "input_label": "単語を入力してウィキペディアを検索:",
        "search_button": "検索",
        "page_not_found": "ページが見つかりません。"
    },
    "Russian": {
        "title": "Поиск по Википедии",
        "input_label": "Введите слово и выполните поиск в Википедии:",
        "search_button": "Поиск",
        "page_not_found": "Страница не найдена."
    },
    "Romanian": {
        "title": "Căutare pe Wikipedia",
        "input_label": "Introduceți un cuvânt și căutați pe Wikipedia:",
        "search_button": "Caută",
        "page_not_found": "Pagina nu a fost găsită."
    },
    "Albanian": {
        "title": "Kërkim në Wikipedia",
        "input_label": "Fut një fjalë dhe kërko në Wikipedia:",
        "search_button": "Kërko",
        "page_not_found": "Faqja nuk u gjend."
    }
}

# Initialize the main application window
root = tk.Tk()

# Create UI elements; their text values will be updated dynamically
title_label = ttk.Label(root, font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

label = ttk.Label(root, font=("Helvetica", 12))
label.grid(row=1, column=0, columnspan=2)

# Input text box for the search query
entry = ttk.Entry(root, font=("Helvetica", 12))
entry.grid(row=2, column=0, columnspan=2)

# Tkinter variable for language; its value will control both UI and Wikipedia API language
language_var = tk.StringVar()
language_var.set("English")  # Default language

# Dropdown menu for language selection
languages = list(language_mapping.keys())  # Using keys from language_mapping
language_menu = ttk.OptionMenu(root, language_var, language_var.get(), *languages)
language_menu.grid(row=3, column=0, columnspan=2)

# Search button (its text will be updated dynamically)
search_button = ttk.Button(root, command=lambda: search_wikipedia())
search_button.grid(row=4, column=0, columnspan=2)

# Text widget to display the Wikipedia page text
result_text = tk.Text(root, height=20, width=40, state='disabled', font=("Helvetica", 12))
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Expand the text widget as the window is resized
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

def update_ui_text(*args):
    """
    Update UI labels based on the selected language.
    """
    selected_lang = language_var.get()
    texts = UI_TEXTS.get(selected_lang, UI_TEXTS["English"])
    root.title(texts["title"])
    title_label.config(text=texts["title"])
    label.config(text=texts["input_label"])
    search_button.config(text=texts["search_button"])

# Attach a callback to update UI elements whenever the selected language changes
language_var.trace("w", update_ui_text)
update_ui_text()

def search_wikipedia():
    """
    Searches for the input query on Wikipedia using the selected language.
    If the page is not found in that language, attempts a fallback by fetching the
    Italian version and translating its content to the selected language.
    """
    query = entry.get().strip()
    selected_language = language_var.get()
    selected_language_code = language_mapping.get(selected_language, "en")
    
    # Create a Wikipedia API instance for the selected language
    wiki_obj = wikipediaapi.Wikipedia(
        language=selected_language_code,
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )
    page = wiki_obj.page(query)
    
    # If the page exists and has text, display it directly
    if page.exists() and page.text.strip() != "":
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, page.text)
        result_text.config(state='disabled')
    else:
        # Fallback: Try the Italian version of the page
        fallback_lang = "Italian"
        fallback_lang_code = language_mapping.get(fallback_lang, "it")
        fallback_wiki = wikipediaapi.Wikipedia(
            language=fallback_lang_code,
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent=user_agent
        )
        fallback_page = fallback_wiki.page(query)
        if fallback_page.exists() and fallback_page.text.strip() != "":
            translator = Translator()
            try:
                # Translate the fallback (Italian) page text into the selected language
                translated_text = translator.translate(
                    fallback_page.text, src=fallback_lang_code, dest=selected_language_code
                ).text
            except Exception as e:
                translated_text = fallback_page.text  # If translation fails, use the Italian version
            result_text.config(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, translated_text)
            result_text.config(state='disabled')
        else:
            # If no page is found, display "page not found" in the appropriate language
            texts = UI_TEXTS.get(selected_language, UI_TEXTS["English"])
            result_text.config(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, texts["page_not_found"])
            result_text.config(state='disabled')

# Run the application
root.mainloop()
