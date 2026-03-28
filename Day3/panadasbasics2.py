import pandas as pd
import requests
from io import StringIO


try:
    response = requests.get("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    data = StringIO(response.text)
    df = pd.read_csv(data)
    print(df.head())
    print(len(df))
    print(df.shape[0])
    print(df['Survived'].sum())
    print(df['Age'].mean())
    print(df['Sex'].value_counts())
except Exception as e:
    print("Error:", e)