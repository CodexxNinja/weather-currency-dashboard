<div align="center">

# Weather & Currency Dashboard

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=28&duration=3500&pause=1000&color=0EA5E9&center=true&vCenter=true&width=800&lines=Real-Time+Weather+Dashboard;5-Day+Forecast+Visualization;Live+Currency+Converter;Flask+%7C+Chart.js+%7C+REST+APIs" />

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
</p>

</div>

---

##  Overview

> A full-stack Flask application that combines **live weather forecasting**, **interactive 5-day visualization**, and a **real-time currency converter** in one responsive dashboard.

---

##  Live Demo

> **Coming Soon** — Replace with your deployed application URL.

---

##  Features

###  Weather Dashboard
- Real-time weather conditions
- Temperature & feels like
- Humidity & wind speed
- Weather icons
- Smart city autocomplete
- Graceful error handling

###  5-Day Forecast
- Midday forecast filtering
- Interactive Chart.js line chart
- Daily forecast cards
- Temperature trend visualization

###  Currency Converter
- Real-time exchange rates
- Searchable currencies
- Server-side conversion
- Fast calculations

###  Production Ready
- API validation
- Network timeout handling
- Invalid city detection
- Invalid currency handling
- User-friendly feedback

---

##  Technology Stack

| Layer | Technologies |
|------|--------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Templates | Jinja2 |
| Visualization | Chart.js |
| APIs | OpenWeatherMap, Frankfurter API |

---

##  Architecture

```text
User
 │
 ├── Weather Search
 ├── Currency Conversion
 │
 ▼
Flask Backend
 │
 ├── OpenWeather API
 ├── Geocoding API
 └── Frankfurter API
 │
 ▼
Data Processing
 │
 ▼
Jinja2 Templates
 │
 ▼
Dashboard + Chart.js
```

---

##  Project Structure

```text
weather-currency-dashboard/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── static/
│   ├── css/style.css
│   └── js/script.js
└── templates/
    ├── base.html
    └── dashboard.html
```

---

##  Local Setup

```bash
git clone https://github.com/CodexxNinja/weather-currency-dashboard.git
cd weather-currency-dashboard

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create `.env`

```env
WEATHER_API_KEY=your_openweathermap_api_key
SECRET_KEY=your_secure_secret_key
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📄 License

Licensed under the **MIT License**.
