import numpy as np
import pandas as pd
import requests
from io import StringIO


try:
    
    response= requests.get("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    data= StringIO(response.text)
    df = pd.read_csv(data)
    df['Normalized_Fare'] = df['Fare']/df['Fare'].max()
    print(df[['Fare', 'Normalized_Fare']].head())
except Exception as e:
    print("error: ", e)