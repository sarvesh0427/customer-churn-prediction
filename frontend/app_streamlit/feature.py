import streamlit as st
import joblib
import matplotlib.pyplot as plt
import pandas as pd

model = joblib.load("models/final_pipeline.pkl") 

def feature():
    st.title("Feature Importance")
    st.write('Top features influencing churn prediction:')
    st.caption("Higher importance = stronger influence on churn prediction")

    rf = model.named_steps["classifier"]
    pre = model.named_steps["preprocessor"]

    feature_names = pre.get_feature_names_out()
    importances = rf.feature_importances_

    imp_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(10)

    fig, ax = plt.subplots()
    ax.barh(imp_df["Feature"], imp_df["Importance"])
    ax.invert_yaxis()
    ax.set_title("Top 10 Important Features")

    st.write(fig) 