import web
import json
import pymongo

client = pymongo.MongoClient()
db = client["test"]

urls = (
  '/', 'index',
  '/docenten', 'docenten',
  '/scholen', 'scholen',
  '/docentform', 'docentform',
  '/schoolform', 'schoolform'
)

render = web.template.render('templates/')

def addDocent(d):
  db.docenten.replace_one(
    {"naam": d["naam"]},
    d,
    True
  )

def addSchool(s):
  db.scholen.replace_one(
    {"naam": s["naam"]},
    s,
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

class scholen:
  def GET(self):
    coll = db["scholen"]
    return render.scholen(scholen=coll.find())

class docentform:
  def GET(self):
    return render.docentform()

  def POST(self):
    data = web.input()
    # print(data)
    data["vak"] = [x.strip() for x in data["vak"].split(",")]
    addDocent(data)
    return render.docenten(docenten=db.docenten.find())

class schoolform:
  def GET(self):
    return render.schoolform()

  def POST(self):
    data = web.input()
    print(data)
    addSchool(data)
    return render.scholen(scholen=db.scholen.find())

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
