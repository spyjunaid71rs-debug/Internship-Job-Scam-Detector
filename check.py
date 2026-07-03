# import joblib

# model = joblib.load("internship_scam_detector.pkl")
# feature_columns = joblib.load("feature_columns.pkl")

# print("Model Features :", len(model.feature_names_in_))
# print("PKL Features   :", len(feature_columns))

# print("\nAre they equal?")
# print(list(model.feature_names_in_) == feature_columns)

from utils.model_loader import model

print("\nTotal Features:", len(model.feature_names_in_))

print("\nFeature Names:\n")
for i, col in enumerate(model.feature_names_in_, 1):
    print(f"{i}. {col}")