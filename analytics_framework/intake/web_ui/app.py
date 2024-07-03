# import yaml
# import ast
# from flask import Flask, request, render_template_string
#
# app = Flask(__name__)
#
#
# # Function to load the YAML file
# def load_yaml(file_path):
#     with open(file_path, 'r') as file:
#         return yaml.safe_load(file)
#
# # Load the YAML file
# data = load_yaml('../catalog_entry.yml')
#
#
# # Route to display the form and entries
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     selected_entries = []
#     if request.method == 'POST':
#         selected_keys = request.form.getlist('entries')
#         selected_entries = [data[ast.literal_eval(key.values())] for key in selected_keys]
#
#     return render_template_string('''
#         <html>
#         <body>
#         <form method="post" action="/submit">
#         {% for key, subkeys in data.items() %}
#             <strong>{{ key }}</strong><br>
#             {% for key2, subkey in subkeys.items() %}
#                  <input type="checkbox" name="entries" value="{{ subkey.metadata }}">{{ subkey.metadata }}<br>
#             {% endfor %}
#         {% endfor %}
#         <input type="submit" value="Submit">
#         </form>
#
#             {% if selected_entries %}
#                 <h2>Selected Entries:</h2>
#                 <ul>
#                 {% for entry in selected_entries %}
#                     <li>{{ entry }}</li>
#                 {% endfor %}
#                 </ul>
#             {% endif %}
#         </body>
#         </html>
#     ''', data=data, selected_entries=selected_entries)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
import yaml

app = Flask(__name__)

# Load the YAML data
def load_yaml():
    with open('../catalog_entry.yml', 'r') as file:
        return yaml.safe_load(file)['sources']

@app.route('/')
def index():
    data = load_yaml()
    sources = []
    for key, value in data.items():
        source_name = key
        source_url = value['metadata']['source_url']
        sources.append({'name': source_name, 'url': source_url})
    return render_template('index.html', sources=sources)

if __name__ == '__main__':
    app.run(debug=True)
