from flask import Flask, jsonify, request, render_template
import call_process
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/duplicatepair', methods = ["POST"])
def duplicatepair():
    input_q1 = request.form.get('input_q1')
    input_q2 = request.form.get('input_q2')
    query = call_process.query_point_creator(input_q1,input_q2)
    result = model.predict(query)[0]

    if result == 1:
        result = 'Duplicate'
    else:
        result = 'Not Duplicate'

    return render_template('index.html',result=result)


if __name__== '__main__':
    app.run(debug=True)