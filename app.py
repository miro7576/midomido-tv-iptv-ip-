echo 'from flask import Flask, render_template_string

app = Flask(__name__)

# رابط فيديو سريع جدا ومفتوح الحماية تماما للتأكد من عمل الموقع
STREAM_URL = "https://vt.tiktok.com/ZSQVqceFw/"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok Video Test</title>
    <style>
        html, body { background-color: #000000; margin: 0; padding: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden; }
        .video-container { width: 100%; max-width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; }
        video { width: 100%; height: auto; max-height: 100vh; aspect-ratio: 16 / 9; background: #000000; }
    </style>
</head>
<body>
    <div class="video-container">
        <!-- مشغل فيديو مباشر يعرض كود التيك توك تلقائيا -->
        <video id="video" controls autoplay playsinline loop preload="auto">
            <source src="{{ stream_url }}" type="video/mp4">
            متصفحك لا يدعم تشغيل هذا الفيديو.
        </video>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE, stream_url=STREAM_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)' > app.py
