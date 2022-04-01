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
nume = "Butnaru"
prenume = "Vlad"
email = "vlad@itemcloud.io"
telefon = "0788888020"
captch_resp = "03AGdBq268WLkpuwSMsKoCgyqwZlwvYswpIERiJKz989LRfCdM_iJoqEzyMB5q0gujWGji-6mjNiQKcu1Nx6Sn944eAcocl88fHsd2EurFF5vJYYXBjJ-II2ocDvjqKHXhlZhY_VQgPzV2irEvjO4EsVuvFG5InTpYFFaX2Dgxb6Q0pbkBbDS7j_mFhcfyU5NGBfokZDAvaSJ6yBGkU6MqgiPB-9G2dPyWRDlgrtiyCo2P2OChQk8C0gnT5om06zU4O_dNZ7zvhvlbNMufnrjhG6E9nIMyoSy8DAz6kLcYHcjBSh8re9HHHbLadyOeo_ky8skaqArm6BIUE9KI8k2nSlouol7WCqLM0udR0jJj3eWWrc7sDmNlRRSc0GZYpuCY_3VT_nHLwwSReFCUTRMHIZB-0V1BPAR7EcfkDO0OmnOH9ZMcQjc7Vu5h2uKWlH15vNoYOKxuHXkoeH_cT_6L5q9qdXWe08EFA820bous53O1Iz3KDrK4PhyFzmCGCF0FfHwd9-Fd6WWwK-qC2cPa68OMSCC11sG7dR-Qz3sCaIHTyYpZSTxgTMXjovM4vKCUGJLPpzvm4_mpzr1yxtqM3AWcrWmZvnWRprD_oHgPZvi8o8f7Alg66mqD8d4gxEm9Ad2h5Dl34XxfisHh7-DlMDoYFpMrTXDEmb2N6OIh34bGATlptHUDf6zA378DNKPooE551xIlKMwxOkRLwP_Qw2USRmtIL1YfXdBlPuJCgfJcr_pWvyGNzVuPw9Qve5XyhbY6hV9fJ30bE2Gr4hEtgnk8NurFio21n6Gyv1taidPBeuRvbthXjAq5eDGC2Tu2zYzDGMp5Dx53g0MUel9UKDCfheIQRKsRxMYxZIKYEGefA7uQSBH8vVuzqzKLDx5Dyds2o4VDQ2cMr2XdXy-lX0QyAudiJeW6krWNGolfCGlJD6iHmiCO1xD0aaYVUkzyG5HvEEDgyD23TDE9NgoGRFIKyzqAdPAouIMfkrHCBIOeAIb4sYnADuMPBCAZ7CUmq-nm8o3BK5gJdN1DelQQz6IjIxXxVmDUDTzuByu1RMpfc8CxeBQ1j_4K_Ytkl6fAUfMPaWctDxMUwYRmXMWH-4joNdR2JUL4JQ1-ovS874UgglNXLHSnft-zmp07-688QEHlEqNP-JgtYR2NdHuM8lgVpoktr3lbGN2rraIrhPubyNmo_W4ijWjXCWroVALcUkYQC8gxyl4MhO28SEorwZ1LxzF6P7CU4Tfi1HHcnBaVKI299Fy_MwDACmz0Tf8gkruxXVHrUYkF0apKDu2HptKt7LD83WP45Eb7f-whJvQ4boYbmxa8c1fUJBljjwC6kEjryjvDX9HRXWuvrxSFZ24urHHCBoZbWYAiXjXnwlJRY2Txu0hnSxtjyEUdNAnhehV5bzCCmzTdjyN23rFf-jL_HfGtO-0aK-muXzm0NsamC_feOvZbNR0nLP9OOHDX0GRY33J6EHaoJhSrLEJjPcIWrivoOrEu0i4M_9mf_lIoZ97ELLojwVoEwCjpruyKOaFBoB9bj6XbNPTgpIkJhcXgC9TmkoSYlTpXXtYxl2D7gUIDBZl4kMFMUvOEsZKrVZsGNlrwIx8-D5vt2Xp5QL6ZUdHYW9k9-nvFbCeUbfIYMiorhduY4oylM1jBQtxprSonUukgI-3AtVuPx7uwN_tEmbl3gI3eAnNDeRvJnuG9uIFigny_6lvFpGx6qQrVkRjTsUX3f1Zb-Bt9djLTVpZ-6V1BvwjhXzc-nMrHfHyZEGWq4frrZwUKIoJUtVPYN5AHJdd8mKFomiCyvuzMNDB4E9-v-LEllWxhPtofhC3Z6DwLtJ1zYF_MpxAFYaz3vx8ruxtvRNvI7qTHyNa8AppaVUT227z6Sw0jtskuGWlEOaWFWlbvmKW7VoM8JDeqOf4pma7zyZ189Gqz7p5-27yP2ksxcjxB3qJHGRUeYh3VFgV4zAOsPLpbfMgmx_uQn2QP-HDNoyxz-jgzri1T8MEiFtbYv3efgSbqDM16DnDpNd0f2T4Wtq1DxZRA1HcZRBrtj2eSFxg4Nbs7pAad4M0gpWdXNAOY1A9Nq8TibDFnqxC6qvdtS0-8WLgqEyon06c4T9DPYeqFEgsNktYDIH7nHQkKmQUz4NRyc_-BCs4TaxpXJsFT8NMao0OJ_Ar2rTd-XSKjcFttn-pNaFh4uPMmJJqP1QQ4zp9IGuZoSR8MRfqZ5TefovU5BCqkDW1iuATwIoBQvfaRrQFWWRK4G9mr5-L2weZrmECSZLOmJb7E5u-M77s9A1xZcC8Wwt4oueu9iUze7m2MULLDVYkDr4RdHIKjdu303fIB-V3Xb_nOg_TujLxb3IzsIOBggxp_3xl27dMMul9qBuRCCcRXx1mdzClVA5Ct7H2XKAQWvdusvOK698DEuNU52jHKyTOa2sqCz9dlEf_yvUevRmcMGgqo87mh_uJIER3FcQrmwcArAPmtY7J02I0hV7-WKYfuhclCt_Z-V0br1j4TI179gY58H7jgyHlaPyBGWBzhGdhkanuLJBfqLnG3x0jVTU-PYYbMQukeQR9oh8yMIfYtFWGRWUF1VMHh8nC5leiRT-R_Ms2Guhdvs-t_c5SQhXBRs1HZH3Fpg1_jxSJ-9AG-PI7UpY-XqftPffotg3vXRpgbHrLbdMif1M3VGsFLHQ2xY3fYfT4brFHQeoewYIFBqbU276COHQ1dK1xrhoMdMJlYavzd5VlgtzfY5YPM_Lrtg3SO2jBuHHIaN_lujMmIZKTFq-93A1108p54TEqdW3fCg1mP6KtlB_VpL3_Nzgogh6A7QdJGYKIb3iE8uDhLCeXg8NiU4Gm5ofMLlQ3YnOo0Gh-HST7UNxBo6kdTacYTyqro1yU9--za2707KAr6URYWzLbmf7u5hlP3qYOagufyxb2BbvzE1eQWi0dv3AOhQZSPBwd2i8Jl4v_h15GBlEjLouSSiaarebxKEwjcOpTCN0mAXs1dQ-sU3pq9pJRa9nHfi7Pfhsfi2oJ8izsIhfE8lwox0YGxOazx8NWg9QUDXO2597XPKK7HIRk-gxVA8IzgPcJhkLGlM1IR0qjKZbRVe1TYeLHA2Zgnn9KB7sORvEcK83vIWJ9rrky1-OzqZuIFpyBFx9eY0Etfu_2LaimdTOXQ6xNbvFlzFKiFDba260iuePsJvnhsTfzKJCmY-O6ZdMBnro1dtR1WuE59xaadqSE0A6XpRGKXQ8c1SfQb_LSN_qX9G48vDfNGaTr_-rgMdkiZugjcMCcrzaYR_SbxcZMuQBHUZ7TwI4gJKSsGLTXH8PsBTcpgC9UIUHko4Liu6ukPecI3TgUGmixSk2jqPAPz1Z2S1axfW0qZcA_HMKwx8qt-0IqK9Uw8rP9oH58ExtUTy7sjoo9kwI4BdD0r_LSUtYbG-uSxKwIGdF59vgBeRgQfSvXsp3zqNA5QreKR1FYePNwjN_eqD6j_FU1Q4H1wkUBIHAFBmuDSfcCYI_X6hkZBNo3xbIxnT_LkB6oca7o54uLYEGEPZUvE7vyBtJKY68F8C87lhgiGcrihwNM1PzehoOLqoRL9OJovdrK3foVP6Wl03jhR04xdBEbMeMBHpRyMFw6f7TZ9SxduwCyEAJrolUH_9gs1F0B_Gmun4urL_tlHk7pmfT3zS_5_J0gHIloq4ggOPEWsepq7ZF9N7pCSTqU"


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




def book_slot(start, end, birou, ghiseu):
    req = {
        "Birou": birou,
        "Ghiseu": ghiseu,
        "Start": start,
        "End": end,
        "PersDat": {
            "Nume": nume,
            "Prenume": prenume,
            "TipDoc": "7",
            "Email": email,
            "Emailconf": email,
            "Telefon": telefon
        },
        "NrPers": "1",
        "Navi": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "Suplim": [],
        "CaptchaResponse": get_new_captcha(),
        "Ip": "82.77.245.3"
    }
    headers = {'content-type': 'application/json',
               'origin': 'https://www.epasapoarte.ro',
               'referer': 'https://www.epasapoarte.ro/',
               'accept': 'application/json, text/plain, */*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'en-US,en;q=0.9,ro;q=0.8',
               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
               'sec-ch-ua-mobile': '?0',
               'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'cors',
               'sec-fetch-site': 'same-origin',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/99.0.4844.74 Safari/537.36'}
    print(req)
    r = requests.post("https://www.epasapoarte.ro/post/new", data=req, headers=headers)
    print(r.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_gaps()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
