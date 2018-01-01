from flask import Flask, render_template, request
from forms.search_form import SearchForm
#from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyComplexPassword!234'
#bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()

  
    if form.validate_on_submit():
        base_url = 'https://api.coinmarketcap.com/v1/ticker/'
        base_url = 'https://api.coinmarketcap.com/v1/ticker/?limit='
        search_coin = form.stringfield.data
        api_url = base_url + search_coin

        results = requests.get(api_url).json()

        return render_template('index.html', results=results, form=form)

    return render_template('index.html', form=form, type=request.method)


if __name__ == '__main__':
    app.run(debug=True)