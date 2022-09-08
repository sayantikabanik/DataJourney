### 🚌 DataJourney
Tutorial featuring Data engineering workflow and Open Source tools and technologies.
The example datasets are openly available online, metadata info is present in the `intake` catalog

### 🛠 Current workflows covered (subject to change)
- Packaging framework added
- Conda environment added
- GitHub actions configured
- Pre-commit hooks configured for code linting/formating
- Reading data from online sources using [intake](https://github.com/intake/intake)
- Sample pipeline built using [Dagster](https://github.com/dagster-io/dagster)
- Dashboarding using [holoviews](https://holoviews.org/gallery/index.html) + [panel](https://panel.holoviz.org/reference/index.html)

#### Codespaces configured
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
#### How to run the applications?

- Dagster UI app
```shell
cd analytics_framework/pipeline
```
```shell
dagit -f process.py
```
![Dagit UI output](./output/dagit_ui.png)

- Panel app
```shell
cd analytics_framework/dashboard
```
```shell
python simple_app.py
```
![Panel app output](./output/panel_app_stock.png)
