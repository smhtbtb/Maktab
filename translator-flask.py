from flask import Flask, request
import translators

app = Flask(__name__)


@app.route('/<to_lang>/<from_lang>/<provider>')
@app.route('/<to_lang>/<from_lang>', defaults={'provider': 'google'})
@app.route('/<to_lang>/', defaults={'from_lang': 'auto', 'provider': 'google'})
def translator(to_lang, from_lang='auto', provider='google'):
    res = getattr(translators, provider)
    text = request.args['text']

    return res(text, from_language=from_lang, to_language=to_lang)


app.run(host='0.0.0.0')
