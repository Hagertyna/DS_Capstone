from flask import Flask , render_template

app = Flask(__name__)
#methods since its name of list
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images" + imagefile.filename
    imagefile.save(image_path)
if __name__ == '__main__':
    app.run(port=3000,debug=True)