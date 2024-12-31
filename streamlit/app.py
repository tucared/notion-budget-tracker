import streamlit_authenticator as stauth  # type: ignore
import yaml
from yaml.loader import SafeLoader

import streamlit as st

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title("Some content")

    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)

elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")

with open("config.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)
