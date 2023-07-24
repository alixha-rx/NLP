import pandas as pd

def test_function(N, V):
    out_list = []
    for v in V:
        watch = any(word in v['Notes'] for word in N)
        if watch:
            out_list.append(True)
        else:
            out_list.append(False)
    return out_list

# Sample clinical notes data
V1 = [
    {'Notes': 'Patient A is currently experiencing unstable housing conditions. They are homeless.'},
    {'Notes': 'Patient B has stable housing and is not homeless.'},
    # Add more clinical notes data here...
]

V2 = [
    {'Notes': 'Patient C used to be homeless but is no longer homeless.'},
    {'Notes': 'Patient D is not experiencing housing insecurity and is not homeless.'},
    # Add more clinical notes data here...
]

homeless_words = ['homeless', 'homless', 'insecure housing', 'unhoused', 'undomiciled', 'undomiciled',
                  'sleeping outside', 'temporary shelter', 'shelter-domiciled', 'sleeping in shelter',
                  'staying in shelter', 'living in shelter', 'living on street', 'living on the street',
                  'living in homeless shelter', 'lives in shelter', 'lives on the street',
                  'lives in homeless shelter', 'in and out of shelter', 'sleeping on subway', 'refuses shelter',
                  'refuses to go to shelter', 'refuses to stay at shelter', 'refuses to visit shelter',
                  'unwilling to go to shelter', 'sleeping in park', 'sleeping in a park', 'sleeping on a bench',
                  'sleeping on train', 'sleeping on the street', 'sleeps in park', 'sleeps in a park',
                  'sleeps on a bench', 'sleeps on the street']

not_homeless_words = ['not homeless', 'used to be homeless', 'homeless in the past', 'was homeless',
                      'no longer homeless', 'not housing insecure', 'not unhoused']

# Create the DataFrame and apply the test function to get True/False values
dt = pd.DataFrame()
dt["notes"] = V1 + V2
dt["homeless"] = test_function(homeless_words, V1 + V2)
dt["not_homeless"] = test_function(not_homeless_words, V1 + V2)

# Create the summary column based on True/False values
dt["overall"] = "unknown"
dt.loc[dt["homeless"] & ~dt["not_homeless"], "overall"] = "Homeless"
dt.loc[~dt["homeless"] & dt["not_homeless"], "overall"] = "NOT_Homeless"

print(dt)
