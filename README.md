<h1 align="center">

[![License](https://img.shields.io/badge/license-CC0%201.0%20Universal-blue)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Code of Conduct](https://img.shields.io/badge/Code_of_Conduct-Contributor%20Covenant-blue)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)\
[![CI](https://github.com/sayantikabanik/DataJourney/actions/workflows/CI.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/CI.yml)
[![github-repo-stats](https://github.com/sayantikabanik/DataJourney/actions/workflows/github-repo-stats.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/github-repo-stats.yml)
[![Deploy DataJourney Stats](https://github.com/sayantikabanik/DataJourney/actions/workflows/static.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/static.yml)
[![Lint prose](https://github.com/sayantikabanik/DataJourney/actions/workflows/review.yml/badge.svg)](https://github.com/sayantikabanik/DataJourney/actions/workflows/review.yml)

</h1>

<p align="center">
  <img src="./assets/DataJourney_logo_svg/dj_darkmode.svg" alt="DJ rocks" style="width:500px; height:600px;">
</p>


### 🚌 What's DataJourney?
DataJourney demonstrates how organizations can effectively manage and utilize data by harnessing the power of open-source technologies. It's designed to help navigate the complex landscape of data tools, offering a structured approach to building **scalable**, and **reproducible** data workflows.

Built on open-source principles, the framework guides users through essential steps—from **identifying** goals and **selecting tools** to **testing** and **customising** workflows. With its flexible, modular design, DataJourney can be tailored to individual needs, making it an invaluable toolkit for data professionals.

### 🧱 Design Philosophy (LEGO)
Built with additive, subtractive capabilities glued with open source.
Each layer has a certain strength of communication inbuilt

- PO (Base): Static home(s) to keep it together `(GitHub)`
- P1 (Tooling): Tooling, strings `(Powered by open source)`
- P2 (Maintenance + Monitoring): Env, automations `(Pixi + GHA)`
- P3 (Abstraction): Layer(s), CLI/task manager for users to interact with `(Pixi)`


![DJ Design](assets/design/dj_vision.png)

### 🛠 Current workflows covered
{✨= Experimental,
✅ = Implemented}

✅ `Python Packaging framework` design principles\
✅ `GitHub actions` configured\
✅ `Vale.sh` configured at PR level\
✅ `Pre-commit hooks` configured for code linting/formatting\
✅ Environment management via [pixi](https://prefix.dev/)\
✅ Reading data from online sources using [intake](https://github.com/intake/intake)\
✅ Sample pipeline built using [Dagster](https://github.com/dagster-io/dagster)\
✅ Building Dashboard using [holoviews](https://holoviews.org/gallery/index.html) + [panel](https://panel.holoviz.org/reference/index.html)\
✅ Exploratory data analysis (EDA) using [mito](https://www.trymito.io/)\
✅ Web UI build on [Flask](https://flask.palletsprojects.com/en/3.0.x/) \
✅ Web UI re-done and expanded with [FastHTML](https://docs.fastht.ml/)\
✅ Leverage AI models to analyse data [GitHub AI models Beta](https://docs.github.com/en/github-models/prototyping-with-ai-models)

### Quickly getting started with DataJourney

- Clone DJ `git@github.com:sayantikabanik/DataJourney.git`
- Switch directory `cd DataJourney`
- Download pixi : [prefix.dev](https://prefix.dev/)
- Activate env: `pixi shell`
- Install DJ framework locally `pixi run DJ_package`
- List all the tasks: `pixi task list`
- Execute a task from the list: `pixi run <TASK>`
- Execute a task with verbosity enabled: `pixi run -v <TASK>`

### Active `tasks` under DJ

- GIT_TOKEN_CHECK
- DJ_package
- DJ_pre_commit
- DJ_dagster
- DJ_fasthtml_app
- DJ_flask_app
- DJ_mito_app
- DJ_panel_app
- DJ_llm_analysis


#### 🔌 About pre-commit-hooks and activating
Just like the name suggests, pre-commit-hooks are designed to format the code based on PEP standards before committing. [More details](https://pre-commit.com/)

```shell
pixi run DJ_pre_commit
```
### Commands to run modules under DataJourney

#### Executing LLM script: Generate Recommendation got the stock data

```shell
pixi run DJ_llm_analysis
```

#### Dagster UI

```shell
pixi run DJ_dagster
```
![Dagit UI output](assets/pipeline/dagster_ui.png)

#### Panel app
```shell
pixi run DJ_panel_app
```

*NOTE:*
The dashboard generated is exported into HTML format and saved as [stock_price_twilio_dashboard](analytics_framework%2Fdashboard%2Fstock_price_twilio_dashboard.html)

![Panel app output](assets/dashboard/panel_app_stock.png)

#### Mito

To explore further visit [trymito.io](https://docs.trymito.io/)
```shell
pixi run DJ_mito_app
```

[//]: # (![mito output]&#40;assets/pipeline/mito_graph.png "Graph generated via mitosheet"&#41; ![mito output operation]&#40;assets/pipeline/mito_operations.png "Operations performed via mitosheet"&#41;)

<div style="display: flex; justify-content: space-between;">
    <img src="assets/pipeline/mito_graph.png" alt="mito_output" width="400"/>
    <img src="assets/pipeline/mito_operations.png" alt="mito_output" width="400"/>
</div>

#### Display all data sources present via web UI

```shell
# Run FastHTML app
pixi run DJ_fasthtml_app
```
![data_sources_fasthtml.png](assets/pipeline/data_sources_fasthtml.png)
