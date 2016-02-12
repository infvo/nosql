import web
import pymongo
import markdown

web.config.debug = False
urls = (
    "/count", "count",
    "/login", "login",
    "/reset", "reset"
)
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

# DB configuration:
client = pymongo.MongoClient()
db = client["blog"]

renderglobals = {'markdown': markdown.markdown}
render = web.template.render('templates/', globals=renderglobals)

class count:
  def GET(self):
    session.count += 1
    return str(session.count)

class reset:
  def GET(self):
    session.kill()
    return ""

class login:
  def GET(self):
    return render.login()

  def POST(self):
    data=web.input()
    print(data)
    if data.user != "":
      user = db.users.find_one({"username": data.user})
      print(user)
      if user != None:
        if user["password"] == data.passwd:
          return "Logged in: " + data.user
    return "not logged in"

# set default users"

db.users.update_one(
    {"username": "jon"},
    {"$set": {"password": "pass1"}},
    upsert=True
  )

db.users.update_one(
    {"username": "jill"},
    {"$set": {"password": "pass2"}},
    upsert=True
  )

if __name__ == "__main__":
    app.run()
