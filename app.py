
import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Loan Default Prediction",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOAD MODEL
# =========================================================

with open("loan_default_model.pkl", "rb") as file:
    saved_package = pickle.load(file)

model = saved_package["model"]
threshold = saved_package["threshold"]


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.header {
    text-align: center;
    padding: 20px 0px 10px 0px;
}

.header h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.header p {
    font-size: 18px;
    color: #777777;
}

.section {
    font-size: 24px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 15px;
}

.result {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header">

<h1>💳 Loan Default Prediction</h1>

<p>
Predict the likelihood of loan default using a Machine Learning model
</p>

</div>
""", unsafe_allow_html=True)

st.divider()


# =========================================================
# APPLICATION FORM
# =========================================================

with st.form("loan_prediction_form"):

    # -----------------------------------------------------
    # PERSONAL INFORMATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">👤 Personal Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35,
            step=1
        )

    with col2:
        employment_type = st.selectbox(
            "Employment Type",
            [
                "salaried",
                "self-employed",
                "business",
                "contract",
                "unemployed"
            ]
        )

    with col3:
        employment_years = st.number_input(
            "Employment Years",
            min_value=0.0,
            max_value=50.0,
            value=5.0,
            step=1.0
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        education = st.selectbox(
            "Education",
            [
                "graduate",
                "post-graduate",
                "high school",
                "diploma",
                "doctorate"
            ]
        )

    with col2:
        dependents = st.number_input(
            "Number of Dependents",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=1.0
        )

    with col3:
        credit_history_years = st.number_input(
            "Credit History (Years)",
            min_value=0,
            max_value=50,
            value=7,
            step=1
        )


    st.divider()


    # -----------------------------------------------------
    # FINANCIAL INFORMATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">💰 Financial Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        annual_income = st.number_input(
            "Annual Income (₹)",
            min_value=0.0,
            value=750000.0,
            step=10000.0
        )

    with col2:
        monthly_income = st.number_input(
            "Monthly Income (₹)",
            min_value=0,
            value=62500,
            step=1000
        )

    with col3:
        savings_balance = st.number_input(
            "Savings Balance (₹)",
            min_value=0.0,
            value=150000.0,
            step=10000.0
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        existing_loan_amount = st.number_input(
            "Existing Loan Amount (₹)",
            min_value=0.0,
            value=0.0,
            step=10000.0
        )

    with col2:
        existing_emi = st.number_input(
            "Existing EMI (₹)",
            min_value=0.0,
            value=0.0,
            step=1000.0
        )

    with col3:
        debt_to_income_ratio = st.number_input(
            "Debt-to-Income Ratio",
            min_value=0.0,
            max_value=3.0,
            value=0.40,
            step=0.01
        )


    st.divider()


    # -----------------------------------------------------
    # LOAN INFORMATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">🏦 Loan Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        loan_amount = st.number_input(
            "Loan Amount (₹)",
            min_value=0.0,
            value=750000.0,
            step=10000.0
        )

    with col2:
        loan_term_months = st.number_input(
            "Loan Term (Months)",
            min_value=12,
            max_value=300,
            value=48,
            step=12
        )

    with col3:
        interest_rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            max_value=30.0,
            value=11.5,
            step=0.1
        )

    col1, col2 = st.columns(2)

    with col1:
        loan_purpose = st.selectbox(
            "Loan Purpose",
            [
                "personal",
                "home",
                "auto",
                "education",
                "business",
                "medical"
            ]
        )

    with col2:
        collateral_value = st.number_input(
            "Collateral Value (₹)",
            min_value=0.0,
            value=0.0,
            step=10000.0
        )


    st.divider()


    # -----------------------------------------------------
    # CREDIT & REPAYMENT HISTORY
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">📊 Credit & Repayment History</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=900,
            value=720,
            step=1
        )

    with col2:
        previous_loan_count = st.number_input(
            "Previous Loan Count",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )

    with col3:
        previous_defaults = st.number_input(
            "Previous Defaults",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

    col1, col2 = st.columns(2)

    with col1:
        late_payments_12m = st.number_input(
            "Late Payments (Last 12 Months)",
            min_value=0,
            max_value=20,
            value=0,
            step=1
        )

    with col2:
        credit_card_utilization = st.number_input(
            "Credit Card Utilization",
            min_value=0.0,
            max_value=1.0,
            value=0.40,
            step=0.01
        )


    st.write("")

    # -----------------------------------------------------
    # PREDICTION BUTTON
    # -----------------------------------------------------

    submitted = st.form_submit_button(
        "🔍 Predict Loan Default",
        type="primary",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

if submitted:

    # Create dataframe with EXACT model feature names

    input_data = pd.DataFrame({
        "Age": [age],
        "Employment_Type": [employment_type],
        "Employment_Years": [employment_years],
        "Education": [education],
        "Dependents": [dependents],
        "Annual_Income": [annual_income],
        "Monthly_Income": [monthly_income],
        "Existing_Loan_Amount": [existing_loan_amount],
        "Existing_EMI": [existing_emi],
        "Credit_Score": [credit_score],
        "Savings_Balance": [savings_balance],
        "Debt_to_Income_Ratio": [debt_to_income_ratio],
        "Loan_Amount": [loan_amount],
        "Loan_Term_Months": [loan_term_months],
        "Interest_Rate": [interest_rate],
        "Loan_Purpose": [loan_purpose],
        "Collateral_Value": [collateral_value],
        "Previous_Loan_Count": [previous_loan_count],
        "Previous_Defaults": [previous_defaults],
        "Late_Payments_12M": [late_payments_12m],
        "Credit_Card_Utilization": [credit_card_utilization],
        "Credit_History_Years": [credit_history_years]
    })


    # -----------------------------------------------------
    # MODEL PREDICTION
    # -----------------------------------------------------

    probability = model.predict_proba(input_data)[0][1]

    prediction = int(probability >= threshold)

    probability_percentage = probability * 100


    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section">📋 Prediction Result</div>',
        unsafe_allow_html=True
    )


    if prediction == 1:

        st.error(
            f"⚠️ HIGHER DEFAULT RISK\n\n"
            f"Estimated probability of default: "
            f"{probability_percentage:.2f}%"
        )

    else:

        st.success(
            f"✅ LOWER DEFAULT RISK\n\n"
            f"Estimated probability of default: "
            f"{probability_percentage:.2f}%"
        )


    st.progress(
        min(int(probability_percentage), 100)
    )


    st.caption(
        f"Classification threshold used by the model: {threshold:.2f}"
    )
