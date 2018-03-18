import os
import codecs
from markdown import markdown
from flask import Flask, render_template, redirect, abort, Markup
from config import STORAGE, PORT


app = Flask(__name__)


storage = os.path.expanduser(STORAGE)
if not os.path.exists(storage): os.mkdir(storage)


def listfiles():
    files = os.listdir(storage)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(storage, x)), reverse=True)
    return files


@app.template_filter('marked')
def marked(content):
    return Markup(markdown(
        content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.nl2br',
            'markdown.extensions.toc'
        ]
    ).replace('<table>', '<table class="table">'))


@app.route('/')
def index():
    files = listfiles()
    if len(files) == 0:
        abort(400, 'No file found in: '+storage)
    return redirect(files[0])


@app.route('/<filename>')
def display_file(filename):
    splitted, ext = filename.split('.'), None
    if len(splitted) > 1: ext = splitted.pop().lower()
    name = '.'.join(splitted)

    filepath = os.path.join(storage, filename)

    if not os.path.isfile(filepath):
        abort(404, filepath+' is not a file.')
    with codecs.open(filepath, encoding='latin1') as f:
        content = f.read()
    return render_template('display_file.html',
            files=listfiles(), name=name, content=content, ext=ext)


if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT, debug=True)