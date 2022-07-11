### 🚌 DataJourney
Tutorial featuring Data engineering workflow and Open Source tools and technologies.
The example datasets are openly available online, metadata info is present in the `intake` catalog

### 🛠 Current workflows covered (subject to change)
- Packaging framework added
- Reading data from online http/https URL using [intake](https://github.com/intake/intake)
- Simple pipeline built using [Dagster](https://github.com/dagster-io/dagster)
- Interactive viz using [Panel](https://panel.holoviz.org/gallery/index.html) + [Holoviews](https://holoviews.org/) (coming soon)
- Conclusion and more

### Environment setup using conda:

#### Installing miniconda
- Visit : https://docs.conda.io/en/latest/miniconda.html

#### Create a conda environment
```shell
conda env create -f environment.yml
conda activate journey
```

#### Install the package locally 
```shell
pip install -e .
```