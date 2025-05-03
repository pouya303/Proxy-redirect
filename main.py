from flask import Flask, request, Response, redirect, render_template_string
import requests
import threading
import time

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>در حال پخش ویدیو...</title>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      background: white;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: sans-serif;
      color: #444;
    }
  </style>
</head>
<body>
  <h1>در حال بارگذاری ویدیو...</h1>
  <script>
    setTimeout(function() {
      window.location.href = "https://www.google.com/search?q=فیلم+مسافران";
    }, 17000);
  </script>
</body>
</html>
'''

@app.route("/start")
def start():
    def background_request():
        try:
            requests.get("https://instagram.igwtch.icu?video=986907192", timeout=10)
        except:
            pass

    threading.Thread(target=background_request).start()
    return render_template_string(TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=3000)