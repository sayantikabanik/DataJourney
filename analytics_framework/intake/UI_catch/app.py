from fasthtml import FastHTML
from fasthtml.common import *
import yaml

app = FastHTML()

def load_yaml():
    with open('../catalog_entry.yml', 'r') as file:
        return yaml.safe_load(file)['sources']

# Function to parse the yaml file + render the required
# content in form HTML table, we are using pico css for styling
@app.get('/')
def home():
    data = load_yaml()
    source_name, source_url = [], []
    for key, value in data.items():
        source_name.append(key)
        source_url.append(value['metadata']['source_url'])
    return Html(
        Head(Title('Welcome to DataJourney'), Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css')),
        Body(
            H2("Data Source Present in this repository"),
            Table(
                Tr(
                    Th(B("Dataset Name")),
                    Th(B("DSource Info"))
                ),
                Tr(
                    Td(Ul(name) for name in source_name),
                    Td(Ul(A(url)) for url in source_url)
                )
            )
        )
    )


serve()
