from flask import Flask,request,jsonify,render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return "Hello, Flask App!"


#@app.run()

@app.route('/<name>/<int:age>')
def test(name,age):
    print("This is test function running")
    return f"Hello my name is,{name},and my age is{age}"

#app.run(debug=True)


# @app.route('/app')
# def home():
#     return '<h1>Hello,flask App!</h1><p>This is my testing app</p><p>This is my home page</p>'



@app.route('/handle',methods=['GET'])


def handle_args_kwargs():

    args_list = request.args.getlist('args')
    kwargs_dict = {key:value for key, value in request.args.items() if key != 'args'}
    result = {
        'args' : args_list,
        'kwargs' : kwargs_dict

    }
    return jsonify(result)

@app.route('/web')
def webpage():
    return render_template ('home.html')
        # @app.route('/about')
        # def aboutpage():
        #     return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
   




#http://127.0.0.1:5000/handle?args=apple&args=banana&color=red&size=large

