import random
from flask import Flask, request, abort
from imgurpython import ImgurClient
from sheetdb import *

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import tempfile, os
from config import client_id, client_secret, album_id, access_token, refresh_token, line_channel_access_token, \
    line_channel_secret

app = Flask(__name__)

line_bot_api = LineBotApi(line_channel_access_token)
handler = WebhookHandler(line_channel_secret)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
a=0
account=[]
print("statr")
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print(signature)
    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'

@handler.add(MessageEvent, message=(ImageMessage, TextMessage))
def handle_message(event):
    print("get")
    userID = get(event.source.user_id)
    
    if isinstance(event.message, TextMessage):
        if event.message.text == "開戶" and len(userID)==0:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入姓名'))
            AccountuserID=event.source.user_id
            create(AccountuserID)
            print(AccountuserID)

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountName']=="":
            AccountuserID=event.source.user_id  
            AccountName=event.message.text
            update(AccountuserID,AccountName," "," "," "," "," "," "," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入身分證號碼'))
        
        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountID']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID=event.message.text
            update(AccountuserID,AccountName,AccountID," "," "," "," "," "," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='生日'))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountBrith']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith," "," "," "," "," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='性別'))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountSex']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith = userID[0]["AccountBrith"]
            AccountSex=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex," "," "," "," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='婚姻'))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountMarital']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith = userID[0]["AccountBrith"]
            AccountSex = userID[0]["AccountSex"]
            AccountMarital=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital," "," "," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='家話(Tel)'))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountTel']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith = userID[0]["AccountBrith"]
            AccountSex = userID[0]["AccountSex"]
            AccountMarital = userID[0]["AccountMarital"]
            AccountTel=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel," "," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='行動電話(Phone)'))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountPhone']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith = userID[0]["AccountBrith"]
            AccountSex = userID[0]["AccountSex"]
            AccountMarital = userID[0]["AccountMarital"]
            AccountTel = userID[0]["AccountTel"]
            AccountPhone=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel,AccountPhone," "," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='居住地址'))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountAdress1']=="":
            AccountuserID=event.source.user_id 
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith = userID[0]["AccountBrith"]
            AccountSex = userID[0]["AccountSex"]
            AccountMarital = userID[0]["AccountMarital"]
            AccountTel = userID[0]["AccountTel"]
            AccountPhone = userID[0]["AccountPhone"]
            AccountAdress1=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel,AccountPhone,AccountAdress1," "," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="戶籍地址(跟居住地址相同請輸入'同上')"))

        elif event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountAdress2']=="":
            AccountuserID=event.source.user_id
            AccountName = userID[0]["AccountName"]
            AccountID = userID[0]["AccountID"]
            AccountBrith = userID[0]["AccountBrith"]
            AccountSex = userID[0]["AccountSex"]
            AccountMarital = userID[0]["AccountMarital"]
            AccountTel = userID[0]["AccountTel"]
            AccountPhone = userID[0]["AccountPhone"]
            AccountAdress1 = userID[0]["AccountAdress1"]
            AccountAdress2=event.message.text
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel,AccountPhone,AccountAdress1,AccountAdress2," "," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="請上傳身分證正面照"))
        
        if event.message.text == "開戶" and len(userID)==1:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='您已經開戶過了'))

    if isinstance(event.message, ImageMessage) and event.source.user_id == userID[0]['AccountuserID'] and userID[0]['AccountImage1']=="":
        print("111")
        ext = 'jpg'
        AccountuserID=event.source.user_id 
        AccountName = userID[0]["AccountName"]
        AccountID = userID[0]["AccountID"]
        AccountBrith = userID[0]["AccountBrith"]
        AccountSex = userID[0]["AccountSex"]
        AccountMarital = userID[0]["AccountMarital"]
        AccountTel = userID[0]["AccountTel"]
        AccountPhone = userID[0]["AccountPhone"]
        AccountAdress1 = userID[0]["AccountAdress1"]
        AccountAdress2 = userID[0]["AccountAdress2"]
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name

        dist_path = tempfile_path + '.' + ext
        dist_name = os.path.basename(dist_path)
        os.rename(tempfile_path, dist_path)
        try:
            client = ImgurClient(client_id, client_secret, access_token, refresh_token)
            config = {
                        'album': album_id,
                        'name': 'Catastrophe!',
                        'title': 'Catastrophe!',
                        'description': 'Cute kitten being cute on '
                     }
            path = os.path.join('static', 'tmp', dist_name)
            image=client.upload_from_path(path, config=config, anon=False)
            os.remove(path)
            print(path)
            print(image["link"])
            AccountImage1=image["link"]
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel,AccountPhone,AccountAdress1,AccountAdress2,AccountImage1," ")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請上傳身分證背面照'))
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='上傳失敗'))

        return

    if isinstance(event.message, ImageMessage)  and userID[0]['AccountImage2']=="":
        ext = 'jpg'
        print("222")
        AccountuserID=event.source.user_id 
        AccountName = userID[0]["AccountName"]
        AccountID = userID[0]["AccountID"]
        AccountBrith = userID[0]["AccountBrith"]
        AccountSex = userID[0]["AccountSex"]
        AccountMarital = userID[0]["AccountMarital"]
        AccountTel = userID[0]["AccountTel"]
        AccountPhone = userID[0]["AccountPhone"]
        AccountAdress1 = userID[0]["AccountAdress1"]
        AccountAdress2 = userID[0]["AccountAdress2"]
        AccountImage1 = userID[0]["AccountImage1"]
        message_content = line_bot_api.get_message_content(event.message.id)

        with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name

        dist_path = tempfile_path + '.' + ext
        dist_name = os.path.basename(dist_path)
        os.rename(tempfile_path, dist_path)
        try:
            client = ImgurClient(client_id, client_secret, access_token, refresh_token)
            config = {
                        'album': album_id,
                        'name': 'Catastrophe!',
                        'title': 'Catastrophe!',
                        'description': 'Cute kitten being cute on '
                     }
            path = os.path.join('static', 'tmp', dist_name)
            image=client.upload_from_path(path, config=config, anon=False)
            os.remove(path)
            print(path)
            AccountImage2=image["link"]
            update(AccountuserID,AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel,AccountPhone,AccountAdress1,AccountAdress2,AccountImage1,AccountImage2)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='上傳完成'))
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='上傳失敗'))
        return



if __name__ == '__main__':
    app.run(debug=True,port=5000)
