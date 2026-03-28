import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt


try:
    response = requests.get("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    data = StringIO(response.text)
    df = pd.read_csv(data)
    
    plt.subplot(1,2,1)
    df['Age'].plot(kind ='hist', bins=20, title="Age Distribution")
    plt.xlabel("Age")
    # plt.subplot(nrows, ncols, index)
    plt.subplot(1,2,2)
    df['Sex'].value_counts().plot(kind='bar', title ="GenderCountrs")
    plt.xlabel("Sex")
    plt.ylabel("Count")
    
    # plt.tight_layout()
    plt.show()
except Exception as e:
    print("Error: ", e)