import pandas as pd


RAW_FEATURES = [
    "LIMIT_BAL",
    "SEX",
    "EDUCATION",
    "MARRIAGE",
    "AGE",
    "PAY_0",
    "PAY_2",
    "PAY_3",
    "PAY_4",
    "PAY_5",
    "PAY_6",
    "BILL_AMT1",
    "BILL_AMT2",
    "BILL_AMT3",
    "BILL_AMT4",
    "BILL_AMT5",
    "BILL_AMT6",
    "PAY_AMT1",
    "PAY_AMT2",
    "PAY_AMT3",
    "PAY_AMT4",
    "PAY_AMT5",
    "PAY_AMT6",
]


def create_features(df):
    """
    Create FinRisk features from the original 23 input features.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the original 23 dataset features.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the original features plus engineered features.
    """

    df = df.copy()

    pay_cols = [
        "PAY_0",
        "PAY_2",
        "PAY_3",
        "PAY_4",
        "PAY_5",
        "PAY_6",
    ]

    bill_cols = [
        "BILL_AMT1",
        "BILL_AMT2",
        "BILL_AMT3",
        "BILL_AMT4",
        "BILL_AMT5",
        "BILL_AMT6",
    ]

    payment_cols = [
        "PAY_AMT1",
        "PAY_AMT2",
        "PAY_AMT3",
        "PAY_AMT4",
        "PAY_AMT5",
        "PAY_AMT6",
    ]

    # Repayment behavior
    df["MAX_DELAY"] = df[pay_cols].max(axis=1)

    df["N_LATE"] = (
        df[pay_cols] > 0
    ).sum(axis=1)

    df["AVG_DELAY"] = (
        df[pay_cols].mean(axis=1)
    )

    # Bill/payment aggregates
    df["AVG_BILL"] = (
        df[bill_cols].mean(axis=1)
    )

    df["AVG_PAYMENT"] = (
        df[payment_cols].mean(axis=1)
    )

    df["TOTAL_BILL"] = (
        df[bill_cols].sum(axis=1)
    )

    df["TOTAL_PAYMENT"] = (
        df[payment_cols].sum(axis=1)
    )

    # Credit utilization
    df["UTILIZATION"] = (
        df["BILL_AMT1"].abs()
        / df["LIMIT_BAL"].clip(lower=1)
    )

    # Payment coverage
    df["PAYMENT_COVERAGE"] = (
        df["PAY_AMT1"]
        / df["BILL_AMT1"].abs().clip(lower=1)
    )

    # Financial trends
    df["BILL_TREND"] = (
        df["BILL_AMT1"] - df["BILL_AMT6"]
    )

    df["PAYMENT_TREND"] = (
        df["PAY_AMT1"] - df["PAY_AMT6"]
    )

    return df