import web
import json
import pymongo

client = pymongo.MongoClient()
db = client["test"]

urls = (
  '/', 'index',
  '/docenten', 'docenten',
  '/form', 'form'
)

render = web.template.render('templates/')

def addDocent(d):
  db.docenten.replace_one(
    {"naam": d["naam"]},
    d,
    True
  )

class index:
  def GET(self):
    return "Hello, world!"

class docenten:
  def GET(self):
    coll = db["docenten"]
    result = []
    for docent in coll.find():
      # normalize docent["vak"] to a list:
      if not isinstance(docent["vak"], list):
        docent["vak"] = [docent["vak"]]
      result.append(docent)
    return render.docenten(docenten=result)

class form:
  def GET(self):
    return render.form()

  def POST(self):
    data = web.input()
    # print(data)
    data["vak"] = [x.strip() for x in data["vak"].split(",")]
    addDocent(data)
    return render.docenten(docenten=db.docenten.find())

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
