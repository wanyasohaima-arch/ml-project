# Diabetes Readmission Prediction

Full-stack ML teaching prototype. Predicts whether a diabetic patient is
readmitted to hospital within 30 days. Research/teaching use only, not for clinical use.

**Live demo (static UI only):** https://wanyasohaima-arch.github.io/ml-project/
**Repository:** https://github.com/wanyasohaima-arch/ml-project

## Architecture
Angular form (localhost:4200) → dev proxy → Flask API (127.0.0.1:5000) →
scikit-learn pipeline (preprocessing + Logistic Regression).
GitHub Actions runs backend tests and the Angular build; GitHub Pages hosts the
static Angular UI only. Predictions need Flask running locally.

## Dataset and model
- Diabetes 130-US hospitals dataset (`diabetic_data.csv`, not committed: 18 MB).
- Target: `readmitted == "<30"`. One row per patient; expired/hospice discharges removed.
- 15 input features, Logistic Regression with class weighting, test ROC-AUC ≈ 0.61.

## Run locally (Windows, PowerShell)
    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r backend\requirements.txt
    python backend\export_model.py      # needs data\diabetic_data.csv
    python backend\app.py               # Terminal 1
    cd frontend; npm install; ng serve --proxy-config proxy.conf.json   # Terminal 2

Then open http://localhost:4200.

## Tests
    python -m pytest backend\tests -q

## Limitations
Modest accuracy, tabular data from 1999-2008 US hospitals, no clinical validation.
GitHub Pages cannot run Flask, so the public page cannot make predictions.