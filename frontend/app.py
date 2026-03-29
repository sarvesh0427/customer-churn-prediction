import streamlit as st
import home
import about
# import feature


st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="centered",
    initial_sidebar_state="expanded"   # keeps sidebar fixed open
)
# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home","About"])
st.sidebar.markdown("---")


if section == 'Home':
    home.home()

elif section == "About":
    about.about()

# elif section == 'Feature Importance Chart':
#     feature.feature()


# ----- FIXED FOOTER -----
st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #444;
        z-index: 999;
    }
    </style>

    <div class="footer">
        Built with using Streamlit & ML
    </div>
    """,
    unsafe_allow_html=True
)


