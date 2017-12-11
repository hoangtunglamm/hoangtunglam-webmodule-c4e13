from flask import Flask, render_template
import mlab
from mongoengine import *
app = Flask(__name__)

#1. COnnect to databse
mlab.connect()

#2. design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()
#3 try inset an item
# tv = Item(
#     title="cat set cu va dat",
#     image="http://genknews.genkcdn.vn/k:2015/1-mr-20586-b8b1e00c33bdcfeb-1445247771551/gamek-tieu-su-dien-tu-4-nut-huyen-thoai-bat-tu-cua-tuoi-tho-game-thu-viet.jpg",
#     description = "cat set cu nen dat",
#     price=3000000
# )
# tv.save()
# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)


@app.route('/')
def index():
    return render_template('index.html', title="TV cũ",
 image="http://static.baophapluat.vn/Uploaded/nguyenvantung/2014_08_06/gietme-bangoai-baophapluat13_XTVD.jpg")

@app.route("/list")
def title_list():
    return render_template("title_for.html", titles=["tv cũ", "cát xét cũ", "tổ ong cũ" ])

@app.route("/object")
def object():
    x={
        "title": "tv cu gia cao",
        "image": "https://s1.vietfones.vn/2017/05/54188_3a9a1525454f56a58be5d18954210fd8.jpg",
        "description": "tv gia dam bao rat cao",
    }

    return render_template("object.html", item=x)

@app.route('/object-list')
def object_list():
    # data = [
    #     {
    #     "title": "tv cu",
    #     "image": "http://via.placeholder.com/200x300",
    #     "description": "Tv dat vl luon"
    #     },
    #     {
    #     "title":  "Tu lanh cu",
    #     "image": "http://via.placeholder.com/200x300",
    #     "description": "lam lanh bang nhiet do phong"
    #     },
    #     {
    #     "title": "bo` cu",
    #     "image": "http://via.placeholder.com/200x300",
    #     "description": "cang ngay cang ngon"
    #     },
    # ]
    data = Item.objects()
    return render_template('object_list.html', items=data)
if __name__ == '__main__':
  app.run(debug=True)
