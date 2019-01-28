from flask import Flask, render_template,request,redirect,session  # 导入这个包

app = Flask(__Name__)  # 创建实例
app.secret_key="zhuzhiqun"
app.debug = True

user_dict = [
    {"name":"laoma","pwd":"123"},
    {"name":"wangjiao","pwd":"456"}
]

@app.route("/index")
def index():
    user = session.get("info")
    if user:
        return render_template("index.html",name=user)
    else:
        return redirect("/login")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',name='laoma')
    else:
        user = request.form.get("name")
        pwd = request.form.get("pwd")
        print(user)
        if user =="laoma" and pwd == "123":
            session["info"] = user
            return redirect("/index")
        if user == "wangjiao" and pwd == "456":
            return "login ok wangjiao"
        return redirect("/login")


app.run(port=8080)


"""
{
'song': song
"getuserinfo": index
}



"""
