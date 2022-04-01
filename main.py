# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
import re
import time
import pyttsx3

from datetime import datetime

iasiID = 84  # actually iasi
#iasiID = 71
nume = "Nume"
prenume = "Prenume"
email = "mail@mail.com"
telefon = "0788888888"

def get_new_captcha():
    s = requests.session()
    recaptcha_regex = re.compile(r'<input type="hidden" id="recaptcha-token" value="([^"]+)">')

    r = s.get(
        "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdVK2cUAAAAAEwMPwWk7ZAOXSU5vX1wEoBJnW1g&co=aHR0cHM6Ly93d3cuZXBhc2Fwb2FydGUucm86NDQz&hl=en&v=2uoiJ4hP3NUoP9v_eBNfU6CR&size=invisible&cb=rdv1veow83gv")

    match = recaptcha_regex.search(r.text)
    if match is None:
        return None
    recaptcha_token = match.group(1)

    data = {"reason": "q", "c": recaptcha_token}

    r = s.post("https://www.google.com/recaptcha/api2/reload?k=6LdVK2cUAAAAAEwMPwWk7ZAOXSU5vX1wEoBJnW1g", data=data)
    text = r.text
    prefix = ")]}'"
    if text.startswith(prefix):
        text = text[len(prefix):]

    json_obj = json.loads(text)
    print("obtained captcha: " + json_obj[1])
    return json_obj[1]


def get_gaps():
    engine = pyttsx3.init()
    engine.say("Started");
    engine.runAndWait()
    found = False
    while not found:
        #engine.say("waiting")
        #engine.runAndWait()
        time.sleep(2)
        wantedDate = datetime.strptime("2022-06-10T00:00:00", '%Y-%m-%dT%H:%M:%S')
        # Use a breakpoint in the code line below to debug your script.
        r = requests.get(f'https://www.epasapoarte.ro/api/gaps/{iasiID}')
        res = r.json()
        print(r.text)
        for entry in res:
            for entry_new in entry:
                print(entry_new[0])
                date = datetime.strptime(entry_new[0]['startTime'], '%Y-%m-%dT%H:%M:%S')
                if date < wantedDate:
                    print(f'Found a slot on {date}')
                    engine.say("Found a sloooot!")
                    engine.runAndWait()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_gaps()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
