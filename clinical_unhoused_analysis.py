import pandas as pd
from utils import positive_vocab, negative_vocab

# Read the CSV file as a DataFrame
df = pd.read_csv("/Users/alishaaristel/nlp/nlp/toy_dataset.csv")

def test_function(note_list, vocabulary_list):
    out_list = []
    for note in note_list:
        watch = any(word in note for word in vocabulary_list)
        out_list.append(watch)
    return out_list

# Apply the test function to get True/False values
df["unhoused"] = test_function(df["Notes"], negative_vocab)
df["housed"] = test_function(df["Notes"], positive_vocab)

# Create the summary column based on True/False values
df["overall"] = "unknown"
df.loc[df["unhoused"], "overall"] = "unhoused"
df.loc[df["housed"], "overall"] = "housed"

print(df)
