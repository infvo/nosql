import web
import json
import pymongo

client = pymongo.MongoClient()
db = client["test"]

urls = (
  '/', 'index',
  '/docenten', 'docenten'
)

class index:
  def GET(self):
    return "Hello, world!"

class docenten:
  def GET(self):
    coll = db["docenten"]
    result = []
    for d in coll.find():
      docend = d
      del docent["_id"]   # not JSON serializable
      result.append(docent)
    return(json.dumps(result))


if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
