from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='', static_folder='../static',)


@app.route('/')
def entry():
  return send_from_directory('../static', './index.html')


# @app.route('/<path:path>')
# def send_files(path):
#   return send_from_directory('../static', path)


if __name__ == "__main__":
  app.run(debug=True)
