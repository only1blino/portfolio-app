import streamlit as st
st.set_page_config(page_title="Blino's Portfolio", page_icon="👌", layout="wide")

st.title(body="🫥 **Blino's** Portfolio — *Dashboard*", anchor="home", help="yetty has a big head")
st.header("Introduction: Proffessional Summary!")
st.subheader("Work Experience")

st.markdown('''  Work experience
Virtual Property Manager,ARORA PROPERTIES LIMITE
rental residential property
Real Estate
D Oct 2023 - Present (2y)
Airtable Google Sheets Zendesk Trello Quickbooks
sana Notion Google Workspace
* Managed property marketing and leasing projects
, increasing occupancy rates through the
implementation of a digital management system that enhanced efficiency by 30%.
* Oversaw property marketing and leasing to attract high-quality tenants
, utilizing targeted strategies
that led to a 20% boost in tenant retention.
* Handled maintenance duties and administrative tasks
,
streamlining processes to enhance overall
efficiency by 30%.
* Managed tenant inquiries
, reducing legal issues to zero by implementing a digital complaint
management system that improved response times by
0%.
* Developed a cashflow system to optimize asset performance and reduce expenses by 15% through
financial analyses
.
* Introduced a streamlined complaint system via a joint Whats
pp group
, resulting in a 5
0%
improvement in resolution time with digital tools''')

st.header(f"Contact Form")
name=st.text_input("Enter your name", placeholder="e.g. Yetunde")
phone_number=st.text_input("Enter your phone number", placeholder="e.g. 0800346782356")
email_address=st.text_input("Enter your email address", placeholder="e.g. tuundr@xyyz.com")
if st.button("Submit"):
    if name and phone_number and email_address:
        st.success(f"Hello, {name}! 👋 i will contact you soon 🫥")
        st.balloons()