import pickle
import pandas as pd


colors = pd.read_excel("data.xlsx").set_index('ID').T.to_dict('list')

print(colors)