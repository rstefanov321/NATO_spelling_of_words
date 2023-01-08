
import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

new_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in new_data.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word to spell in NATO lang: ").upper()

result = [new_dict[i] for i in user_word if i != " "]
print(result)
