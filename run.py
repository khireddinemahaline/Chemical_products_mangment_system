from web_dynamic import create_app
from os import getenv

app = create_app()

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    app.run(host=host, port=port, debug=True)
    
