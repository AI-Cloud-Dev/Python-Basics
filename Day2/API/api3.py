import json, requests

try:
    # Sending request to OpenWeatherMap API
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Lisle&appid=f51eb3cfc888d137d1dbea099d7dc8b7")
    # Parsing JSON response from the API
    data = response.json()
    # Extracting specific fields from the JSON response
    city = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    # Storing extracted data in a new dictionary
    clean_data={
        "city": city,
        "temp": temp,
        "desc": desc
    }
    
    # Writing filtered data to a JSON file (clean_data.json)
    with open("clean_data.json", "w") as file:
        json.dump(clean_data, file, indent=4)
        
    
        
except Exception as e:
    print("error in api:", e)