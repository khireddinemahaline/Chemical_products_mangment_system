from web_dynamic import create_app
from flask_cors import CORS
from os import getenv

app = create_app()

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5002"}})

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    app.run(host=host, port=port, debug=True)
    
