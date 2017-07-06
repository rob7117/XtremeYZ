import requests
import config

messageUrl = 'https://api.ciscospark.com/v1/messages'
headers = {"Authorization":"Bearer {}".format(config.bot['token'])}

def sendMessage(text, markdown):
    data = {
        "roomId":config.roomId,
        "text":text,
        "markdown":markdown
    }
    requests.post(messageUrl, data=data, headers=headers).json()

def getMessage(id):
    return requests.get("{}/{}".format(messageUrl ,id), headers=headers).json()