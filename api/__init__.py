from flask import Flask , jsonify
from api.views.redflag import redflag

app = Flask(__name__)

# Registering the Blueprint
app.register_blueprint(redflag, url_prefix='/api/v1')


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message': 'Welcome to iReporter!!!'})