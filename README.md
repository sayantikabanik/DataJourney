### 🚌 DataJourney
Tutorial featuring Data engineering workflow and Open Source tools and technologies.
The example datasets are openly available online, metadata info is present in the `intake` catalog

### 🛠 Current workflows covered (subject to change)
- Packaging framework added
- Conda environment added
- GitHub actions configured
- Pre-commit hooks configured for code linting/formating 
- Reading data from online sources using [intake](https://github.com/intake/intake)
- Simple pipeline built using [Dagster](https://github.com/dagster-io/dagster)

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

#### 🔌 About pre-commit-hooks and activating
Just like the name suggests, pre-commit-hooks are designed to format the code based on PEP standards before committing. [More details 🗒](https://pre-commit.com/)
```python
pip install pre-commit
pre-commit install
```
