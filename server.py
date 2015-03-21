import os
import configparser
import tornado.ioloop
import tornado.web

class Hello(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

config = configparser.ConfigParser()
config.read("config.ini")

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret":config['secrets']['cookie'],
    "xsrf_cookies": True,
}

application = tornado.web.Application([
    (r"/", Hello),
    
], **settings)

if __name__ == "__main__":
    application.listen(int(config['networking']['port']))
    tornado.ioloop.IOLoop.instance().start()
