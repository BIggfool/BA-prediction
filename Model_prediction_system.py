import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('./logistic_model.pkl', 'rb'))

def run():
    img1 = Image.open('image.jpg')
    img1 = img1.resize((700,200))
    st.image(img1,use_column_width=False)
    st.title("Automatic Loan status prediction")

    ## Account No
    account_no = st.text_input('Account number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For Credit History
    cred_display = ('No','Yes')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit History",cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

    ## Loan AMount
    loan_amt = st.number_input("Loan Amount",value=0)

    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[ mar, edu, mon_income, co_mon_income, loan_amt, duration, cred]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello: " + fn + ' || '
                "Account number: "+account_no + ' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: " + fn +  ' || '
                "Account number: "+account_no + ' || '
                'Congratulations!! You are eligible to apply for the loan!'
            )

run()