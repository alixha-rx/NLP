import pandas as pd
from utils import unhoused_words, not_unhoused_words


def test_function(N, V):
    out_list = []
    for note in N:
        watch = any([word in note for word in V])
        if watch:
            out_list.append(True)
        else:
            out_list.append(False)
    return out_list


# Sample clinical notes data
with open('toy_dataset.txt', 'r') as f:
    note_list = [note.strip() for note in f]

# Create the DataFrame and apply the test function to get True/False values
dt = pd.DataFrame()
dt["notes"] = note_list
dt["unhoused"] = test_function(note_list, unhoused_words)
dt["not_unhoused"] = test_function(note_list, not_unhoused_words)

# Create the summary column based on True/False values
dt["housing"] = "unknown"
dt.loc[dt["unhoused"] & ~dt["not_unhoused"], "housing"] = "Unhoused"
dt.loc[dt["not_unhoused"], "housing"] = "Not Unhoused"

print(dt)
