import web
import pymongo
import markdown

# configuration:
client = pymongo.MongoClient()
db = client["blog"]

urls = (
  '/', 'index',
  '/create', 'createpost',
  '/posts', 'posts',
  '/editform', 'editform',
  '/saveform', 'saveform'
)

renderglobals = {'markdown': markdown.markdown}
render = web.template.render('templates/', globals=renderglobals)

class index:
  def GET(self):
    return "Hello, world!"
    
class posts:
  def GET(self):
    return render.posts(db.posts.find())

class editform:
  def GET(self):
    return render.posts(db.posts.find())
    
  def POST(self):
    data=web.input()
    p = db.posts.find_one({"title": data["title"]})
    if p != None:
      return render.editform(post=p)
    else:
      return render.posts(db.posts.find())
      
class saveform:
  def POST(self):
    data=web.input()
    db.posts.update_one({"title": data["title"]},
        {"$set": {"content": data["content"]}}
      )
    return render.posts(db.posts.find())
    
class createpost:
  def GET(self):
    return render.createpost()
    
  def POST(self):
    data=web.input()
    print(data)
    print(db.posts.find_one({"title": data["title"]}))
    if db.posts.find_one({"title": data["title"]}) == None:
      db.posts.insert(data)
    else:
      return "Existing post; update?"
    return render.posts(db.posts.find())

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
