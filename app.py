from application import app
from application.characters import route

if __name__ == "__main__":
    app.run(host="0.0.0.0") # <- host="0.0.0.0" is only for docker