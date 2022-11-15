from flask import Flask , request , jsonify

app = Flask(__name__)
@app.route('/abc' ,methods=['GET' , 'POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/omkar' ,methods=['GET' , 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify(str(result))


if __name__ =='__main__':
    app.run()

"""
1) WAP to insert a record in SQL Table via API Database
2) WAP to update a record via api
3) WAP to delete a record via api
4) WAP to fetch  a record via api
5) All this things you have to do with Mongo DB as well
"""