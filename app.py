from flask import Flask, render_template, request, flash, redirect, url_for
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        # try:
        city = request.form['cityName']
        state_province_territory = request.form['state/province/territoryName']
        country = request.form['countryName']
        data = get_weather(city, state_province_territory, country)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)