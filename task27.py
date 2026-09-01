"""Write a python proogram to fromat the following letter using esacpe sequence charcaters
    letter ="Dear Saurabh, this python course is nice. Thanks!"
"""
letter ="Dear Saurabh, this python course is nice. Thanks!"
letter=letter.replace(", ","\n")
letter=letter.replace(". ","\n")
print(letter)
