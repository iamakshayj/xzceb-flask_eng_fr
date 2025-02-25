from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    englishToFrench(textToTranslate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    frenchToEnglish(textToTranslate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
   return render_template('home.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
