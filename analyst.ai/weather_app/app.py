from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods=['POST', 'GET'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {
        'q': request.form.get("city"),
        'appid': 'b16890e24c52ee7c92998e168d3fc1dd',
        'units': 'metric'
    }

    response = requests.get(url, params=parameters)
    data = response.json()

    city = data['name']
    temperature = data['main']['temp']
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']

    return render_template("result.html", city=city, temperature=temperature, temp_max=temp_max, temp_min=temp_min)


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port = 5002)