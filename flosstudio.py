# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Submission website for flosstudio
"""

import datetime
import os

from flask import Flask, render_template, request
from ruamel.yaml import YAML

app = Flask(__name__)

def parse_comma_list(text):
    """
    Reduce comma-separated entries onto a list
    """
    if text:
        return [i.strip() for i in text.split(',')]
    return []

def save_file(entry):
    """
    Save submission to file
    """
    name = entry['Name'].lower().replace(' ', '-')
    yaml = YAML()
    yaml.default_flow_style = False
    yaml.explicit_start = True
    yaml.sort_keys = False
    yaml.indent(mapping=2, offset=2, sequence=2)
    with open(
            os.path.join('entries',
                         f'{name}-{datetime.datetime.now()}.yaml'),
            'w') as yaml_file:
        yaml.dump(entry, yaml_file)

@app.route('/')
def index():
    """
    Homepage
    """
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """
    Submission
    """
    if request.method == 'POST':
        entry = {k:v for k, v in {
            'Name': request.form.get('name'),
            'Summary': request.form.get('summary'),
            'Description': request.form.get('description'),
            'Authors': parse_comma_list(request.form.get('authors')),
            'URL': request.form.get('ur'),
            'Licenses': request.form.getlist('licenses'),
            'Formats': request.form.getlist('formats'),
            'Latest version': request.form.get('version'),
            'Last updated': request.form.get('updated'),
            'Categories': request.form.getlist('categories'),
            'Repositories': request.form.getlist('repositories'),
            'Notes': request.form.get('notes'),
            'Entry editors': request.form.get('editor-name')
        }.items() if v}
        save_file(entry)
        return render_template('submit.html', success=True)
    return render_template('submit.html')
