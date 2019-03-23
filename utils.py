from wit import Wit
access_token = "GFVAV7CS3FH4LVPKXW63M6RSJHE2EJER"
client = Wit(access_token = access_token)
def wit_resp(message_text):
    resp = client.message(message_text)
    entity = None
    value = None
    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return (entity,value)
#print(wit_resp("Tin tức thời sự hôm nay"))