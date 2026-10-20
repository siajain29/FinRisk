import sys
import os
import streamlit as st


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SRC_DIR = os.path.join(
    BASE_DIR,
    "src"
)

sys.path.append(SRC_DIR)

from predict import predict_risk


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="FinRisk",
    page_icon="💳",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("💳 FinRisk")
st.subheader("Credit Default Risk Prediction")

st.write(
    "Enter customer financial information to estimate "
    "the probability of credit default."
)

st.divider()


# --------------------------------------------------
# CUSTOMER PROFILE
# --------------------------------------------------

st.header("👤 Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    limit_bal = st.number_input(
        "Credit Limit",
        min_value=1000.0,
        value=50000.0,
        step=1000.0
    )

with col2:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

with col3:
    sex = st.selectbox(
        "Sex",
        options=[1, 2],
        format_func=lambda x: (
            "Male" if x == 1 else "Female"
        )
    )

col1, col2 = st.columns(2)

with col1:
    education = st.selectbox(
        "Education",
        options=[0, 1, 2, 3, 4, 5, 6],
        format_func=lambda x: {
            0: "Unknown",
            1: "Graduate School",
            2: "University",
            3: "High School",
            4: "Others",
            5: "Unknown",
            6: "Unknown"
        }[x]
    )

with col2:
    marriage = st.selectbox(
        "Marital Status",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Unknown",
            1: "Married",
            2: "Single",
            3: "Other"
        }[x]
    )


# --------------------------------------------------
# REPAYMENT HISTORY
# --------------------------------------------------

st.header("📊 Repayment History")

st.caption(
    "Positive values indicate months of repayment delay. "
    "0 indicates a current/revolving payment status."
)

pay_options = list(range(-2, 9))

col1, col2, col3 = st.columns(3)

with col1:
    pay_0 = st.selectbox(
        "Most Recent Repayment Status",
        pay_options,
        index=2
    )

with col2:
    pay_2 = st.selectbox(
        "Previous Month Repayment Status",
        pay_options,
        index=2
    )

with col3:
    pay_3 = st.selectbox(
        "2 Months Ago Repayment Status",
        pay_options,
        index=2
    )

col1, col2, col3 = st.columns(3)

with col1:
    pay_4 = st.selectbox(
        "3 Months Ago Repayment Status",
        pay_options,
        index=2
    )

with col2:
    pay_5 = st.selectbox(
        "4 Months Ago Repayment Status",
        pay_options,
        index=2
    )

with col3:
    pay_6 = st.selectbox(
        "5 Months Ago Repayment Status",
        pay_options,
        index=2
    )


# --------------------------------------------------
# BILL AMOUNTS
# --------------------------------------------------

st.header("💰 Bill Amounts")

col1, col2, col3 = st.columns(3)

with col1:
    bill_amt1 = st.number_input(
        "Latest Bill Amount",
        min_value=0.0,
        value=3913.0,
        step=100.0
    )

with col2:
    bill_amt2 = st.number_input(
        "Previous Bill Amount",
        min_value=0.0,
        value=3102.0,
        step=100.0
    )

with col3:
    bill_amt3 = st.number_input(
        "Bill Amount (2 Months Ago)",
        min_value=0.0,
        value=689.0,
        step=100.0
    )

col1, col2, col3 = st.columns(3)

with col1:
    bill_amt4 = st.number_input(
        "Bill Amount (3 Months Ago)",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

with col2:
    bill_amt5 = st.number_input(
        "Bill Amount (4 Months Ago)",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

with col3:
    bill_amt6 = st.number_input(
        "Bill Amount (5 Months Ago)",
        min_value=0.0,
        value=0.0,
        step=100.0
    )


# --------------------------------------------------
# PAYMENT AMOUNTS
# --------------------------------------------------

st.header("💵 Payment Amounts")

col1, col2, col3 = st.columns(3)

with col1:
    pay_amt1 = st.number_input(
        "Latest Payment Amount",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

with col2:
    pay_amt2 = st.number_input(
        "Previous Payment Amount",
        min_value=0.0,
        value=1500.0,
        step=100.0
    )

with col3:
    pay_amt3 = st.number_input(
        "Payment Amount (2 Months Ago)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

col1, col2, col3 = st.columns(3)

with col1:
    pay_amt4 = st.number_input(
        "Payment Amount (3 Months Ago)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

with col2:
    pay_amt5 = st.number_input(
        "Payment Amount (4 Months Ago)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

with col3:
    pay_amt6 = st.number_input(
        "Payment Amount (5 Months Ago)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )


# --------------------------------------------------
# INPUT DATA
# --------------------------------------------------

input_data = {
    "LIMIT_BAL": limit_bal,
    "SEX": sex,
    "EDUCATION": education,
    "MARRIAGE": marriage,
    "AGE": age,

    "PAY_0": pay_0,
    "PAY_2": pay_2,
    "PAY_3": pay_3,
    "PAY_4": pay_4,
    "PAY_5": pay_5,
    "PAY_6": pay_6,

    "BILL_AMT1": bill_amt1,
    "BILL_AMT2": bill_amt2,
    "BILL_AMT3": bill_amt3,
    "BILL_AMT4": bill_amt4,
    "BILL_AMT5": bill_amt5,
    "BILL_AMT6": bill_amt6,

    "PAY_AMT1": pay_amt1,
    "PAY_AMT2": pay_amt2,
    "PAY_AMT3": pay_amt3,
    "PAY_AMT4": pay_amt4,
    "PAY_AMT5": pay_amt5,
    "PAY_AMT6": pay_amt6
}


# --------------------------------------------------
# RISK ASSESSMENT
# --------------------------------------------------

st.divider()

st.header("🔍 Risk Assessment")

if st.button(
    "Assess Credit Risk",
    type="primary",
    use_container_width=True
):

    try:

        result = predict_risk(input_data)

        probability = float(
            result["default_probability"]
        )

        category = result["risk_category"]

        # ------------------------------------------
        # PREDICTION RESULT
        # ------------------------------------------

        st.subheader("Prediction Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Default Probability",
                f"{probability * 100:.2f}%"
            )

        with col2:
            st.metric(
                "Risk Category",
                category
            )

        st.progress(
            min(probability, 1.0),
            text=(
                f"Default probability: "
                f"{probability * 100:.2f}%"
            )
        )

        if category == "Low Risk":

            st.success(
                "🟢 Low Risk — The model estimates a "
                "relatively low probability of credit default."
            )

        elif category == "Medium Risk":

            st.warning(
                "🟡 Medium Risk — The customer shows "
                "moderate credit default risk."
            )

        else:

            st.error(
                "🔴 High Risk — The model estimates a "
                "high probability of credit default."
            )

        st.caption(
            "Risk bands: Low < 30% | "
            "Medium 30–60% | High ≥ 60%"
        )


        # ------------------------------------------
        # SHAP EXPLANATION
        # ------------------------------------------

        st.divider()

        st.subheader(
            "🧠 Why did the model make this prediction?"
        )

        explanation = result["explanation"].copy()

        feature_names = {

            "LIMIT_BAL": "Credit Limit",
            "SEX": "Gender",
            "EDUCATION": "Education Level",
            "MARRIAGE": "Marital Status",
            "AGE": "Age",

            "PAY_0": "Most Recent Repayment Status",
            "PAY_2": "Previous Month Repayment Status",
            "PAY_3": "2 Months Ago Repayment Status",
            "PAY_4": "3 Months Ago Repayment Status",
            "PAY_5": "4 Months Ago Repayment Status",
            "PAY_6": "5 Months Ago Repayment Status",

            "BILL_AMT1": "Latest Bill Amount",
            "BILL_AMT2": "Previous Bill Amount",
            "BILL_AMT3": "Bill Amount (2 Months Ago)",
            "BILL_AMT4": "Bill Amount (3 Months Ago)",
            "BILL_AMT5": "Bill Amount (4 Months Ago)",
            "BILL_AMT6": "Bill Amount (5 Months Ago)",

            "PAY_AMT1": "Latest Payment Amount",
            "PAY_AMT2": "Previous Payment Amount",
            "PAY_AMT3": "Payment Amount (2 Months Ago)",
            "PAY_AMT4": "Payment Amount (3 Months Ago)",
            "PAY_AMT5": "Payment Amount (4 Months Ago)",
            "PAY_AMT6": "Payment Amount (5 Months Ago)",

            "MAX_DELAY": "Maximum Repayment Delay",
            "N_LATE": "Number of Late Payments",
            "AVG_DELAY": "Average Repayment Delay",
            "AVG_BILL": "Average Monthly Bill",
            "AVG_PAYMENT": "Average Monthly Payment",
            "TOTAL_BILL": "Total Bill Amount",
            "TOTAL_PAYMENT": "Total Payment Amount",
            "UTILIZATION": "Credit Utilization",
            "PAYMENT_COVERAGE": "Payment Coverage",
            "BILL_TREND": "Bill Amount Trend",
            "PAYMENT_TREND": "Payment Amount Trend"
        }

        explanation["display_name"] = (
            explanation["feature"]
            .map(feature_names)
            .fillna(explanation["feature"])
        )


        # ------------------------------------------
        # TOP RISK-INCREASING FACTORS
        # ------------------------------------------

        increasing_risk = (
            explanation[
                explanation["shap_value"] > 0
            ]
            .sort_values(
                "shap_value",
                ascending=False
            )
            .head(5)
        )


        # ------------------------------------------
        # TOP RISK-DECREASING FACTORS
        # ------------------------------------------

        decreasing_risk = (
            explanation[
                explanation["shap_value"] < 0
            ]
            .sort_values(
                "shap_value"
            )
            .head(5)
        )


        col1, col2 = st.columns(2)


        # ------------------------------------------
        # INCREASING RISK
        # ------------------------------------------

        with col1:

            st.markdown(
                "### 🔴 Factors increasing risk"
            )

            if len(increasing_risk) == 0:

                st.info(
                    "No major factors are currently "
                    "increasing risk."
                )

            else:

                for _, row in increasing_risk.iterrows():

                    st.markdown(
                        f"**{row['display_name']}**"
                    )

                    st.caption(
                        f"Customer value: "
                        f"{row['value']:.2f}"
                    )

                    st.caption(
                        f"Model contribution: "
                        f"+{row['shap_value']:.4f}"
                    )


        # ------------------------------------------
        # DECREASING RISK
        # ------------------------------------------

        with col2:

            st.markdown(
                "### 🟢 Factors decreasing risk"
            )

            if len(decreasing_risk) == 0:

                st.info(
                    "No major factors are currently "
                    "reducing risk."
                )

            else:

                for _, row in decreasing_risk.iterrows():

                    st.markdown(
                        f"**{row['display_name']}**"
                    )

                    st.caption(
                        f"Customer value: "
                        f"{row['value']:.2f}"
                    )

                    st.caption(
                        f"Model contribution: "
                        f"{row['shap_value']:.4f}"
                    )


        # ------------------------------------------
        # SHAP NOTE
        # ------------------------------------------

        st.caption(
            "Positive contributions push the prediction "
            "toward higher default risk. Negative "
            "contributions push the prediction toward "
            "lower default risk."
        )


    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )
        # --------------------------------------------------
# MODEL PERFORMANCE
# --------------------------------------------------

st.divider()

st.header("📈 Model Performance")

st.write(
    "FinRisk compares three classification models and "
    "selects the model with the strongest predictive performance."
)


# Model comparison metrics
model_results = {
    "Logistic Regression": {
        "ROC-AUC": 0.7523,
        "PR-AUC": 0.5137,
        "Precision": 0.4441,
        "Recall": 0.6086,
        "F1": 0.5135
    },

    "Random Forest": {
        "ROC-AUC": 0.7640,
        "PR-AUC": 0.5276,
        "Precision": 0.5475,
        "Recall": 0.4864,
        "F1": 0.5152
    },

    "XGBoost": {
        "ROC-AUC": 0.7769,
        "PR-AUC": 0.5537,
        "Precision": 0.4526,
        "Recall": 0.6297,
        "F1": 0.5266
    }
}


# Create comparison dataframe
import pandas as pd

performance_df = pd.DataFrame(
    model_results
).T


# Display table
st.dataframe(
    performance_df.style.format("{:.4f}"),
    use_container_width=True
)


# Highlight selected model
st.success(
    "🏆 XGBoost was selected as the final model "
    "based on the highest ROC-AUC and PR-AUC."
)


# Key metrics
st.subheader("Final Model Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "ROC-AUC",
        "0.7769"
    )

with col2:
    st.metric(
        "PR-AUC",
        "0.5537"
    )

with col3:
    st.metric(
        "Recall",
        "62.97%"
    )

with col4:
    st.metric(
        "F1 Score",
        "0.5266"
    )


st.caption(
    "The model uses a 0.60 decision threshold for final "
    "binary risk classification. The displayed model metrics "
    "above use the standard 0.50 probability threshold."
)