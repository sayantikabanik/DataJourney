import yaml
from flask import Flask, request, render_template_string

app = Flask(__name__)


# Function to load the YAML file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


# Load the YAML file
data = load_yaml('test.yml')  # Change 'data.yml' to your YAML file name


# Route to display the form and entries
@app.route('/', methods=['GET', 'POST'])
def index():
    selected_entries = []
    if request.method == 'POST':
        selected_keys = request.form.getlist('entries')
        selected_entries = [data[key] for key in selected_keys]

    return render_template_string('''
        <html>
        <body>
            <form method="post">
                <h2>Select Entries:</h2>
                {% for key in data.keys() %}
                    <input type="checkbox" name="entries" value="{{ key }}">{{ key }}<br>
                {% endfor %}
                <input type="submit" value="Submit">
            </form>

            {% if selected_entries %}
                <h2>Selected Entries:</h2>
                <ul>
                {% for entry in selected_entries %}
                    <li>{{ entry }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        </body>
        </html>
    ''', data=data, selected_entries=selected_entries)


if __name__ == '__main__':
    app.run(debug=True)
