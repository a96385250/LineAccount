import requests
url = 'https://sheetdb.io/api/v1/4hca9nukrvlg4'
url2= 'https://sheetdb.io/api/v1/4hca9nukrvlg4/search'

# 新增
def create(AccountuserID):
    datas = {"data":[{
                        "AccountuserID":AccountuserID
                    }]}
    r = requests.post(url, json=datas)
    return r

# def create(AccountName,AccountID,AccountBrith,AccountSex,AccountMarital,AccountTel,AccountPhone,AccountAdress1,AccountAdress2,AccountID1,AccountID2):
#     datas = {'data':[{"AccountName":AccountName,
#                       "AccountID":AccountID,
#                       "AccountBrith":AccountBrith,
#                       "AccountSex":AccountSex,
#                       "AccountMarital":AccountMarital,
#                       "AccountTel":AccountTel,
#                       "AccountPhone":AccountPhone,
#                       "AccountAdress1":AccountAdress1,
#                       "AccountAdress2":AccountAdress2,
#                       "AccountImage1":AccountID1,
#                       "AccountImage2":AccountID2}]}
#     r = requests.post(url, json=datas)
#     return r

#修改
def update(AccountuserID,AccountName, AccountID, AccountBrith, AccountSex,AccountMarital,AccountTel,AccountPhone,AccountAdress1,AccountAdress2,AccountImage1,AccountImage2):
    furl = url+'/AccountuserID/'+AccountuserID
    datas = {"data":[{  
                        "AccountuserID": AccountuserID,
                        "AccountName"  : AccountName,
                        "AccountID"   : AccountID,
                        "AccountBrith"  : AccountBrith,
                        "AccountSex"  : AccountSex,
                        "AccountMarital": AccountMarital,
                        "AccountTel": AccountTel,
                        "AccountPhone": AccountPhone,
                        "AccountAdress1": AccountAdress1,
                        "AccountAdress2": AccountAdress2,
                        "AccountImage1": AccountImage1,
                        "AccountImage2" : AccountImage2
                    }]}
    
    r = requests.put(furl, json= datas)
    

# 刪除
def delete(userid,flow):
    furl = url+'/userid/'+userid
    datas = {'data':[{"userid":userid, "flow":flow}]}
    r = requests.delete(furl)
    return r

# 查詢
def get(userid):
    params = {"AccountuserID":userid}
    r = requests.get(url2, params=params)
    return r.json()
# ,eto,efrom,money,bnak,rate,info
# ,'','','','','',''
# s = update('james', 'nn','TWD','USD',1221)
# print(s)
# a = get("213131")
# print(a)
# print(a[0]['AccountuserID'])