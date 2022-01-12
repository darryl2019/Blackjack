from tkinter import re

def calcValue(ListArgs):
    totalHandValue = 0
    characters_to_remove = "HCDS"
    pattern = "[" + characters_to_remove + "]"
    for y in range(len(ListArgs)):
        value = int(re.sub(pattern, "", ListArgs[y]))

        if value > 10:
            value = 10
            totalHandValue = totalHandValue + value
        else:
            totalHandValue = totalHandValue + value
    return totalHandValue
