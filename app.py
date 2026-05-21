from flask import Flask, send_file
import subprocess, os, tempfile

app = Flask(__name__)

@app.route('/screenshot')
def screenshot():
    url = "https://ingest2-video.streaming-pro.com/demo/encode4/playlist.m3u8"
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    subprocess.run([
        "ffmpeg", "-y",
        "-i", url,
        "-frames:v", "1",
        "-q:v", "2",
        tmp.name
    ], timeout=30)
    return send_file(tmp.name, mimetype="image/jpeg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))