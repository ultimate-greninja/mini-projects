import pandas as pd
import tkinter as tk
from tkinter import messagebox
import webbrowser  # Import the webbrowser module

# Load the CSV file into a DataFrame
file_path = "pokemon drawn.csv"  # Replace with the correct path to your CSV file
pokemon_data = pd.read_csv(file_path)

# Add a new column 'Drawn' with default value False if it doesn't exist
if 'Drawn' not in pokemon_data.columns:
    pokemon_data['Drawn'] = False

# Function to find a Pokemon
def findPokemon():
    # Check if there are any Pokemon without 'Drawn' being True
    undrawn_pokemon = pokemon_data[pokemon_data['Drawn'] == False]
    if undrawn_pokemon.empty:
        return ('No Pokemon available', 'Done')

    # Check if there's a Pokemon with 'Drawn' value as 'Current'
    current_pokemon = pokemon_data[pokemon_data['Drawn'] == 'Current']
    if current_pokemon.empty:
        random_pokemon = undrawn_pokemon.sample(1)
        return (random_pokemon.iloc[0], 'Not Done')
    else:
        if len(current_pokemon) > 1:
            print("Error: More than one Pokemon marked as 'Current'. Returning the first one. Others are", current_pokemon.iloc[1:])
        return (current_pokemon.iloc[0], 'Not Done')

# Function to handle marking a Pokemon as drawn
def mark_as_drawn(pokemon):
    pokemon_data.loc[pokemon_data['Name'] == pokemon['Name'], 'Drawn'] = True
    messagebox.showinfo("Marked as Drawn", f"{pokemon['Name']} has been marked as drawn.")
    find_and_display_pokemon()

# Function to find and display the next Pokemon
def find_and_display_pokemon():
    global draw_pokemon_loop
    pokemon, draw_pokemon_loop = findPokemon()
    if draw_pokemon_loop != 'Done':
        # Open a new tab with the Pokemon's name as a search query
        webbrowser.open(f"https://www.google.com/search?q={pokemon['Name']} art")
    no_button.config(command=find_and_display_pokemon)  # Update the skip button to generate a new Pokemon
    if draw_pokemon_loop == 'Done':
        messagebox.showinfo("All Done", "All Pokemon have been marked as drawn.")
        root.destroy()
        return

    # Update the label with the selected Pokemon and Number
    pokemon_label.config(text=f"Selected Pokemon: {pokemon['Name']}")
    dex_label.config(text=f"Number: {int(pokemon['Number'])}")  # Ensure Number is treated as a number
    yes_button.config(command=lambda: mark_as_drawn(pokemon))
    no_button.config(command=lambda: messagebox.showinfo("Not Marked", f"{pokemon['Name']} has not been marked as drawn."))

# Create the main tkinter window
root = tk.Tk()
root.title("Pokemon Checklist")

# Create and place widgets
pokemon_label = tk.Label(root, text="Selected Pokemon: ", font=("Arial", 16))
pokemon_label.pack(pady=20)

dex_label = tk.Label(root, text="Dex Number: ", font=("Arial", 14))
dex_label.pack(pady=10)

yes_button = tk.Button(root, text="Mark as Drawn", font=("Arial", 14))
yes_button.pack(side=tk.LEFT, padx=20, pady=20)

no_button = tk.Button(root, text="Skip", font=("Arial", 14))
no_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Start the process
find_and_display_pokemon()

# Run the tkinter main loop
root.mainloop()

