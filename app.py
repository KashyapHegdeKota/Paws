from flask import Flask,render_template,redirect,request
from pymongo import MongoClient
from flask_pymongo import PyMongo
app =Flask(__name__)

def signup(email, password):
    client = MongoClient("mongodb+srv://dbuser:9jgKjkfq3AG6E17c@cluster0.lpjcq.mongodb.net/CodeX?retryWrites=true&w=majority")
    mydb = client["CodeX"]
    mycol = mydb["CodeX"]   
    user_data= {"email":email,"password":password}
    mycol.insert_one(user_data)

def get_data(email, passwd): 
    client = MongoClient("mongodb+srv://dbuser:9jgKjkfq3AG6E17c@cluster0.lpjcq.mongodb.net/CodeX?retryWrites=true&w=majority")
    mydb=client["CodeX"]
    mycol = mydb["CodeX"]
    y = mycol.find()
    for data in y:
        if str(data["email"]) == str(email) and str(data["password"])==str(passwd):
            return True

@app.route('/index.html')
def index() :
    return render_template('index.html')
@app.route('/index')
def index1() :
    return render_template('index.html')
@app.route('/about')
def about() :
    return render_template('about.html')
@app.route('/about.html')
def about2() :
    return render_template('about.html')
@app.route('/shop')
def shop() :
    return render_template('shop.html')
@app.route('/shop.html')
def shop2() :
    return render_template('shop.html')
@app.route('/videos')
def videos() :
    return render_template('videos.html')
@app.route('/videos.html')
def videos2() :
    return render_template('videos.html')
@app.route('/adopt')
def adopt():
    return render_template("adopt.html")
@app.route('/adopt.html')
def adopt2():
    return render_template("adopt.html")
@app.route('/breeds_of_dogs.html')
def bod():
    return render_template("breeds_of_dogs.html")
@app.route('/breeds_of_dogs')
def bod2():
    return render_template("breeds_of_dogs.html")
@app.route('/breed_of_cats.html')
def boc():
    return render_template("breed_of_cats.html")
@app.route('/breed_of_cats')
def boc2():
    return render_template("breed_of_cats.html")
@app.route('/type_of_birds.html')
def tob():
    return render_template("type_of_birds.html")
@app.route('/type_of_birds')
def tob2def():
    return render_template("type_of_birds.html")

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        password = data.get("password")
        confirm = get_data(email,password)
        confirm = True
        if confirm == True:
            return redirect("/index")
        else:
            return "<h1>Does not work </h1>"

@app.route('/',methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template('sign_up.html')
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        password = data.get("password")
        c_password = data.get("c_password")
        if password== c_password:
            signup(email,password)
            return redirect("/login")
            



if __name__=='__main__':
    app.secret_key='Code-X'
    app.run(debug=True)

