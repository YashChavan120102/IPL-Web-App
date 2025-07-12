import pandas as pd

def preprocess(df):
    df = pd.concat([df, pd.get_dummies(df['winner'])], axis=1)
    return df