from flask import Flask, render_template, request
from forms.search_form import SearchForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyComplexPassword!234'


@app.route('/', methods=['GET', 'POST'])
def index():
    # Load the custom form;
    # Forms are python classes that inherit from FlaskForm
    form = SearchForm()
  
    # When the form is POST'ed from the site, the POST is back
    # to this route. If all inputs are valid, the logic block is entered
    if form.validate_on_submit():
        # Call coinmarketcap.com for number of coins
        # submitted in the form
        base_url = 'https://api.coinmarketcap.com/v1/ticker/?limit='
        search_coin = form.stringfield.data
        api_url = base_url + search_coin

        # Results is a `list` of `dict`. [{k:v..}, ..]
        results = requests.get(api_url).json()

        # Return the same page, blank form and all results
        return render_template('index.html', results=results, form=form)

    return render_template('index.html', form=form, type=request.method)


if __name__ == '__main__':
    app.run(debug=True)