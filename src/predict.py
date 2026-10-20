import os
import joblib
import numpy as np
import pandas as pd
import shap

from feature_engineering import create_features


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "finrisk_xgboost.pkl"
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

def load_model():
    return joblib.load(MODEL_PATH)


# --------------------------------------------------
# RISK CATEGORY
# --------------------------------------------------

def get_risk_category(probability):

    if probability < 0.30:
        return "Low Risk"

    elif probability < 0.60:
        return "Medium Risk"

    return "High Risk"


# --------------------------------------------------
# PREDICT RISK
# --------------------------------------------------

def predict_risk(input_data):

    bundle = load_model()

    model = bundle["model"]
    feature_columns = bundle["feature_columns"]

    # Convert input into DataFrame
    df = pd.DataFrame([input_data])

    # Create engineered features
    df = create_features(df)

    # Ensure exact feature order
    df = df[feature_columns]

    # Predict probability
    probability = float(
        model.predict_proba(df)[0, 1]
    )

    # Determine risk category
    category = get_risk_category(probability)

    # --------------------------------------------------
    # SHAP EXPLANATION
    # --------------------------------------------------

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(df)

    shap_values = np.asarray(shap_values)

    # Handle possible extra dimensions
    if shap_values.ndim == 3:
        shap_values = shap_values[0, :, 1]

    else:
        shap_values = shap_values[0]

    # Create explanation DataFrame
    explanation = pd.DataFrame({
        "feature": feature_columns,
        "value": df.iloc[0].values,
        "shap_value": shap_values
    })

    # Sort by absolute contribution
    explanation["abs_shap"] = (
        explanation["shap_value"].abs()
    )

    explanation = explanation.sort_values(
        "abs_shap",
        ascending=False
    )

    return {
        "default_probability": probability,
        "risk_category": category,
        "explanation": explanation
    }