from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')


def get_weather(city):
    """Fetch current weather + 5-day forecast for a city."""
    try:
        current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        current_res = requests.get(current_url, timeout=5)

        if current_res.status_code != 200:
            return None, "City not found. Please check the spelling and try again."

        current_data = current_res.json()

        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
        forecast_res = requests.get(forecast_url, timeout=5)
        forecast_data = forecast_res.json()

        daily_forecast = []
        seen_dates = set()
        for entry in forecast_data.get('list', []):
            date = entry['dt_txt'].split(' ')[0]
            time = entry['dt_txt'].split(' ')[1]
            if time == "12:00:00" and date not in seen_dates:
                daily_forecast.append({
                    'date': date,
                    'temp': round(entry['main']['temp']),
                    'description': entry['weather'][0]['description'].title(),
                    'icon': entry['weather'][0]['icon']
                })
                seen_dates.add(date)

        weather_info = {
            'city': current_data['name'],
            'country': current_data['sys']['country'],
            'temp': round(current_data['main']['temp']),
            'feels_like': round(current_data['main']['feels_like']),
            'humidity': current_data['main']['humidity'],
            'wind_speed': current_data['wind']['speed'],
            'description': current_data['weather'][0]['description'].title(),
            'icon': current_data['weather'][0]['icon'],
            'forecast': daily_forecast[:5]
        }
        return weather_info, None

    except requests.exceptions.RequestException:
        return None, "Couldn't reach the weather service. Please try again."


def get_exchange_rate(base_currency, target_currency, amount):
    """Convert an amount from base_currency to target_currency using Frankfurter (no API key needed)."""
    try:
        url = f"https://api.frankfurter.dev/v1/latest?base={base_currency}&symbols={target_currency}"
        res = requests.get(url, timeout=5)
        data = res.json()

        if res.status_code != 200 or target_currency not in data.get('rates', {}):
            return None, "Currency conversion failed. Check your currency codes (e.g. USD, INR, EUR)."

        rate = data['rates'][target_currency]
        converted = round(rate * amount, 2)

        return {
            'base': base_currency,
            'target': target_currency,
            'amount': amount,
            'rate': rate,
            'converted': converted
        }, None

    except requests.exceptions.RequestException:
        return None, "Couldn't reach the currency service. Please try again."


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    weather_info = None
    weather_error = None
    conversion_info = None
    conversion_error = None
    city = ''

    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'weather':
            city = request.form.get('city', '').strip()
            if city:
                weather_info, weather_error = get_weather(city)

        elif form_type == 'currency':
            base = request.form.get('base_currency', 'USD').upper()
            target = request.form.get('target_currency', 'INR').upper()
            amount = request.form.get('amount', '1')
            try:
                amount = float(amount)
                conversion_info, conversion_error = get_exchange_rate(base, target, amount)
            except ValueError:
                conversion_error = "Please enter a valid amount."

    return render_template(
        'dashboard.html',
        weather_info=weather_info,
        weather_error=weather_error,
        conversion_info=conversion_info,
        conversion_error=conversion_error,
        city=city
    )


@app.route('/api/city-search')
def city_search():
    query = request.args.get('q', '').strip()
    if len(query) < 2:
        return {'cities': []}

    try:
        url = f"https://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={WEATHER_API_KEY}"
        res = requests.get(url, timeout=5)
        data = res.json()

        if not isinstance(data, list):
            return {'cities': []}

        cities = []
        for place in data:
            label = place['name']
            if place.get('state'):
                label += f", {place['state']}"
            label += f", {place['country']}"
            cities.append(label)

        return {'cities': cities}
    except requests.exceptions.RequestException:
        return {'cities': []}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)