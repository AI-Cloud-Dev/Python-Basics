import json, requests

try:
    response = requests.get("https://restcountries.com/v3.1/name/Japan")
    data = response.json()[0]
    
    countryName = data["name"]["common"]
    capitalCity = data["capital"][0]
    region = data["region"]
    
    country_details = {
        "name": countryName,
        "capital": capitalCity,
        "region": region
    }
    
    with open("country_data.json", "w") as file:
        json.dump(country_details, file, indent=4)
    print("✔️ Country data saved successfully to country_data.json")
except Exception as e:
    print("error is :", e)