import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to McNair's Online Portal.")

app = webapp2.WSGIApplication([
    ('/hello-mcnair', MainHandler)
], debug=True)
