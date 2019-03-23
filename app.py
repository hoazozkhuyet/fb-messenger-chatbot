import os
import sys
import json
from datetime import datetime
from pymessenger import Bot
from utils import wit_resp
from pymessager.message import Messager
#from googlesearch.googlesearch import GoogleSearch
from pymessenger2.utils import AttrsEncoder
import requests
from flask import Flask, request

app = Flask(__name__)
PAGE_ACCESS_TOKEN = "EAAHZAErTAOQQBAEC4VACIHam094JVRQ3TuwZAFVJU5HXJFsZCo9VSKhZCL1r9Bjnx6dBwPyLSltwX3QqaXylj2ZCo8gHosIjZANqrRTLLAHvXQiPAA6Vp1MMRqh5WKgsM4yqiCzXO2d1ZCTCa4GZBCwfjk2Y40N8HYEZAXmZC9nqoCM9UASd1HR2ZA9"
bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "test-app":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello Cuong", 200


client = Messager(PAGE_ACCESS_TOKEN)
client.set_greeting_text("Kính chào ban lãnh đạo công ty VNNet\n Tên em là Nguyễn Quốc Cường\n Đây là chatbot đầu tiên của em")
client.set_get_started_button_payload("Get Start")
#ggsearch = GoogleSearch()
button_list = [
        {
            "type":"web_url",
            "url":"https://www.facebook.com/cuong.nguyenquoc.7186",
            "title":"Thông tin về tôi"
        },
		{
			"type": "postback",
  			"title": "Tin tức hôm nay",
  			"payload": "payload"
		},
		{
			"type": "postback",
  			"title": "Thời tiết hôm nay",
  			"payload": "payload"
		}
		]
		
@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)
	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:
				sender_id = messaging_event['sender']['id']
				# recipient_id = messaging_event['recipient']['id']
				if messaging_event.get('message'):
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
						if messaging_text == "Trước khi bắt đầu hãy xem lại video demo chatbot này":
							response = "https://www.youtube.com"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif messaging_text == "Thông tin về tôi":
							response = "https://www.facebook.com/cuong.nguyenquoc.7186"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif messaging_text == "Tin tức thể thao hôm nay":
							#entity, value = wit_resp(messaging_text)
							response = "https://news.zing.vn/the-thao.html"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif messaging_text == "Tin tức pháp luật hôm nay":
							#entity, value = wit_resp(messaging_text)
							response = "https://news.zing.vn/phap-luat.html"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif messaging_text == "Tin tức thế giới hôm nay":
							#entity, value = wit_resp(messaging_text)
							response = "https://news.zing.vn/the-gioi.html"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif messaging_text == "Tin tức công nghệ hôm nay":
							#entity, value = wit_resp(messaging_text)
							response = "https://news.zing.vn/cong-nghe.html"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						else:
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
				elif messaging_event.get('postback'):
					if 'title' in messaging_event['postback']:
						button_title = messaging_event['postback']['title']
						if button_title == "Tin tức hôm nay":
							response = "https://news.zing.vn/"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif button_title == "Bắt đầu":
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)
						elif button_title == "Thời tiết hôm nay":
							response = "https://www.accuweather.com/vi/vn/vietnam-weather"
							bot.send_text_message(sender_id, response)
							bot.send_button_message(sender_id,"Bạn nên chọn những options này thay vì tự nhập",button_list)					             
	return "ok", 200

def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 2410)
