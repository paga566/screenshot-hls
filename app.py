from flask import Flask, send_file
import subprocess, os, tempfile

app = Flask(__name__)

@app.route('/screenshot')
def screenshot():
    url = "https://ingest2-video.streaming-pro.com/demo/encode4/playlist.m3u8"
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    
    # Buscar ffmpeg en paths conocidos
    ffmpeg_paths = [
        "ffmpeg",
        "/usr/bin/ffmpeg",
        "/usr/local/bin/ffmpeg",
        "/nix/store/ffmpeg",
    ]
    
    import shutil
    ffmpeg_bin = shutil.which("ffmpeg")
    if not ffmpeg_bin:
        return "ffmpeg not found", 500
    
    subprocess.run([
        ffmpeg_bin, "-y",
        "-i", url,
        "-frames:v", "1",
        "-q:v", "2",
        tmp.name
    ], timeout=60)
    return send_file(tmp.name, mimetype="image/jpeg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))