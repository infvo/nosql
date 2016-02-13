import web
import pymongo
import markdown

web.config.debug = False
urls = (
    "/count", "count",
    "/admin", "admin",
    "/admin/newuser", "newuser",
    "/login", "login",
    "/logout", "logout"
)
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': ""})

# DB configuration:
client = pymongo.MongoClient()
db = client["blog"]

renderglobals = {'markdown': markdown.markdown}
render = web.template.render('templates/', globals=renderglobals)

class admin:
  def GET(self):
    if session.user == "admin":
      return render.admin()
    else:
      return render.login(msg="first login as admin")

class count:
  def GET(self):
    session.count += 1
    return str(session.count)

class logout:
  def GET(self):
    session.user = ""
    session.kill()
    return render.login(msg="Logged out")

class login:
  def GET(self):
    if session.user != "":
      print(session.user)
      return "Already logged in: " + session.user
    return render.login(msg="Please enter user name and password")

  def POST(self):
    data=web.input()
    print(data)
    if data.user != "":
      user = db.users.find_one({"username": data.user})
      print(user)
      if user != None:
        session.user = data.user
        if user["password"] == data.passwd:
          return "Logged in: " + data.user
    return render.login(msg="User name/password not found, try again")

class newuser:
  def GET(self):
    return "get newuser?"

  def POST(self):
    data = web.input()
    print(data)
    if data.user != "" and data.passwd != "":
      db.users.update_one(
        {"username": data.user},
        {"$set": {"password": data.passwd}},
        upsert=True
      )
      return "User added: " + data.user
    else: render.admin()


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

db.users.update_one(
    {"username": "admin"},
    {"$set": {"password": "pass3"}},
    upsert=True
  )

if __name__ == "__main__":
    app.run()
