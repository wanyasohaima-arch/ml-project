from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_csv(ROOT / "data" / "diabetic_data.csv", na_values=["?"], low_memory=False)

# Clean: one row per patient, drop patients who died / went to hospice
df = df[~df["discharge_disposition_id"].isin([11, 13, 14, 19, 20, 21])]
df = df.drop_duplicates(subset="patient_nbr", keep="first")

# Binary target: readmitted within 30 days
y = (df["readmitted"] == "<30").astype(int)

NUMERIC = ["time_in_hospital", "num_lab_procedures", "num_procedures",
           "num_medications", "number_outpatient", "number_emergency",
           "number_inpatient", "number_diagnoses"]
CATEGORICAL = ["race", "gender", "age", "A1Cresult", "insulin", "change", "diabetesMed"]
FEATURES = CATEGORICAL + NUMERIC
X = df[FEATURES].copy()

pre = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("sc", StandardScaler())]), NUMERIC),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="constant", fill_value="Unknown")),
                      ("oh", OneHotEncoder(handle_unknown="ignore"))]), CATEGORICAL),
])
pipe = Pipeline([("preprocess", pre),
                 ("model", LogisticRegression(max_iter=1000, class_weight="balanced"))])

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
pipe.fit(Xtr, ytr)
print("Test ROC-AUC:", round(roc_auc_score(yte, pipe.predict_proba(Xte)[:, 1]), 3))

Xte.dropna().head(1).to_csv(ROOT / "data" / "sample_inputs.csv", index=False)
out = ROOT / "backend" / "models" / "model_bundle.joblib"
joblib.dump({"pipeline": pipe, "features": FEATURES, "task": "classification",
             "model_version": "1.0"}, out)
print("Saved", out, "with", len(FEATURES), "features")