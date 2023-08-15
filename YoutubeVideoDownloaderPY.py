#incio
from flask import Flask, request
from flask import render_template
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/procesar", methods=["POST"])
def procesar():
        texto = request.form.get("URL")
        video = YouTube(texto)
        video.streams.filter(file_extension='mp4',res='720p').first().download("C:\\Users\\Hidari\\Downloads")
        return render_template("done.html")

@app.route("/procesar2", methods=["POST"])
def procesar2():
        texto = request.form.get("URLAudio")
        video = YouTube(texto)
        video.streams.filter(only_audio=True).first().download("C:\\Users\\Hidari\\Downloads")
        return render_template("done.html")

@app.route("/procesar3", methods=["POST"])
def procesar3():
      return render_template ("home.html")
if __name__ == "__main__":
    app.run()


   


