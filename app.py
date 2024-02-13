from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_route():
    name = request.args.get('name', '')
    return f"Hello {name}" if name else "Hello World"
   
if __name__ == '__main__':
    app.run(port=3000,host='0.0.0.0')
