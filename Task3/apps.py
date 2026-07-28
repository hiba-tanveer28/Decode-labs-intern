import streamlit as st

from password_logic import generate_password




st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered"
)



st.markdown(
    """
    <style>

    .stApp {
        background-color: #0B1120;
    }

    .block-container {
        max-width: 800px;
        padding-top: 3rem;
    }

    .main-title {
        text-align: center;
        color: #F8FAFC;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 8px;
    }

    .subtitle {
        text-align: center;
        color: #94A3B8;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .section-title {
        color: #E2E8F0;
        font-size: 21px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .password-box {
        background-color: #020617;
        border: 1px solid #334155;
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        color: #38BDF8;
        font-size: 24px;
        font-weight: bold;
        letter-spacing: 2px;
        word-break: break-all;
    }

    </style>
    """,
    unsafe_allow_html=True
)




st.markdown(
    '<div class="main-title">'
    'Password Generator'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create a random password with letters, numbers, '
    'and special characters.'
    '</div>',
    unsafe_allow_html=True
)


st.divider()



st.markdown(
    '<div class="section-title">'
    'Password Settings'
    '</div>',
    unsafe_allow_html=True
)


length = st.number_input(
    "Enter password length",
    min_value=1,
    max_value=50,
    value=8,
    step=1
)


include_special = st.checkbox(
    "Include special characters (@, #, $, %, &, *)",
    value=True
)


st.divider()




if st.button(
    "Generate Password",
    use_container_width=True
):

  
    if length < 6:

        st.error(
            "Password length must be at least 6 characters."
        )

    else:

        password = generate_password(
            length,
            include_special
        )

        st.session_state.password = password

        st.success(
            "Password generated successfully!"
        )




if "password" in st.session_state:

    st.markdown(
        '<div class="section-title">'
        'Your Generated Password'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="password-box">
            {st.session_state.password}
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()



if st.button(
    "Generate Another Password",
    use_container_width=True
):

    if length < 6:

        st.error(
            "Password length must be at least 6 characters."
        )

    else:

        password = generate_password(
            length,
            include_special
        )

        st.session_state.password = password

        st.rerun()
