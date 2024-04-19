import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/knowLandStatus"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    data = {
        "district": district,
        "mandal": mandal,
        "village": village
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        survey_numbers = [option.text.strip() for option in soup.find("select", {"id": "SlnoNo"}).find_all("option")]
        return survey_numbers
    else:
        print("Failed to retrieve survey numbers.")
        return None

district = input("Enter district: ")
mandal = input("Enter mandal: ")
village = input("Enter village: ")

survey_numbers = get_survey_numbers(district, mandal, village)
if survey_numbers:
    print("Survey Numbers:")
    for number in survey_numbers:
        print(number)
