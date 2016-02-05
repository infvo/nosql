import web
import pymongo

# configuration:
client = pymongo.MongoClient()
db = client["blog"]

urls = (
  '/', 'index',
  '/create', 'createpost'
)

render = web.template.render('templates/')

class index:
  def GET(self):
    return "Hello, world!"
    
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
    return "Almost done..."

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
  