<<<<<<< HEAD
""" Starts a Flask web app """
=======
#!/usr/bin/python3
>>>>>>> ca0d536a19f75eb02d6292a3c56069def2fc4f7e
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!<p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

=======

@app.route('/', strict_slashes=False)
def hello_hbnd():
    return "Hello HBND!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ca0d536a19f75eb02d6292a3c56069def2fc4f7e
