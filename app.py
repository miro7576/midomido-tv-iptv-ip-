echo 'from flask import Flask, redirect

app = Flask(__name__)

# الرابط الخاص بك الذي يعمل بكفاءة عالية في المتصفح
STREAM_URL = "https://ibo.lynxiptv.com/live/777685932038/VJQBOrw29f/255242.m3u8"

@app.route("/", methods=["GET"])
def index():
    # توجيه المتصفح فورا لفتح الرابط مباشرة بكفاءته العالية وبدون جدار حماية
    return redirect(STREAM_URL, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)' > app.py
