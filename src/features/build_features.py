def create_features(df):

    df = df.copy()

    df["tenure_group"] = df["tenure"] // 12

    return df