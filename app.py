from flask import Flask, render_template, jsonify
import json
from collections import defaultdict
import os

app = Flask(__name__)

# --- Load store locations from JSON config ---
DATA_FILE = 'store_locations.json'

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"Configuration file {DATA_FILE} not found.")

with open(DATA_FILE, 'r') as f:
    locations = json.load(f)

# --- Extract unique business units ---
business_units = sorted(set(loc['business_unit'] for loc in locations))

# --- Extract countries grouped by business unit ---
countries_by_bu = defaultdict(set)
for loc in locations:
    countries_by_bu[loc['business_unit']].add(loc['country'])
# Convert sets to sorted lists for template use
countries_by_bu = {k: sorted(list(v)) for k, v in countries_by_bu.items()}

# --- Set your Google Maps API Key here ---
GOOGLE_MAPS_API_KEY = "your-google-api-key"  # Replace with your real key

# --- Routes ---
@app.route('/')
def map_view():
    return render_template(
        'map.html',
        locations=locations,
        business_units=business_units,
        countries_by_bu=countries_by_bu,
        api_key=GOOGLE_MAPS_API_KEY
    )

# Optional: for debugging or external API use
@app.route('/api/locations')
def api_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
