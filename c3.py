from flask import Flask,jsonify # 导入这个包

app = Flask(__name__)  # 创建实例

a = 'zhu'
b = 1
# -->数据库
c = {'name':a,'age':b}

e = "song lei"
g = 18

f = {'name':e, 'age':g}


@app.route('/getuserinfo')   # 注册了一个路由 装饰器
def index():
    return jsonify(c)

@app.route('/',methods=['GET','POST'])
def song():
    return jsonify(f)

app.run()


"""
{
'song': song
"getuserinfo": index
}



"""
