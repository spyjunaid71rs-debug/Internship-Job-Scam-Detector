import joblib
import os

MODEL_PATH = "internship_scam_detector.pkl"

model = joblib.load(MODEL_PATH)

print("=" * 50)
print("✅ Model Loaded Successfully")
print("Path:", os.path.abspath(MODEL_PATH))
print("Total Features:", len(model.feature_names_in_))
print("=" * 50)