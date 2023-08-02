from flask import Flask, render_template, Response, url_for

import requests
import json

url = "https://api.ouedkniss.com/graphql"

headers = {
  'authority': 'api.ouedkniss.com',
  'accept': '*/*',
  'accept-language': 'en',
  'authorization': '',
  'content-type': 'application/json',
  'dnt': '1',
  'locale': 'en',
  'origin': 'https://www.ouedkniss.com',
  'referer': 'https://www.ouedkniss.com/',
  'save-data': 'on',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
  'x-app-version': '"2.1.28"'
}




app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/phone_number/<id>", methods=["POST","GET"])
def phone_number(id):
    print(id)
    payload = '{\"query\":\"query UnhidePhone($id: ID!) {\\n  phones: announcementPhoneGet(id: $id) {\\n    id\\n    phone\\n    phoneExt\\n    hasViber\\n    hasWhatsapp\\n    hasTelegram\\n    __typename\\n  }\\n}\\n","variables":{"id":"'+id+'"}}'
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    return response.json()


app.run('192.168.1.2',4444,debug=True)