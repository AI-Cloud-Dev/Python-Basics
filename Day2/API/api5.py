import json, requests

try:
    response = requests.get("")
    data = response.json()
    
    title = data["title"]
    date = data["date"]
    explaination = data["explaination"]
    
    nasa_apod = {
        "title": title,
        "date": date,
        "explaination": explaination
    }
    
    with open("nasa_apod.json", "w") as file:
        json.dump(nasa_apod, file, indent = 4)
    print("Filtered the data successfully!!")
    
except Exception as e:
    print("Error is:", e)