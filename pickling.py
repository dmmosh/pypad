import pickle
import pandas as pd


colors = pd.read_excel("pypad/data.xlsx").to_dict('list')

object = pickle.dump(colors, open('pypad/data.obj', 'wb'))

object = pickle.load(open('pypad/data.obj', 'rb'))

colors = None
print(object)