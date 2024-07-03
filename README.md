### 🚌 DataJourney
Tutorial featuring Data engineering workflow and Open Source tools and technologies.
The example datasets are openly available online, metadata info is present in the `intake` catalog

🪸 **upcoming: analysis on coral bleaching**

### 🛠 Current workflows covered (✨ represents: experimental)
✅ Packaging framework added\
✅ Conda environment added\
✅ GitHub actions configured\
✅ Pre-commit hooks configured for code linting/formating\
✅ Reading data from online sources using [intake](https://github.com/intake/intake)\
✅ Sample pipeline built using [Dagster](https://github.com/dagster-io/dagster)\
✅ Building Dashboard using [holoviews](https://holoviews.org/gallery/index.html) + [panel](https://panel.holoviz.org/reference/index.html)\
✅ Exploratory data analysis (EDA) using [mito](https://www.trymito.io/)\
✨ [WIP] Analysing source code complexity using [Wily](https://wily.readthedocs.io/en/latest/index.html)\
✨ [WIP]: Interesting viz(s) using [Quarto](https://quarto.org/)

### 📊 Repository stats 

⚙️ Managed by GitHub Action: https://github.com/jgehrcke/github-repo-stats \
⏳ Configured to run daily at 23:55:00 IST\
📬 Checkout daily reports generated: [PDF Report](https://github.com/sayantikabanik/DataJourney/blob/github-repo-stats/sayantikabanik/DataJourney/latest-report/report.pdf)\
🗳️ Supplementary details regarding stats/reports generated present [here](https://github.com/sayantikabanik/DataJourney/tree/github-repo-stats/sayantikabanik/DataJourney)

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
python app.py
```
<img width="751" alt="Screenshot 2024-07-03 at 9 27 30 AM" src="https://github.com/sayantikabanik/DataJourney/assets/17350312/180ae07b-3525-4466-bfe7-bc6d2284391b">
