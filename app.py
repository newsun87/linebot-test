#!/usr/bin/env python3
# -*- coding: utf-8

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Ll8E/hD0IKh1+Laro91WzHmBTgOGF2KgQl7cSjFag+NgVDCZYioxn9oolnkijfwtNFZe/gQzhHdZimzjJq1R3uLbb296yZ2PQ5tuG4aChni9RbTEu0cekvQIPUmks15l1hZdp2y/MlxEzXuDZgYgrlGUYhWQfeY8sLGRXgo3xvw=')
# Channel Secret
handler = WebhookHandler('05ad96ecf63b4f2f886feb10425a2b43')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text="我收到你送來的文字訊息" + event.message.text)    
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000)
    app.run(debug=True, use_reloader=True)

     
