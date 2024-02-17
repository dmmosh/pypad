import pickle
import pandas as pd


colors = pd.read_excel("data.xlsx").to_dict('list')

object = pickle.dump(colors, open('data.obj', 'wb'))

object = pickle.load(open('data.obj', 'rb'))

colors = None
print(object)