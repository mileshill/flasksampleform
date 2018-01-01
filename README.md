# Install

Clone the repo.
Create the environment with `conda` from the YML file.
Use `pip` to install remaining requirements.
Finally, run the app.

```shell
git clone https://github.com/mileshill/flasksampleform
conda env create -f conda_requirements.yml
pip install -r pip_requirements.txt
source activate flaskapisearch
python app.py