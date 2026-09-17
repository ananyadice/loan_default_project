
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

/* =========================================================
   BANKING-STYLE UI
   Clean institutional design: navy, white, light grey
   ========================================================= */

:root {
    --bank-navy: #12345B;
    --bank-blue: #1D4E89;
    --bank-light-blue: #EAF2F8;
    --bank-border: #D8E0E8;
    --bank-text: #263746;
    --bank-muted: #667788;
    --bank-bg: #F4F6F8;
}

/* Page */
.stApp {
    background: var(--bank-bg);
    color: var(--bank-text);
}

.main .block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Top institutional bar */
.bank-topbar {
    background: var(--bank-navy);
    color: white;
    padding: 9px 22px;
    margin: -1.5rem -1rem 1.25rem -1rem;
    font-size: 13px;
    letter-spacing: 0.2px;
}

.bank-topbar-inner {
    max-width: 1180px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Header */
.header {
    background: white;
    border: 1px solid var(--bank-border);
    border-top: 4px solid var(--bank-navy);
    padding: 22px 30px 20px 30px;
    margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.header h1 {
    color: var(--bank-navy);
    font-size: 30px;
    font-weight: 650;
    margin: 0 0 5px 0;
    letter-spacing: -0.3px;
}

.header p {
    color: var(--bank-muted);
    font-size: 14px;
    margin: 0;
}

/* Section headings */
.section {
    color: var(--bank-navy);
    background: var(--bank-light-blue);
    border-left: 4px solid var(--bank-blue);
    font-size: 17px;
    font-weight: 650;
    padding: 11px 15px;
    margin: 18px 0 16px 0;
}

/* Form area */
div[data-testid="stForm"] {
    background: white;
    border: 1px solid var(--bank-border);
    border-radius: 2px;
    padding: 20px 24px 12px 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

/* Labels */
label {
    color: #34495E !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

/* Inputs */
div[data-baseweb="input"],
div[data-baseweb="select"] > div {
    border-color: #C9D3DD !important;
    border-radius: 2px !important;
    background: white !important;
}

div[data-baseweb="input"]:focus-within,
div[data-baseweb="select"]:focus-within {
    border-color: var(--bank-blue) !important;
    box-shadow: 0 0 0 1px var(--bank-blue) !important;
}

/* Selectbox text */
div[data-baseweb="select"] * {
    font-size: 14px;
}

/* Primary action button */
.stFormSubmitButton button {
    background: var(--bank-navy) !important;
    border: 1px solid var(--bank-navy) !important;
    border-radius: 2px !important;
    min-height: 44px;
    font-size: 14px !important;
    font-weight: 650 !important;
    letter-spacing: 0.1px;
}

.stFormSubmitButton button:hover {
    background: #0D2948 !important;
    border-color: #0D2948 !important;
}

/* Dividers */
hr {
    border-color: #DDE3E8 !important;
    margin: 22px 0 !important;
}

/* Result cards */
.result-card {
    background: white;
    border: 1px solid var(--bank-border);
    border-left: 5px solid var(--bank-blue);
    padding: 22px 25px;
    margin-top: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.result-card.high-risk {
    border-left-color: #B23A3A;
}

.result-title {
    font-size: 13px;
    color: var(--bank-muted);
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin-bottom: 7px;
}

.result-value {
    color: var(--bank-navy);
    font-size: 25px;
    font-weight: 700;
}

.result-subtitle {
    color: #526273;
    font-size: 14px;
    margin-top: 5px;
}

/* Progress bar */
div[data-testid="stProgress"] > div > div > div {
    background-color: var(--bank-blue) !important;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 2px !important;
    border-width: 1px !important;
}

/* Caption */
.stCaption {
    color: #71808F !important;
    font-size: 12px;
}

/* Footer */
.bank-footer {
    border-top: 1px solid var(--bank-border);
    margin-top: 30px;
    padding-top: 12px;
    text-align: center;
    color: #7A8793;
    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="bank-topbar">
    <div class="bank-topbar-inner">
        <span>RETAIL CREDIT SERVICES</span>
        <span>Credit Assessment Portal</span>
    </div>
</div>

<div class="header">
    <h1>Loan Default Risk Assessment</h1>
    <p>Credit evaluation based on applicant, financial and repayment information</p>
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
        '<div class="section">1. Personal Information</div>',
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
        '<div class="section">2. Financial Information</div>',
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
        '<div class="section">3. Loan Information</div>',
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
        '<div class="section">4. Credit & Repayment History</div>',
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
        "Assess Default Risk",
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
        '<div class="section">Credit Assessment Result</div>',
        unsafe_allow_html=True
    )


    if prediction == 1:

        st.markdown(
            f"""
            <div class="result-card high-risk">
                <div class="result-title">Assessment Outcome</div>
                <div class="result-value">Higher Default Risk</div>
                <div class="result-subtitle">
                    Estimated probability of default: <strong>{probability_percentage:.2f}%</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Assessment Outcome</div>
                <div class="result-value">Lower Default Risk</div>
                <div class="result-subtitle">
                    Estimated probability of default: <strong>{probability_percentage:.2f}%</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.progress(
        min(int(probability_percentage), 100)
    )


    st.caption(
        f"Classification threshold used by the model: {threshold:.2f}"
    )


st.markdown("""
<div class="bank-footer">
    Internal Credit Assessment System &nbsp;|&nbsp; Risk classification generated by the configured ML model
</div>
""", unsafe_allow_html=True)
