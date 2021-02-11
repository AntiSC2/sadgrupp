from jinja2 import Template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    template = Template('Hello {{ name }}!')
    html = template.render(name='Sebastian')
    return html
