import pandas as pd
import requests
from io import StringIO

try:
    response = requests.get("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    data = StringIO(response.text)
    df = pd.read_csv(data)
    print("Before cleaned Rows:", len(df))
    df_clean = df[df['Age'].notna()]
    df_clean = df.dropna(subset =['Age'])
    print("cleaned Rows:", len(df_clean))
    
except Exception as e:
    print("Uncleaned", e)