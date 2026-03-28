import pandas as pd
import requests
from io import StringIO

try:
    response = requests.get("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    response.raise_for_status()
    # df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    data = StringIO(response.text)
    df = pd.read_csv(data)
    
    print(df.head())
    print(df['Age'].mean())
    print(df['Sex'].value_counts())
except Exception as e:
    print("Error: ", e)