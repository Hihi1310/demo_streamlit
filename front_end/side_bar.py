import streamlit as st

# ------------------ Private Functions ------------------ #

def _render_intstruction() -> None:

    # Add instructions on how to use the app to the sidebar
    st.sidebar.header("How to use Rx Strategist")

    with st.sidebar:
        st.markdown(
            "Welcome to STRIDE GPT, an AI-powered tool designed to help teams produce better threat models for their applications."
        )
        st.markdown(
            "Threat modelling is a key activity in the software development lifecycle, but is often overlooked or poorly executed. STRIDE GPT aims to help teams produce more comprehensive threat models by leveraging the power of Large Language Models (LLMs) to generate a threat list, attack tree and/or mitigating controls for an application based on the details provided."
        )
        st.markdown("Created by [Matt Adams](https://www.linkedin.com/in/matthewrwadams/).")
        # Add "Star on GitHub" link to the sidebar
        st.sidebar.markdown(
            "⭐ Star on GitHub: [![Star on GitHub](https://img.shields.io/github/stars/mrwadams/stride-gpt?style=social)](https://github.com/mrwadams/stride-gpt)"
        )
        st.markdown("""---""")


def _render_app_description() -> None:

    # Add "Example Application Description" section to the sidebar
    st.sidebar.header("Example Application Description")

    with st.sidebar:
        st.markdown(
            "Below is an example application description that you can use to test STRIDE GPT:"
        )
        st.markdown(
            "> A web application that allows users to create, store, and share personal notes. The application is built using the React frontend framework and a Node.js backend with a MongoDB database. Users can sign up for an account and log in using OAuth2 with Google or Facebook. The notes are encrypted at rest and are only accessible by the user who created them. The application also supports real-time collaboration on notes with other users."
        )
        st.markdown("""---""")


def _render_FAQs() -> None:

    # Add "FAQs" section to the sidebar
    st.sidebar.header("FAQs")

    with st.sidebar:
        st.markdown(
            """
        ### **What is STRIDE?**
        STRIDE is a threat modeling methodology that helps to identify and categorise potential security risks in software applications. It stands for **S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, **D**enial of Service, and **E**levation of Privilege.
        """
        )
        st.markdown(
            """
        ### **How does STRIDE GPT work?**
        When you enter an application description and other relevant details, the tool will use a GPT model to generate a threat model for your application. The model uses the application description and details to generate a list of potential threats and then categorises each threat according to the STRIDE methodology.
        """
        )
        st.markdown(
            """
        ### **Do you store the application details provided?**
        No, STRIDE GPT does not store your application description or other details. All entered data is deleted after you close the browser tab.
        """
        )
        st.markdown(
            """
        ### **Why does it take so long to generate a threat model?**
        If you are using a free OpenAI API key, it will take a while to generate a threat model. This is because the free API key has strict rate limits. To speed up the process, you can use a paid API key.
        """
        )
        st.markdown(
            """
        ### **Are the threat models 100% accurate?**
        No, the threat models are not 100% accurate. STRIDE GPT uses GPT Large Language Models (LLMs) to generate its output. The GPT models are powerful, but they sometimes makes mistakes and are prone to 'hallucinations' (generating irrelevant or inaccurate content). Please use the output only as a starting point for identifying and addressing potential security risks in your applications.
        """
        )
        st.markdown(
            """
        ### **How can I improve the accuracy of the threat models?**
        You can improve the accuracy of the threat models by providing a detailed description of the application and selecting the correct application type, authentication methods, and other relevant details. The more information you provide, the more accurate the threat models will be.
        """
        )    


# ------------------ Public Functions ------------------ #

def render_ele() -> None:

    # st.sidebar.image("logo.png")

    # Add instructions on how to use the app to the sidebar
    _render_intstruction()

    # Add "Example Application Description" section to the sidebar
    _render_app_description()

    # Add "FAQs" section to the sidebar
    _render_FAQs()
