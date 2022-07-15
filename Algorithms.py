
import pandas as pd

# load data set

dftrain = pd.read_csv('data/train.csv')
dfeval = pd.read_csv('data/test.csv')
y_train = dftrain.pop('Survived')
# y_eval = dfeval.pop('Survived')

print(dftrain.head())