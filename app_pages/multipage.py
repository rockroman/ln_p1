import streamlit as st



# Class to generate multiple Streamlit pages using an object oriented approach
# Boilerplate code taken from malaria detector walkthrough project with minor edits
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            )

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})
    
    # LOGO = "src/static/logo.png"
    # LOGO_NAME = "src/static/name.png"

    def run(self):
        st.title(self.app_name)
        # st.logo(
        #     LOGO,
        #     icon_image=LOGO_NAME)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()