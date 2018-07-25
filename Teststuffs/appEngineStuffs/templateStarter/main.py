"""
in order to start the server, use the following command in
the terminal

dev_appserver.py app.yaml
"""


import webapp2
import jinja2
import json
import logging
import random
from google.appengine.api import urlfetch

api_string = "https://api.imgflip.com/get_memes"
response1 = urlfetch.fetch(api_string)
json_dict1 = json.loads(response1.content)
meme_dict = {}

for obj in json_dict1['data']['memes']:
    meme_dict[obj['name']] = int(obj['id'])

templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)

def getRandomMeme(top=None, bot=None):
    picIds = []
    topTexts = ["This is a meme!",'HA',"Fool",'Guess what', "yikes"]
    botTexts = ['You thought!', 'Get Reckt', "Its LIT", "WOOOOOOOOW"]

    #creating api strings
    api_string = "https://api.imgflip.com/get_memes"
    api_string2 = "https://api.imgflip.com/caption_image?{ids}&{u}&{p}&{t}&{tt}"

    #variables that needed to make meme

    id = "template_id="
    username = "username=chukwurahnonso"
    password = "password=0987654321"
    text0 = 'text0='
    text1 = 'text1='

    #using urlfetch, the api strings are passed to get requests
    #the requests are the deciphered into json using json lib

    response1 = urlfetch.fetch(api_string)
    json_dict1 = json.loads(response1.content)

    for obj in json_dict1['data']['memes']:
        picIds.append(int(obj['id']))

    randomMemeID = random.choice(picIds)
    randomTopText = random.choice(topTexts)
    randomBotText = random.choice(botTexts)

    meme_url = api_string2.format(
        ids=id+str(randomMemeID), u=username,p=password,t=text0+randomTopText,
        tt=text1+randomBotText)

    POSTResponse = urlfetch.fetch(meme_url)
    json_dict = json.loads(POSTResponse.content)

    #This works
    logging.info(json_dict['data']['url'])
    return json_dict['data']['url']


def makeMeme(top, bot, meme_t):
    picIds = []

    #creating api strings
    api_string = "https://api.imgflip.com/get_memes"
    api_string2 = "https://api.imgflip.com/caption_image?{ids}&{u}&{p}&{t}&{tt}"

    id = "template_id="+str(meme_dict[str(meme_t)])
    logging.info(id)
    username = "username=chukwurahnonso"
    password = "password=0987654321"
    text0 = 'text0='+top
    text1 = 'text1='+bot

    #using urlfetch, the api strings are passed to get requests
    #the requests are the deciphered into json using json lib
    # response1 = urlfetch.fetch(api_string)
    # json_dict1 = json.loads(response1.content)
    #
    # for obj in json_dict1['data']['memes']:
    #     picIds.append(int(obj['id']))
    # 
    # randomMemeID = random.choice(picIds)

    meme_url = api_string2.format(
        ids=id, u=username,p=password,t=text0,tt=text1)

    POSTResponse = urlfetch.fetch(meme_url)
    json_dict = json.loads(POSTResponse.content)

    return json_dict['data']['url']



class HomePage(webapp2.RequestHandler):


    def get(self):
        template = templateEnv.get_template("templates/home.html")

        perams = {"meme_img":getRandomMeme(),
            'memes':meme_dict}

        self.response.write(template.render(perams))

    def post(self):
        line1 = self.request.get('user-first-ln')
        line2 = self.request.get('user-second-ln')
        memeType = self.request.get('meme-type')
        url = makeMeme(str(line1), str(line2),memeType)
        meme_dict = {"first_line":line1,"second_line":line2,
            "meme_type":memeType, "meme_url":url}


        template = templateEnv.get_template('templates/result.html')
        self.response.write(template.render(meme_dict))

class recipeBrowser(webapp2.RequestHandler):
    def get(self):
        recipe = {'ingredients':['cottage chese','pinapple'],
            'cuisine':"nixonian"}
        template = templateEnv.get_template("templates/recipieBrowser.html")
        self.response.write(template.render(recipe))

app = webapp2.WSGIApplication([("/home",HomePage),('/recipeBrowser',recipeBrowser)],
 debug=True)
