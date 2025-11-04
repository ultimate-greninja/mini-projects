import pandas as pd

pokemon = pd.read_csv("pokemon.csv")
pd.options.display.max_rows = 99999


def sorting(pokemon):
  pokemon = pokemon.sort_values(by="Dex Number")
  pokemon.to_csv("pokemon.csv", index=False)


def defence_weakness(
  pokemon_type_1, pokemon_type_2
):  #Normal,Fire,Water,Grass,Flying,Fighting,Poison,Electric,Ground,Rock,Psychic,Ice,Bug,Ghost,Steel,Dragon,Dark,Fairy
  weakness = []
  multiplier = {
    "Normal": 1,
    "Fire": 1,
    "Water": 1,
    "Grass": 1,
    "Flying": 1,
    "Fighting": 1,
    "Poison": 1,
    "Electric": 1,
    "Ground": 1,
    "Rock": 1,
    "Psychic": 1,
    "Ice": 1,
    "Bug": 1,
    "Ghost": 1,
    "Steel": 1,
    "Dragon": 1,
    "Dark": 1,
    "Fairy": 1
  }
  types = [
    "Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison",
    "Electric", "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel",
    "Dragon", "Dark", "Fairy"
  ]
  if pokemon_type_1 == "normal":
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
  elif pokemon_type_1 == "fire":
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "water":
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "grass":  #Bug, Fire, Flying, Ice, Poison
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
  elif pokemon_type_1 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_1 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Phychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "electric":  #
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "ground":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 5
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "rock":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_1 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_1 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Fighting"] = multiplier["Fighting"] - 5
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_1 == "steel":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 5
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "dragon":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 5
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "fairy":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 5
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1


#copy above but type 2
  if pokemon_type_2 == "normal":
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
  elif pokemon_type_2 == "fire":
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "water":
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "grass":  #Bug, Fire, Flying, Ice, Poison
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
  elif pokemon_type_2 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_2 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "electric":  #
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "ground":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 5
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "rock":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_2 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_2 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Fighting"] = multiplier["Fighting"] - 5
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_2 == "steel":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 5
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "dragon":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 5
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "fairy":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 5
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  check = 0
  for register in types:
    effect = ("(x2)")
    if multiplier[register] > 1:
      if multiplier[register] > 2:
        effect = ("(x4)")
      weak = register + effect
      weakness.append(weak)
      check = check + 1
  if check == 0:
    weakness = "None"
  weakness = "/".join(weakness)
  return (weakness)


def defence_strength(
  pokemon_type_1, pokemon_type_2
):  #Normal,Fire,Water,Grass,Flying,Fighting,Poison,Electric,Ground,Rock,Psychic,Ice,Bug,Ghost,Steel,Dragon,Dark,Fairy
  strength = []
  multiplier = {
    "Normal": 1,
    "Fire": 1,
    "Water": 1,
    "Grass": 1,
    "Flying": 1,
    "Fighting": 1,
    "Poison": 1,
    "Electric": 1,
    "Ground": 1,
    "Rock": 1,
    "Psychic": 1,
    "Ice": 1,
    "Bug": 1,
    "Ghost": 1,
    "Steel": 1,
    "Dragon": 1,
    "Dark": 1,
    "Fairy": 1
  }
  types = [
    "Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison",
    "Electric", "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel",
    "Dragon", "Dark", "Fairy"
  ]
  if pokemon_type_1 == "normal":
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
  elif pokemon_type_1 == "fire":
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "water":
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "grass":  #Bug, Fire, Flying, Ice, Poison
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
  elif pokemon_type_1 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_1 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Phychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "electric":  #
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "ground":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 5
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "rock":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_1 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_1 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Fighting"] = multiplier["Fighting"] - 5
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_1 == "steel":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 5
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "dragon":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 5
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "fairy":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 5
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
#copy above but type 2
  if pokemon_type_2 == "normal":
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
  elif pokemon_type_2 == "fire":
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "water":
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "grass":  #Bug, Fire, Flying, Ice, Poison
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
  elif pokemon_type_2 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_2 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "electric":  #
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "ground":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 5
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "rock":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_2 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
  elif pokemon_type_2 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Fighting"] = multiplier["Fighting"] - 5
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
  elif pokemon_type_2 == "steel":  #
    multiplier["Normal"] = multiplier["Normal"] - 1
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 5
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "dragon":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 5
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "fairy":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 5
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  check = 0
  for register in types:
    effect = ("(x1/2)")
    if multiplier[register] < 1:
      if multiplier[register] < 0:
        effect = ("(x1/4)")
        if multiplier[register] < -2:
          effect = ("(x0)")
      strong = (register + effect)
      strength.append(strong)
      check = check + 1
  if check == 0:
    strength = "None"
  strength = "/".join(strength)
  return (strength)


#can use for moves might not be useful for data base but could use for attacks keep in may be useful
#                        |
#                        V
def attack_weakness(pokemon_type_1, pokemon_type_2):
  weakness = []
  multiplier = {
    "Normal": 1,
    "Fire": 1,
    "Water": 1,
    "Grass": 1,
    "Flying": 1,
    "Fighting": 1,
    "Poison": 1,
    "Electric": 1,
    "Ground": 1,
    "Rock": 1,
    "Psychic": 1,
    "Ice": 1,
    "Bug": 1,
    "Ghost": 1,
    "Steel": 1,
    "Dragon": 1,
    "Dark": 1,
    "Fairy": 1
  }
  types = [
    "Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison",
    "Electric", "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel",
    "Dragon", "Dark", "Fairy"
  ]
  if pokemon_type_1 == "normal":
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "fire":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "water":
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_1 == "grass":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Normal"] = multiplier["Normal"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 5
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "electric":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_1 == "ground":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "rock":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
  elif pokemon_type_1 == "steel":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "dragon":  #
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 5
  elif pokemon_type_1 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "fairy":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "normal":
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "fire":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "water":
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_2 == "grass":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Normal"] = multiplier["Normal"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Pyschic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 5
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "electric":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_2 == "ground":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "rock":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
  elif pokemon_type_2 == "steel":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "dragon":  #
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 5
  elif pokemon_type_2 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "fairy":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  check = 0
  for register in types:
    effect = ("(x1/2)")
    if multiplier[register] < 1:
      if multiplier[register] < 0:
        effect = ("(x1/4)")
        if multiplier[register] < -2:
          effect = ("(x0)")
      weak = register + effect
      weakness.append(weak)
      check = check + 1
  if check == 0:
    weakness = "None"
  weakness = "/".join(weakness)
  return (weakness)


def attack_strength(pokemon_type_1, pokemon_type_2):
  weakness = []
  multiplier = {
    "Normal": 1,
    "Fire": 1,
    "Water": 1,
    "Grass": 1,
    "Flying": 1,
    "Fighting": 1,
    "Poison": 1,
    "Electric": 1,
    "Ground": 1,
    "Rock": 1,
    "Psychic": 1,
    "Ice": 1,
    "Bug": 1,
    "Ghost": 1,
    "Steel": 1,
    "Dragon": 1,
    "Dark": 1,
    "Fairy": 1
  }
  types = [
    "Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison",
    "Electric", "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel",
    "Dragon", "Dark", "Fairy"
  ]
  if pokemon_type_1 == "normal":
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "fire":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "water":
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_1 == "grass":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Normal"] = multiplier["Normal"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 5
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "electric":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_1 == "ground":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_1 == "rock":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_1 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
  elif pokemon_type_1 == "steel":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_1 == "dragon":  #
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 5
  elif pokemon_type_1 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_1 == "fairy":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "normal":
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "fire":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "water":
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_2 == "grass":
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "flying":  #Electric, Ice, Rock
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "fighting":  #Fairy, Flying, Psychic
    multiplier["Normal"] = multiplier["Normal"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Pyschic"] - 1
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 5
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "poison":  #
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Rock"] = multiplier["Rock"] - 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Steel"] = multiplier["Steel"] - 5
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "electric":  #
    multiplier["Water"] = multiplier["Water"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 5
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] - 1
  elif pokemon_type_2 == "ground":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Grass"] = multiplier["Grass"] - 1
    multiplier["Electric"] = multiplier["Electric"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Flying"] = multiplier["Flying"] - 5
    multiplier["Bug"] = multiplier["Bug"] - 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] + 1
  elif pokemon_type_2 == "rock":  #
    multiplier["Fire"] = multiplier["Fire"] + 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Ground"] = multiplier["Ground"] - 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Bug"] = multiplier["Bug"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "psychic":  #
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] + 1
    multiplier["Psychic"] = multiplier["Psychic"] - 1
    multiplier["Dark"] = multiplier["Dark"] - 5
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "ice":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Ice"] = multiplier["Ice"] - 1
    multiplier["Ground"] = multiplier["Ground"] + 1
    multiplier["Flying"] = multiplier["Flying"] + 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  elif pokemon_type_2 == "bug":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Grass"] = multiplier["Grass"] + 1
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Flying"] = multiplier["Flying"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] - 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "ghost":  #
    multiplier["Normal"] = multiplier["Normal"] - 5
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
  elif pokemon_type_2 == "steel":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Water"] = multiplier["Water"] - 1
    multiplier["Electric"] = multiplier["Electric"] - 1
    multiplier["Ice"] = multiplier["Ice"] + 1
    multiplier["Rock"] = multiplier["Rock"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] + 1
  elif pokemon_type_2 == "dragon":  #
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 5
  elif pokemon_type_2 == "dark":  #
    multiplier["Fighting"] = multiplier["Fighting"] - 1
    multiplier["Psychic"] = multiplier["Psychic"] + 1
    multiplier["Ghost"] = multiplier["Ghost"] + 1
    multiplier["Dark"] = multiplier["Dark"] - 1
    multiplier["Fairy"] = multiplier["Fairy"] - 1
  elif pokemon_type_2 == "fairy":  #
    multiplier["Fire"] = multiplier["Fire"] - 1
    multiplier["Fighting"] = multiplier["Fighting"] + 1
    multiplier["Poison"] = multiplier["Poison"] - 1
    multiplier["Dragon"] = multiplier["Dragon"] + 1
    multiplier["Dark"] = multiplier["Dark"] + 1
    multiplier["Steel"] = multiplier["Steel"] - 1
  check = 0
  for register in types:
    effect = ("(x2)")
    if multiplier[register] > 1:
      if multiplier[register] > 2:
        effect = ("(x4)")
      weak = register + effect
      weakness.append(weak)
      check = check + 1
  if check == 0:
    weakness = "None"
  weakness = "/".join(weakness)
  return (weakness)
  check = 0


def pokedex():
  pokemon_dex = (0)
  import pandas as pd
  pokemon = pd.read_csv("pokemon.csv")
  pokemon_evolve_method = "N/A"
  while pokemon_dex == 0:
    try:
      pokemon_dex = int(input("National Dex Number: "))
    except:
      print("invalid")
  pokemon_name = input("name: ").lower()
  pokemon_name = pokemon_name.split(" ")
  for i in range(len(pokemon_name)):
    pokemon_name[i] = " ".join(word.capitalize()
                               for word in pokemon_name[i].split())
  pokemon_name = " ".join(pokemon_name)
  pokemon_type_1 = input("type 1: ").lower()
  pokemon_type_2 = input("type 2: ").lower()  # if none just put N/A
  pokemon_ability = input("abilities: ")  # / in between
  pokemon_ability = pokemon_ability.split("/")
  for i in range(len(pokemon_ability)):
    pokemon_ability[i] = " ".join(word.capitalize()
                                  for word in pokemon_ability[i].split())
  pokemon_ability = "/".join(pokemon_ability)
  pokemon_region = input("region: ")
  pokemon_region = pokemon_region.split("/")
  for i in range(len(pokemon_region)):
    pokemon_region[i] = "/".join(word.capitalize()
                                 for word in pokemon_region[i].split())
  pokemon_region = "/".join(pokemon_region)
  pokemon_base_hp = None
  while pokemon_base_hp is None:
    try:
      pokemon_base_hp = int(input("base HP: "))  ###########
    except:
      print("invalid")
  pokemon_base_attack = None
  while pokemon_base_attack is None:
    try:
      pokemon_base_attack = int(input("base Attack: "))
    except:
      print("invalid")
  pokemon_base_Defence = None
  while pokemon_base_Defence is None:
    try:
      pokemon_base_Defence = int(input("base Defence: "))
    except:
      print("invalid")
  pokemon_base_SPattack = None
  while pokemon_base_SPattack is None:
    try:
      pokemon_base_SPattack = int(input("base SP.Attack: "))
    except:
      print("invalid")
  pokemon_base_SPDefence = None
  while pokemon_base_SPDefence is None:
    try:
      pokemon_base_SPDefence = int(input("base SP.Defence: "))
    except:
      print("invalid")
  pokemon_base_speed = None
  while pokemon_base_speed is None:
    try:
      pokemon_base_speed = int(input("base Speed: "))
    except:
      print("invalid")
  pokemon_base_total = pokemon_base_hp + pokemon_base_attack + pokemon_base_Defence + pokemon_base_SPattack + pokemon_base_SPDefence + pokemon_base_speed
  pokemon_mega = input("can they Mega Evolve: ")
  while pokemon_mega[0].upper() != "Y" and pokemon_mega[0].upper() != "N":
    print("invalid")
    pokemon_mega = input("can they Mega Evolve: ")
  if pokemon_mega[0].upper() == "Y":
    pokemon_mega = "Yes"
  elif pokemon_mega[0].upper() == "N":
    pokemon_mega = "No"
  pokemon_evolution = input("can they evolve: ")
  while pokemon_evolution[0].upper() != "Y" and pokemon_evolution[0].upper(
  ) != "N":
    print("invalid")
    pokemon_evolution = input("can they evolve: ")
  if pokemon_evolution[0].upper() == "Y":
    pokemon_evolution = input("what does it evolve into: ")
    pokemon_evolution = pokemon_evolution.split("/")
    for i in range(len(pokemon_evolution)):
      pokemon_evolution[i] = " ".join(word.capitalize()
                                      for word in pokemon_evolution[i].split())
    pokemon_evolution = "/".join(pokemon_evolution)
    pokemon_evolve_method = input("how do they evolve: ")
    pokemon_evolve_method = pokemon_evolve_method.split("/")
    for i in range(len(pokemon_evolve_method)):
      pokemon_evolve_method[i] = " ".join(
        word.capitalize() for word in pokemon_evolve_method[i].split())
    pokemon_evolve_method = "/".join(pokemon_evolve_method)
  elif pokemon_evolution[0].upper() == "N":
    pokemon_evolution = "None"
  pokemon_defence_weakness = defence_weakness(pokemon_type_1, pokemon_type_2)
  pokemon_defence_strength = defence_strength(pokemon_type_1, pokemon_type_2)
  pokemon_attack_weakness = attack_weakness(pokemon_type_1, pokemon_type_2)
  pokemon_attack_strength = attack_strength(pokemon_type_1, pokemon_type_2)
  pokemon_type_2 = pokemon_type_2.capitalize()
  if pokemon_defence_weakness == "N/o/n/e":
    pokemon_defence_weakness = "None"
  if pokemon_defence_strength == "N/o/n/e":
    pokemon_defence_strength = "None"
  if pokemon_attack_strength == "N/o/n/e":
    pokemon_attack_strength = "None"
  if pokemon_attack_weakness == "N/o/n/e":
    pokemon_attack_weakness = "None"
  if pokemon_type_2.upper() == "N":
    pokemon_type_2 = "N/A"
  if pokemon_type_2.capitalize() == "Normal":
    pokemon_type_2 = "Normal"
  new_pokemon = pd.DataFrame({
    "Dex Number": [pokemon_dex],
    "Name": [pokemon_name],
    "Type 1": [pokemon_type_1.capitalize()],
    "Type 2": [pokemon_type_2],
    "Defence_Weakness": [pokemon_defence_weakness],
    "Defence_Strength": [pokemon_defence_strength],
    "Attack_Weakness": [pokemon_attack_weakness],
    "Attack_Strength": [pokemon_attack_strength],
    "Ability": [pokemon_ability],
    "Base Total": [pokemon_base_total],
    "Base HP": [pokemon_base_hp],
    "Base Attack": [pokemon_base_attack],
    "Base Defence": [pokemon_base_Defence],
    "Base SP.Attack": [pokemon_base_SPattack],
    "Base SP.Defence": [pokemon_base_SPDefence],
    "Base Speed": [pokemon_base_speed],
    "Region": [pokemon_region],
    "Mega_Evolve": [pokemon_mega],
    "Evolution": [pokemon_evolution],
    "How_They_Evolve": [pokemon_evolve_method]
  })
  pokemon = pd.concat([pokemon, new_pokemon], ignore_index=True)

  pokemon.to_csv("pokemon.csv", index=False)


while True:
  lock = input("put quit to stop ")
  #lock = "quit"
  if lock.upper() == "QUIT":
    break
  pokedex()


def mega_checker(pokemon):
  for i in range(len(pokemon["Mega_Evolve"])):
    if pokemon["Mega_Evolve"][i][0] == "Y":
      print("")
      print("Dex:", pokemon["Dex Number"][i])
      print("Name:", pokemon["Name"][i])
      print("Evolution:", pokemon["Evolution"][i])
      print("Mega:", pokemon["Mega_Evolve"][i])


#mega_checker(pokemon)
def evolution_checker(pokemon):
  for i in range(len(pokemon["Evolution"])):
    if pokemon["Evolution"][i] != "N/A":
      print("")
      print("Dex:", pokemon["Dex Number"][i])
      print("Name:", pokemon["Name"][i])
      print("Type 1:", pokemon["Type 1"][i])
      print("Type 2:", pokemon["Type 2"][i])
      print("Evolution:", pokemon["Evolution"][i])


#evolution_checker(pokemon)
def NotApplicable(pokemon):
  pokemon.fillna("N/A", inplace=True)
  #print(pokemon)
  pokemon.to_csv("pokemon.csv", index=False)


#NotApplicable(pokemon)
def megachoice(pokemon, region):
  print("")
  for i in range(len(pokemon["Name"])):
    ability_list = pokemon["Ability"][i].split("/")
    if pokemon["Name"][i][0:4] == "Mega":
      print("Dex:", pokemon["Dex Number"][i])
      print("Name:", pokemon["Name"][i])
      if pd.isnull(pokemon["Type 2"][i]) == False:
        print("Typing:", pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
      elif pd.isnull(pokemon["Type 2"][i]):
        print("Typing:", pokemon["Type 1"][i])
      print("Abilities:", (" / ".join(ability_list)))
      print("--BASE STATS--")
      print("Total:", pokemon["Base Total"][i])
      print("Total:", pokemon["Base HP"][i])
      print("Total:", pokemon["Base Attack"][i])
      print("Total:", pokemon["Base Defence"][i])
      print("Total:", pokemon["Base SP.Attack"][i])
      print("Total:", pokemon["Base SP.Defence"][i])
      print("Total:", pokemon["Base Speed"][i])
      print("--BASE STATS--")
      print("")


def mega_search(pokemon, region):
  search_choice = input(
    "what would you like to search by? (dex,name,type,ability) ")
  print(" ")

  def mega_dex_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    try:
      dex = int(input("National Dex Number: "))
    except:
      dex = ("invalid")
    print("")
    for i in range(len(pokemon["Dex Number"])):
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      ability_list = pokemon["Ability"][i].split("/")
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          if pokemon["Dex Number"][i] == dex:
            if pokemon["Name"][i][0:4] == "Mega":
              if pokemon["Name"][i] not in printed_pokemon:
                printed_pokemon.append(pokemon["Name"][i])
                print("Dex:", pokemon["Dex Number"][i])
                print("Name:", pokemon["Name"][i])
                if pd.isnull(pokemon["Type 2"][i]) == False:
                  print("Typing:",
                        pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
                elif pd.isnull(pokemon["Type 2"][i]):
                  print("Typing:", pokemon["Type 1"][i])
                print("Abilities:", (" / ".join(ability_list)))
                print("Strong against:", pokemon["Defence_Strength"][i])
                print("Weak to:", pokemon["Defence_Weakness"][i])
                print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
                if pokemon["Evolution"][i] == "None":
                  print("Evolution:", pokemon["Evolution"][i])
                elif pokemon["Evolution"][i] != "None":
                  print("Evolution:", pokemon["Evolution"][i],
                        pokemon["How_They_Evolve"][i])
                print("--BASE STATS--")
                print("Total:", pokemon["Base Total"][i])
                print("HP:", pokemon["Base HP"][i])
                print("Attack:", pokemon["Base Attack"][i])
                print("Defence:", pokemon["Base Defence"][i])
                print("SP.Attack:", pokemon["Base SP.Attack"][i])
                print("SP.Defence:", pokemon["Base SP.Defence"][i])
                print("Speed:", pokemon["Base Speed"][i])
                print("--BASE STATS--")
                print("")
                lock = 0
                counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  def mega_name_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    name = input("Name: ")
    name = name.split(" ")
    for cap in range(len(name)):
      name[cap] = name[cap].capitalize()
    name = " ".join(name)
    print("")
    for i in range(len(pokemon["Name"])):
      ability_list = pokemon["Ability"][i].split("/")
      if pokemon["Name"][i] == name:
        pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
        pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
        pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
        pokemon_defence_strength = pokemon["Defence_Strength"][i]
        pokemon_defence_strength = pokemon_defence_strength.split(")/")
        pokemon_defence_strength = "),".join(
          pokemon_defence_strength)  #--here--
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          if pokemon["Name"][i][0:4] == "Mega":
            if pokemon["Name"][i] not in printed_pokemon:
              printed_pokemon.append(pokemon["Name"][i])
              print("Dex:", pokemon["Dex Number"][i])
              print("Name:", pokemon["Name"][i])
              if pd.isnull(pokemon["Type 2"][i]) == False:
                print("Typing:",
                      pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
              elif pd.isnull(pokemon["Type 2"][i]):
                print("Typing:", pokemon["Type 1"][i])
              print("Strong against:", pokemon["Defence_Strength"][i])
              print("Weak to:", pokemon["Defence_Weakness"][i])
              print("Abilities:", (" / ".join(ability_list)))
              print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
              if pokemon["Evolution"][i] == "None":
                print("Evolution:", pokemon["Evolution"][i])
              elif pokemon["Evolution"][i] != "None":
                print("Evolution:", pokemon["Evolution"][i],
                      pokemon["How_They_Evolve"][i])
              print("--BASE STATS--")
              print("Total:", pokemon["Base Total"][i])
              print("HP:", pokemon["Base HP"][i])
              print("Attack:", pokemon["Base Attack"][i])
              print("Defence:", pokemon["Base Defence"][i])
              print("SP.Attack:", pokemon["Base SP.Attack"][i])
              print("SP.Defence:", pokemon["Base SP.Defence"][i])
              print("Speed:", pokemon["Base Speed"][i])
              print("--BASE STATS--")
              print("")
              lock = 0
              counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  def mega_type_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    types = input("Types: ")
    print("")
    types = types.split("/")
    for l in range(len(types)):
      types[l] = types[l].capitalize()
    for i in range(len(pokemon["Type 1"])):
      ability_list = pokemon["Ability"][i].split("/")
      counter = 0
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      for c in range(len(types)):
        if pokemon["Type 1"][i] == types[c] or pokemon["Type 2"][i] == types[c]:
          counter = counter + 1
          if pd.isnull(pokemon["Type 2"][i]):
            counter = counter + 1
        if counter == 2:
          pokemon_region = pokemon["Region"][i].split("/")
          for loop in range(len(pokemon_region)):
            lock = 0
            if region == pokemon_region[loop]:
              lock = lock + 1
            elif region == "None":
              lock = lock + 1
            if lock == 1:
              if pokemon["Name"][i][0:4] == "Mega":
                if pokemon["Name"][i] not in printed_pokemon:
                  printed_pokemon.append(pokemon["Name"][i])
                  print("Dex:", pokemon["Dex Number"][i])
                  print("Name:", pokemon["Name"][i])
                  if pd.isnull(pokemon["Type 2"][i]) == False:
                    print("Typing:",
                          pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
                  elif pd.isnull(pokemon["Type 2"][i]):
                    print("Typing:", pokemon["Type 1"][i])
                  print("Abilities:", (" / ".join(ability_list)))
                  print("Strong against:", pokemon["Defence_Strength"][i])
                  print("Weak to:", pokemon["Defence_Weakness"][i])
                  print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
                  if pokemon["Evolution"][i] == "None":
                    print("Evolution:", pokemon["Evolution"][i])
                  elif pokemon["Evolution"][i] != "None":
                    print("Evolution:", pokemon["Evolution"][i],
                          pokemon["How_They_Evolve"][i])
                  print("--BASE STATS--")
                  print("Total:", pokemon["Base Total"][i])
                  print("HP:", pokemon["Base HP"][i])
                  print("Attack:", pokemon["Base Attack"][i])
                  print("Defence:", pokemon["Base Defence"][i])
                  print("SP.Attack:", pokemon["Base SP.Attack"][i])
                  print("SP.Defence:", pokemon["Base SP.Defence"][i])
                  print("Speed:", pokemon["Base Speed"][i])
                  print("--BASE STATS--")
                  print("")
                  lock = 0
                  counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  def mega_ability_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    abilities = input("ability: ")
    abilities = abilities.split(" ")
    for cap in range(len(abilities)):
      abilities[cap] = abilities[cap].capitalize()
    abilities = " ".join(abilities)
    print("")
    for i in range(len(pokemon["Name"])):
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      ability_list = pokemon["Ability"][i].split("/")
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          for l in range(len(ability_list)):
            if abilities == ability_list[l]:
              if pokemon["Name"][i][0:4] == "Mega":
                if pokemon["Name"][i] not in printed_pokemon:
                  printed_pokemon.append(pokemon["Name"][i])
                  print("Dex:", pokemon["Dex Number"][i])
                  print("Name:", pokemon["Name"][i])
                  if pd.isnull(pokemon["Type 2"][i]) == False:
                    print("Typing:",
                          pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
                  elif pd.isnull(pokemon["Type 2"][i]):
                    print("Typing:", pokemon["Type 1"][i])
                  print("Abilities:", (" / ".join(ability_list)))
                  print("Strong against:", pokemon["Defence_Strength"][i])
                  print("Weak to:", pokemon["Defence_Weakness"][i])
                  print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
                  if pokemon["Evolution"][i] == "None":
                    print("Evolution:", pokemon["Evolution"][i])
                  elif pokemon["Evolution"][i] != "None":
                    print("Evolution:", (pokemon["Evolution"][i]),
                          pokemon["How_They_Evolve"][i])
                  print("--BASE STATS--")
                  print("Total:", pokemon["Base Total"][i])
                  print("HP:", pokemon["Base HP"][i])
                  print("Attack:", pokemon["Base Attack"][i])
                  print("Defence:", pokemon["Base Defence"][i])
                  print("SP.Attack:", pokemon["Base SP.Attack"][i])
                  print("SP.Defence:", pokemon["Base SP.Defence"][i])
                  print("Speed:", pokemon["Base Speed"][i])
                  print("--BASE STATS--")
                  print("")
                  lock = 0
                  counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  if search_choice[0].lower() == "d":
    mega_dex_search(pokemon, region)
  elif search_choice[0].lower() == "n":
    mega_name_search(pokemon, region)
  elif search_choice[0].lower() == "t":
    mega_type_search(pokemon, region)
  elif search_choice[0].lower() == "a":
    mega_ability_search(pokemon, region)
  else:
    print("invalid")


def search(pokemon, region):
  search_choice = input(
    "what would you like to search by? (dex,name,type,ability) ")
  print("")

  def dex_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    try:
      dex = int(input("National Dex Number: "))
    except:
      dex = ("invalid")
    print("")
    for i in range(len(pokemon["Dex Number"])):
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      ability_list = pokemon["Ability"][i].split("/")
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          if pokemon["Dex Number"][i] == dex:  #
            if pokemon["Name"][i][0:4] != "Mega":
              if pokemon["Name"][i] not in printed_pokemon:
                printed_pokemon.append(pokemon["Name"][i])
              print("Dex:", pokemon["Dex Number"][i])
              print("Name:", pokemon["Name"][i])
              if pd.isnull(pokemon["Type 2"][i]) == False:
                print("Typing:",
                      pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
              elif pd.isnull(pokemon["Type 2"][i]):
                print("Typing:", pokemon["Type 1"][i])
              print("Abilities:", (" / ".join(ability_list)))
              print("Strong against:", pokemon["Defence_Strength"][i])
              print("Weak to:", pokemon["Defence_Weakness"][i])
              print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
              if pokemon["Evolution"][i] == "None":
                print("Evolution:", pokemon["Evolution"][i])
              elif pokemon["Evolution"][i] != "None":
                print("Evolution:", pokemon["Evolution"][i],
                      pokemon["How_They_Evolve"][i])
              print("--BASE STATS--")
              print("Total:", pokemon["Base Total"][i])
              print("HP:", pokemon["Base HP"][i])
              print("Attack:", pokemon["Base Attack"][i])
              print("Defence:", pokemon["Base Defence"][i])
              print("SP.Attack:", pokemon["Base SP.Attack"][i])
              print("SP.Defence:", pokemon["Base SP.Defence"][i])
              print("Speed:", pokemon["Base Speed"][i])
              print("--BASE STATS--")
              print("")
              lock = 0
              counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  def name_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    name = input("Name: ")
    name = name.split(" ")
    for cap in range(len(name)):
      name[cap] = name[cap].capitalize()
    name = " ".join(name)
    print("")
    for i in range(len(pokemon["Name"])):
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      ability_list = pokemon["Ability"][i].split("/")
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          if pokemon["Name"][i] == name:
            if pokemon["Name"][i][0:4] != "Mega":
              if pokemon["Name"][i] not in printed_pokemon:
                printed_pokemon.append(pokemon["Name"][i])
                print("Dex:", pokemon["Dex Number"][i])
                print("Name:", pokemon["Name"][i])
                if pd.isnull(pokemon["Type 2"][i]) == False:
                  print("Typing:",
                        pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
                elif pd.isnull(pokemon["Type 2"][i]):
                  print("Typing:", pokemon["Type 1"][i])
                print("Abilities:", (" / ".join(ability_list)))
                print("Strong against:", pokemon["Defence_Strength"][i])
                print("Weak to:", pokemon["Defence_Weakness"][i])
                print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
                if pokemon["Evolution"][i] == "None":
                  print("Evolution:", pokemon["Evolution"][i])
                elif pokemon["Evolution"][i] != "None":
                  print("Evolution:", pokemon["Evolution"][i],
                        pokemon["How_They_Evolve"][i])
                print("--BASE STATS--")
                print("Total:", pokemon["Base Total"][i])
                print("HP:", pokemon["Base HP"][i])
                print("Attack:", pokemon["Base Attack"][i])
                print("Defence:", pokemon["Base Defence"][i])
                print("SP.Attack:", pokemon["Base SP.Attack"][i])
                print("SP.Defence:", pokemon["Base SP.Defence"][i])
                print("Speed:", pokemon["Base Speed"][i])
                print("--BASE STATS--")
                print("")
                counting = counting + 1
                lock = 0
    if counting == 0:
      print("no pokemon found")

  def type_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    types = input("Types: ")
    print("")
    types = types.split("/")
    for l in range(len(types)):
      types[l] = types[l].capitalize()
    for i in range(len(pokemon["Type 1"])):
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      ability_list = pokemon["Ability"][i].split("/")
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          counter = 0
          for c in range(len(types)):
            if pokemon["Type 1"][i] == types[c] or pokemon["Type 2"][
                i] == types[c]:
              counter = counter + 1
              if pd.isnull(pokemon["Type 2"][i]):
                counter = counter + 1
            if counter == 2:
              if pokemon["Name"][i][0:4] != "Mega":
                if pokemon["Name"][i] not in printed_pokemon:
                  printed_pokemon.append(pokemon["Name"][i])
                  print("Dex:", pokemon["Dex Number"][i])
                  print("Name:", pokemon["Name"][i])
                  if pd.isnull(pokemon["Type 2"][i]) == False:
                    print("Typing:",
                          pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
                  elif pd.isnull(pokemon["Type 2"][i]):
                    print("Typing:", pokemon["Type 1"][i])
                  print("Abilities:", (" / ".join(ability_list)))
                  print("Strong against:", pokemon["Defence_Strength"][i])
                  print("Weak to:", pokemon["Defence_Weakness"][i])
                  print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
                  if pokemon["Evolution"][i] == "None":
                    print("Evolution:", pokemon["Evolution"][i])
                  elif pokemon["Evolution"][i] != "None":
                    print("Evolution:", pokemon["Evolution"][i],
                          pokemon["How_They_Evolve"][i])
                  print("--BASE STATS--")
                  print("Total:", pokemon["Base Total"][i])
                  print("HP:", pokemon["Base HP"][i])
                  print("Attack:", pokemon["Base Attack"][i])
                  print("Defence:", pokemon["Base Defence"][i])
                  print("SP.Attack:", pokemon["Base SP.Attack"][i])
                  print("SP.Defence:", pokemon["Base SP.Defence"][i])
                  print("Speed:", pokemon["Base Speed"][i])
                  print("--BASE STATS--")
                  print("")
                  lock = 0
                  counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  def ability_search(pokemon, region):
    printed_pokemon = []
    counting = 0
    abilities = input("ability: ")
    abilities = abilities.split(" ")
    for cap in range(len(abilities)):
      abilities[cap] = abilities[cap].capitalize()
    abilities = " ".join(abilities)
    print("")
    for i in range(len(pokemon["Name"])):
      pokemon_defence_weakness = pokemon["Defence_Weakness"][i]  #--here--
      pokemon_defence_weakness = pokemon_defence_weakness.split(")/")
      pokemon_defence_weakness = "),".join(pokemon_defence_weakness)
      pokemon_defence_strength = pokemon["Defence_Strength"][i]
      pokemon_defence_strength = pokemon_defence_strength.split(")/")
      pokemon_defence_strength = "),".join(pokemon_defence_strength)  #--here--
      ability_list = pokemon["Ability"][i].split("/")
      pokemon_region = pokemon["Region"][i].split("/")
      for loop in range(len(pokemon_region)):
        lock = 0
        if region == pokemon_region[loop]:
          lock = lock + 1
        elif region == "None":
          lock = lock + 1
        if lock == 1:
          for l in range(len(ability_list)):
            if abilities == ability_list[l]:
              if pokemon["Name"][i][0:4] != "Mega":
                if pokemon["Name"][i] not in printed_pokemon:
                  printed_pokemon.append(pokemon["Name"][i])
                  print("Dex:", pokemon["Dex Number"][i])
                  print("Name:", pokemon["Name"][i])
                  if pd.isnull(pokemon["Type 2"][i]) == False:
                    print("Typing:",
                          pokemon["Type 1"][i] + "/" + pokemon["Type 2"][i])
                  elif pd.isnull(pokemon["Type 2"][i]):
                    print("Typing:", pokemon["Type 1"][i])
                  print("Abilities:", (" / ".join(ability_list)))
                  print("Strong against:", pokemon["Defence_Strength"][i])
                  print("Weak to:", pokemon["Defence_Weakness"][i])
                  print("Can Mega Evolve:", pokemon["Mega_Evolve"][i])
                  if pokemon["Evolution"][i] == "None":
                    print("Evolution:", pokemon["Evolution"][i])
                  elif pokemon["Evolution"][i] != "None":
                    print("Evolution:", (pokemon["Evolution"][i]),
                          pokemon["How_They_Evolve"][i])
                  print("--BASE STATS--")
                  print("Total:", pokemon["Base Total"][i])
                  print("HP:", pokemon["Base HP"][i])
                  print("Attack:", pokemon["Base Attack"][i])
                  print("Defence:", pokemon["Base Defence"][i])
                  print("SP.Attack:", pokemon["Base SP.Attack"][i])
                  print("SP.Defence:", pokemon["Base SP.Defence"][i])
                  print("Speed:", pokemon["Base Speed"][i])
                  print("--BASE STATS--")
                  print("")
                  lock = 0
                  counting = counting + 1
    if counting == 0:
      print("no pokemon found")

  if search_choice[0].lower() == "d":
    dex_search(pokemon, region)
  elif search_choice[0].lower() == "n":
    name_search(pokemon, region)
  elif search_choice[0].lower() == "t":
    type_search(pokemon, region)
  elif search_choice[0].lower() == "a":
    ability_search(pokemon, region)
  else:
    print("invalid")


while True:
  region = input("what region do you want to search? ").capitalize()
  print("")
  if region == "Kanto" or region == "Johto" or region == "Hoenn" or region == "Sinnoh" or region == "Unnova" or region == "Kalos" or region == "Alola" or region == "Galar" or region == "Paldea" or region == "Hisui" or region == "None":
    choice = input(
      "do you want to search for a mega pokemon or a non mega (mega/non mega)? "
    )
    print(" ")
    if choice[0].upper() == "M":
      mega_search(pokemon, region)
      break
    elif choice[0].upper() == "N":
      search(pokemon, region)
      break
    else:
      print("invalid")
      replace = False  # make false when finished
      if replace == True:
        for i in range(len(pokemon["Dex Number"])):
          if input("enter quit to stop: ").upper() == "QUIT":
            break
          else:
            print("")
            if pokemon["Region"][i] == (""):
              print("done")
            else:
              print("Name:", pokemon["Name"][i])
              pokemon_region = input("region: ")
              pokemon_region = pokemon_region.split("/")
              for i in range(len(pokemon_region)):
                pokemon_region[i] = "/".join(
                  word.capitalize() for word in pokemon_region[i].split())
              pokemon_region = "/".join(pokemon_region)
              pokemon.loc[i, "Region"] = pokemon_region
              print("")
              pokemon.to_csv("pokemon.csv", index=False)
  else:
    print("invalid")
#sorting(pokemon)# sorts
#print(pokemon["Base Speed"])
#for i in range(len(pokemon["Dex Number"])):
#pokemon.loc[i, "Dex Number"] = int(pokemon.loc[i, "Dex Number"])
#pokemon.loc[i, "Base Total"] = int(pokemon.loc[i, "Base Total"])
#pokemon.loc[i, "Base HP"] = int(pokemon.loc[i, "Base HP"])
#pokemon.loc[i, "Base Attack"] = int(pokemon.loc[i, "Base Attack"])
#pokemon.loc[i, "Base Defence"] = int(pokemon.loc[i, "Base Defence"])
#pokemon.loc[i, "Base SP.Attack"] = int(pokemon.loc[i, "Base SP.Attack"])
#pokemon.loc[i, "Base Speed"] = int(pokemon.loc[i, "Base Speed"])
#pokemon.to_csv("pokemon.csv", index=False)
