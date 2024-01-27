from flask import Flask, send_from_directory, Response
import os

app = Flask(__name__, static_folder='website-html')

@app.route('/api/test', methods=['GET'])
def test():
    return {"message": "Hello from Flask!"}

@app.route("/ready", methods=['GET'])
def ready():
    return Response("Serwer gotowy", status=200)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/infopage')
def infopage():
    return send_from_directory(app.static_folder, 'infopage.html')

@app.route('/aboutme')
def aboutme():
    return send_from_directory(app.static_folder, 'aboutme.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)
