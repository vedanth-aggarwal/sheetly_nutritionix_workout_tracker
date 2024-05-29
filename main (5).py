
import requests,datetime,os
token = os.environ['TOKEN']
username = os.environ['username']
password = os.environ['password']
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
sheetyurl = os.environ['SHEETYURL']

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Authorization': f'Bearer {token}'
}
searchparams = {
    'query':input('Enter activity : '),
    'gender':input('Enter Gender : ').lower(),
    'weight_kg' : float(input('Enter weight : ')),
    'height_cm' : float(input('Enter height : ')),
    'age' : int(input('Enter age : '))
}
sheetyendpoint = "https://api.sheety.co/30c62f467aac2927a0d958d82fdd2214/workoutTracking/workouts"
response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',
                         json=searchparams,headers=headers)
response.raise_for_status()
response = response.json()
print(response)
#################################

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheetyendpoint, json=sheet_inputs,headers=headers)
    print(sheet_response.text)