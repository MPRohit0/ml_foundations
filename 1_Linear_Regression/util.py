import pandas as pd

data = pd.read_csv("insurance.csv")

# we will get a list of all fectures needed to be encoded and the dataframe

def ordinalEncoder(df):
    pass


def OneHotEncoder(df):
    
    print(pd.dtype(df["sex"]))


OneHotEncoder(data)