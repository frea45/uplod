import requests
import json


def account_login():

    raw_text1 = input("**Now Send Your PW Auth Token:**\n")

    headers = {

        'Host': 'api.penpencil.co',

        'authorization': f"Bearer {raw_text1}",

        'client-id': '5eb393ee95fab7468a79d189',

        'client-version': '1910',

        'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',

        'randomid': 'e4307177362e86f1',

        'client-type': 'WEB',

        'content-type': 'application/json; charset=utf-8',

    }

    params = {

        'mode': '1',

        'amount': 'paid',

        'page': '1',

    }



    print("**You have these Batches :-\n\nBatch ID : Batch Name**")

    aa = ''

    response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]

    for data in response:

        batch_name = data['name']

        batch_id = data['_id']

        aa += f'**{batch_name}**  :  ```{batch_id}```\n\n'

    print(aa)



    raw_text3 = input("**Now send the Batch ID to Download**\n")

    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]

    print("Subject : Subject_Id")

    bb = ''

    for data in response2:

        subject_name = data['subject']

        subject_id = data['_id']

        bb += f'**{subject_name}**  :  ```{subject_id}```\n\n'

    print(bb)



    raw_text4 = input("**Now send the subject ID to Download**\n")



    print('**Now Send Content Type you want to extract.**\n```DppNotes```|```videos```|```notes```')

    raw_text5 = input()



    to_write = ''

    for i in range(1, 15):

        params1 = {

            'page': f'{i}',

            'tag': '',

            'contentType': f'{raw_text5}',

        }

        response3 = requests.get(f'https://api.penpencil.co/v2/batches/{raw_text3}/subject/{raw_text4}/contents', params=params1, headers=headers).json()["data"]

        if raw_text5 == 'videos':

            for data in response3:

                url = f"https://d26g5bnklkwsh4.cloudfront.net/{data['url'].split('/')[-2]}/master.m3u8" if raw_text5 == "videos" else f"{data['baseUrl']}{data['key']}"

                topic = data['topic']

                write = f"{topic} {url}\n"

                to_write += write

        else:

            for data in response3:

                a = data['homeworkIds'][0]['attachmentIds'][0]

                name = data['homeworkIds'][0]['topic'].replace('|', ' ').replace(':', ' ')

                url = a['baseUrl'] + a['key']

                write = f"{name} {url}\n"

                to_write += write



    with open(f"{raw_text5} {raw_text4}.txt", "w", encoding="utf-8") as f:

        f.write(to_write)

    print("Course txt file generated successfully.")

   print("\nBy AntifiedNull 😎")



account_login()


                        #AntifiedNull[Prateek]