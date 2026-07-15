// Render the 5-day forecast chart if data is present
const forecastCanvas = document.getElementById('forecastChart');

if (forecastCanvas) {
    const labels = JSON.parse(forecastCanvas.dataset.labels);
    const temps = JSON.parse(forecastCanvas.dataset.temps);

    new Chart(forecastCanvas, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Temperature (°C)',
                data: temps,
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.15)',
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#3b82f6',
                pointRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } },
                y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } }
            }
        }
    });
}

// ---------- CITY AUTOCOMPLETE ----------
const cityInput = document.getElementById('cityInput');
const suggestionsBox = document.getElementById('citySuggestions');
let debounceTimer;

if (cityInput) {
    cityInput.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        const query = cityInput.value.trim();

        if (query.length < 2) {
            suggestionsBox.innerHTML = '';
            return;
        }

        // Wait 300ms after typing stops before calling the API (avoids spamming requests)
        debounceTimer = setTimeout(() => {
            fetch(`/api/city-search?q=${encodeURIComponent(query)}`)
                .then(res => res.json())
                .then(data => {
                    suggestionsBox.innerHTML = '';
                    data.cities.forEach(city => {
                        const item = document.createElement('div');
                        item.classList.add('suggestion-item');
                        item.textContent = city;
                        item.addEventListener('click', () => {
                            cityInput.value = city.split(',')[0]; // use just the city name for the search
                            suggestionsBox.innerHTML = '';
                        });
                        suggestionsBox.appendChild(item);
                    });
                });
        }, 300);
    });

    // Hide suggestions when clicking elsewhere
    document.addEventListener('click', (e) => {
        if (e.target !== cityInput) {
            suggestionsBox.innerHTML = '';
        }
    });
}