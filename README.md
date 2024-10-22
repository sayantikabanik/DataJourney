
[![CI](https://github.com/sayantikabanik/DataJourney/actions/workflows/CI.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/CI.yml)
[![code-complexity-check](https://github.com/sayantikabanik/DataJourney/actions/workflows/code-complexity-check.yml/badge.svg?event=pull_request)](https://github.com/sayantikabanik/DataJourney/actions/workflows/code-complexity-check.yml)
[![github-repo-stats](https://github.com/sayantikabanik/DataJourney/actions/workflows/github-repo-stats.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/github-repo-stats.yml)
[![Deploy DataJourney Stats](https://github.com/sayantikabanik/DataJourney/actions/workflows/static.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/static.yml)
[![Lint prose](https://github.com/sayantikabanik/DataJourney/actions/workflows/review.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/review.yml)

<p align="center">
  <img src="./assets/DataJourney_logo_svg/dj_darkmode.svg" alt="DJ rocks" style="width:500px; height:600px;">
</p>


### 🚌 What's DataJourney?
DataJourney demonstrates how organizations can effectively manage and utilize data by harnessing the power of open-source technologies. It's designed to help navigate the complex landscape of data tools, offering a structured approach to building **scalable**, and **reproducible** data workflows.

Built on open-source principles, the framework guides users through essential steps—from **identifying** goals and **selecting tools** to **testing** and **customising** workflows. With its flexible, modular design, DataJourney can be tailored to individual needs, making it an invaluable toolkit for data professionals.

### 🛠 Current workflows covered
{✨= Experimental,
✅ = Implemented}

✅ `Python Packaging framework` design principles\
✅ `Conda` environment added\
✅ `GitHub actions` configured\
✅ `Vale.sh` configured at PR level\
✅ `Pre-commit hooks` configured for code linting/formatting\
✅ Reading data from online sources using [intake](https://github.com/intake/intake)\
✅ Sample pipeline built using [Dagster](https://github.com/dagster-io/dagster)\
✅ Building Dashboard using [holoviews](https://holoviews.org/gallery/index.html) + [panel](https://panel.holoviz.org/reference/index.html)\
✅ Exploratory data analysis (EDA) using [mito](https://www.trymito.io/)\
✅ Analysing source code complexity using [Wily](https://wily.readthedocs.io/en/latest/index.html)\
✅ Web UI build on [Flask](https://flask.palletsprojects.com/en/3.0.x/) \
✅ Web UI re-done and expanded with [FastHTML](https://docs.fastht.ml/)\
✅ Leverage AI models to analyse data [GitHub AI models Beta](https://docs.github.com/en/github-models/prototyping-with-ai-models)

### 📊 Repository stats

⚙️ Managed by GitHub Action: https://github.com/jgehrcke/github-repo-stats \
⏳ Configured to run daily at 23:55:00 IST\
📬 Checkout daily reports generated: [DataJourney Stats on Web](https://sayantikabanik.github.io/DataJourney/)

### Dataset metadata/citations

- Global coral bleaching dataset: [Additional Info](https://www.bco-dmo.org/dataset/773466)
```txt
van Woesik, R., Burkepile, D. (2022) Bleaching and environmental data for global coral reef sites from 1980-2020. Biological and Chemical Oceanography Data Management Office (BCO-DMO). (Version 2) Version Date 2022-10-14 [if applicable, indicate subset used]. doi:10.26008/1912/bco-dmo.773466.2 [access date]
Terms of Use
This dataset is licensed under Creative Commons Attribution 4.0 (https://creativecommons.org/licenses/by/4.0/)
```

#### Codespaces configured
*Currently new pre-build images are disabled due to limited storage*

![Screenshot 2022-08-29 at 3 41 12 PM (2)](https://user-images.githubusercontent.com/17350312/187180872-881322ed-dfc7-478b-bd07-5fefc1642cb5.png)

### Environment setup using conda:

#### Installing miniconda
- Visit : https://docs.conda.io/en/latest/miniconda.html

#### Create a conda environment
```shell
conda env create -f environment.yml
```
```shell
conda activate journey
```

#### Install the package locally
```shell
pip install -e .
```

#### 🔌 About pre-commit-hooks and activating
Just like the name suggests, pre-commit-hooks are designed to format the code based on PEP standards before committing. [More details 🗒](https://pre-commit.com/)

```shell
pre-commit install
```
### How to run the applications?

#### Dagster UI
```shell
cd analytics_framework/pipeline
```
```shell
dagit -f process.py
```
![Dagit UI output](./output/dagit_ui.png)

#### Panel app
```shell
cd analytics_framework/dashboard
```
```shell
python simple_app.py
```
*NOTE:*
The dashboard generated is exported into HTML format and saved as `stock_price_dashboard.html`

![Panel app output](./output/panel_app_stock.png)

#### Mito

Before running the jupyter notebook `doc/mito_exp.ipynb`, run the below command
in your terminal to enable the installer. Might take some time to run.

To explore further visit [trymito.io](https://docs.trymito.io/)
```shell
python -m mitoinstaller install
```
![mito output](./output/mito_graph.png "Graph generated via mitosheet") ![mito output operation](./output/mito_operations.png "Operations performed via mitosheet")


#### Display all data sources present via web UI

```shell
# Instructions specific to FastHTML app
cd intake/web_ui_fasthtml
python app.py
```
```python
Link: http://localhost:5001
INFO:     Will watch for changes in these directories: ['../DataJourney/analytics_framework/intake/web_ui_fasthtml']
INFO:     Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
INFO:     Started reloader process [20071] using WatchFiles
INFO:     Started server process [20075]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
![Screenshot 2024-07-31 at 4 42 44 PM](https://github.com/user-attachments/assets/a1c977c9-1698-416c-8ac3-15fdbffa0b0a)
