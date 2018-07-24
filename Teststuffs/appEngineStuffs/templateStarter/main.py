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

templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)

def getRandomMeme():
    picIds = []

    #creating api strings
    api_string = "https://api.imgflip.com/get_memes"
    api_string2 = "https://api.imgflip.com/caption_image?{ids}&{u}&{p}&{t}&{tt}"

    #variables that needed to make meme
    id = "template_id="
    username = "username=chukwurahnonso"
    password = "password=0987654321"
    text0 = 'text0=this'
    text1 = 'text1=this'

    #using urlfetch, the api strings are passed to get requests
    #the requests are the deciphered into json using json lib

    response1 = urlfetch.fetch(api_string)
    json_dict1 = json.loads(response1.content)

    for obj in json_dict1['data']['memes']:
        picIds.append(int(obj['id']))

    randomMemeID = random.choice(picIds)
    meme_url = api_string2.format(
        ids=id+str(randomMemeID), u=username,p=password,t=text0,tt=text1)

    POSTResponse = urlfetch.fetch(meme_url)
    json_dict = json.loads(POSTResponse.content)

    #This works
    logging.info(json_dict['data']['url'])
    return json_dict['data']['url']





class HomePage(webapp2.RequestHandler):
    def get(self):
        template = templateEnv.get_template("templates/home.html")
        self.response.write(template.render())
        getRandomMeme()

class recipeBrowser(webapp2.RequestHandler):
    def get(self):
        recipe = {'ingredients':['cottage chese','pinapple'],
            'cuisine':"nixonian"}
        template = templateEnv.get_template("templates/recipieBrowser.html")
        self.response.write(template.render(recipe))

app = webapp2.WSGIApplication([("/home",HomePage),('/recipeBrowser',recipeBrowser)],
 debug=True)
