import pymongo
import web
import re
import base64

urls = (
    '/','Index',
    '/login','Login',
    '/logout', 'Logout'
)

app = web.application(urls,globals())

# db configuration:
client = pymongo.MongoClient()
db = client["blog"]

allowed = (
    ('jon','pass1'),
    ('tom','pass2')
)


session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

class Index:
    def GET(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
            return 'This is the index page'
        else:
            raise web.seeother('/login')

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            username, password = base64.decodestring(auth).split(':')
            if (username, password) in allowed:
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return

class Logout:
    def GET(self):
      session.kill()


if __name__=='__main__':
    app.run()
