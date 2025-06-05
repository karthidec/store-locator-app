# store-locator-app

**Cloud SDK setup(local)**
  gcloud auth login
  gcloud config set project YOUR_PROJECT_ID
  gcloud config set run/region us-central1

**Deploy to Cloud Run**

  gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/store-locator
  
  gcloud run deploy store-locator \
    --image gcr.io/YOUR_PROJECT_ID/store-locator \
    --platform managed \
    --allow-unauthenticated

**Add Your Google Maps API Key (Cloud-Safe)**
  Replace the placeholder in app.py with:
  
  import os
  GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY", "")
  Then deploy using:
  
  gcloud run deploy store-locator \
    --image gcr.io/YOUR_PROJECT_ID/store-locator \
    --platform managed \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_MAPS_API_KEY=your_actual_maps_key
