# Software Name: Wikipedia Search
# Author: Bocaletto Luca
# Language: English
# License: GPLv3

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
import wikipediaapi

# Set a custom user agent for requests
user_agent = "MyWikipediaSearchApp/1.0 (YourEmailAddress@example.com)"

# Define a function to perform a Wikipedia search
def search_wikipedia():
    query = entry.get()  # Get the query from the text box
    selected_language = language_var.get()  # Get the selected language
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
    selected_language_code = language_mapping.get(selected_language, "en")  # Get the language code (default is English)
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

# Initialize the main application window
root = tk.Tk()
root.title("Wikipedia Search")

# Increase the font size for the title label
title_label = ttk.Label(root, text="Wikipedia Search", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Label for the input text box
label = ttk.Label(root, text="Enter a word and search on Wikipedia:", font=("Helvetica", 12))
label.grid(row=1, column=0, columnspan=2)

# Text box for query input
entry = ttk.Entry(root, font=("Helvetica", 12))
entry.grid(row=2, column=0, columnspan=2)

# Dropdown menu for language selection
language_var = tk.StringVar()
language_var.set("English")  # Set English as the default language
languages = [
    "Italian", "English", "French", "Spanish", "German", "Portuguese",
    "Dutch", "Arabic", "Chinese", "Japanese", "Russian", "Romanian", "Albanian"
]
language_menu = ttk.OptionMenu(root, language_var, *languages)
language_menu.grid(row=3, column=0, columnspan=2)

# Search button
search_button = ttk.Button(root, text="Search", command=search_wikipedia)
search_button.grid(row=4, column=0, columnspan=2)

# Use grid layout for the result_text widget
result_text = tk.Text(root, height=20, width=40, state='disabled', font=("Helvetica", 12))
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configure the grid to allow the Text widget to expand with the window
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the application
root.mainloop()
