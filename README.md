# Install

First, create the environment with `conda` from the YML file.
Then, use `pip` to install remaining requirements.
Finally, run the app.

```shell
conda env create -f conda_requirements.yml
pip install -r pip_requirements.txt
source activate flaskapisearch
python app.py```