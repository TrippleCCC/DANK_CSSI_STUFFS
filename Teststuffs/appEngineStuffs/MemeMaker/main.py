
import webapp2
import json
from google.appengine.api import urlfetch
import time
import logging


pics = []
memes = []


def getMemes():
    #creating api strings
    api_string = "https://api.imgflip.com/get_memes"
    api_string2 = "https://api.imgflip.com/caption_image?{ids}&{u}&{p}&{t}&{tt}"
    #variables that needed to make meme
    id = "template_id=438680"
    username = "username=chukwurahnonso"
    password = "password=0987654321"
    text0 = 'text0=this'
    text1 = 'text1=this'

    #using urlfetch, the api strings are passed to get requests
    #the requests are the deciphered into json using json lib
    api_string2 = api_string2.format(
        ids=id,u=username,p=password,t=text0,tt=text1)
    r = urlfetch.fetch(api_string)
    r2 = urlfetch.fetch(api_string2)
    j = json.loads(r.content)
    j2 = json.loads(r2.content)

    #this loops through all the objects that were returned from
    #api_string, takes the pic ids and stores them in pics
    for obj in j['data']['memes']:
        pics.append(obj['id'])

    for i in range(0,5):
        temp = urlfetch.fetch(api_string2.format(
            ids='template_id='+str(pics[i]),
            u=username,p=password,t=text0,tt=text1))
        temp2 = json.loads(temp.content)
        memes.append(temp2['data']['url'])


    memes.append(j2['data']['url'])


class MemeMaker(webapp2.RequestHandler):
    def get(self):
        text = self.request.get("text")
        self.request.headers['Content-Type'] = 'text/html'
        #self.response.write("<img src={}>".format(pics[0]))
        for i in range(len(memes)):
            self.response.write("<img src={}>".format(memes[i]))
        self.response.write(memes)
app = webapp2.WSGIApplication([("/meme",MemeMaker)], debug=True)

getMemes()
