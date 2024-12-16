# TODO: Upload GitHub files to helper assistant
# TODO: Add link to Streamlit helper assistant to this page

import streamlit as st
import constants as const
from xata.client import XataClient

site_title = "Chat Builder | Chat-lab.ai"
site_icon = "💬"
st.set_page_config(page_title= site_title, page_icon= site_icon,layout="wide")
st.write("#")
const.load_css(const.css_file)
const.footer(const.footer_text, const.footer_link_text)
hide_top_bar_style = """
        <style>
        header {visibility: hidden;}
        </style>
        """
# Inject CSS with Markdown
st.markdown(hide_top_bar_style, unsafe_allow_html=True)
const.load_css(const.nav_css)
# Render the navigation bar
st.markdown(const.nav_bar_html, unsafe_allow_html=True)

st.markdown(f"""<div style="text-align: center;"><h1>Chat Builder</h1></div>""", unsafe_allow_html=True)

if 's3_access_key' in st.secrets:
    access_key = st.secrets['s3_access_key']
if 's3_secret_key' in st.secrets:
    secret_key = st.secrets['s3_secret_key']   

if 'DB_KEY' in st.secrets:
    DB_KEY = st.secrets['DB_KEY']
if 'DB_URL' in st.secrets:
    DB_URL = st.secrets['DB_URL']   

xata = XataClient(api_key=DB_KEY, db_url= DB_URL)
github_repo = "https://github.com/mailynfz/chat-builder-template"

chat_app_builder_instructions = f"""
        Use *Chat Builder* to generate a Python script that will give your OpenAI Assistant a familiar ChatGPT-style interface. *Chat Builder* is meant to serve as a quick, easy, no-code option for those who like the idea of using chat assistants but don't know how to code or just aren't interested in coding something like this for themselves. If you are familiar with Python or enjoy getting in the weeds of code, you can access the project's files at its [GitHub repo]({github_repo}), which will allow you to download and customize the source code. 

        While I tailored *Chat Builder*'s instructions to create a custom teaching assistant, you can use this tool to create a chat app for any purpose. For example, I created a custom assistant with the documentation information from all the libraries and services I used to build Chat-Lab.AI, so that I could quickly access the information I needed while making this site. You might consider creating a chat assistant with the literature you are using for a given research project. For information on how to make an assistant and advice on getting the most out of custom chat assistants, please visit the Chat-Lab.AI [documentation site](https://doc.chat-lab.ai).

        Note, Chat-Lab.AI's mission is to introduce the public to the possibilities of LLMs beyond ChatGPT. Because *Chat Builder* is meant to provide a quick, no-code solution for creating chat assistants, presently, *Chat Builder*'s template app is only compatible with OpenAI's Assistants API. However, I'm open to supporting other LLMs in the future, should a similar easily deployable option become available. If you are interested in using a different LLM and have suggestions (or code) to share to that end, please [contact me](mailto:feedback@chat-lab.ai). I love nerding out over this stuff and would be happy to entertain any practical ideas.
        
        ## Instructions

        Fill in the prompt fields below and click the *Generate Script* button. Note that some text fields accept [Markdown](https://www.markdownguide.org/basic-syntax/) text, which allows you to add formatting and include links to reference materials. If you are new to [Markdown](https://www.markdownguide.org/basic-syntax/), you can [preview your markdown text here](https://markdownlivepreview.com/).  
        
        After downloading your script here, upload it to a GitHub repo (free) and share it to Streamlit, a free cloud hosting service (using your GitHub login). The [readme section]({github_repo}) for this template contains detailed instructions on how to deploy your app to Streamlit, including an [excellent video tutorial](https://youtu.be/HKoOBiAaHGg?si=FZSTLBjbheHtPOd6) by the [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q).
        
        Following these steps will result in an app that [looks something like this](https://acis-2116-chat.streamlit.app/). After deploying your chat app to Streamlit, share the link to the app with your students and prepare to be known as a *legend*&mdash; if not among your students, certainly among your peers for figuring out how to outsource all the "it's on the syllabus" emails from students. 
        ###
    """
col1,col2,col3 = st.columns([1,6,1])
col2.markdown(chat_app_builder_instructions, unsafe_allow_html=True)
with col2:
    with st.expander("**Click Here to view template site as reference.**"):
        st.image('https://chat-lab-asssets.nyc3.cdn.digitaloceanspaces.com/chat-builder/app-marked-up.png')


with col2.form("Chat Builder Form"):
    # Displaying input fields for each variable
    st.markdown('### Site Title')
    st.write("Give your chat assistant a catchy site title. This is what will appear in the browser tab. Sorry folks, CostGPT is already taken. 😎")
    site_title = st.text_input("#", 'Site Title', key=1, label_visibility="collapsed")

    st.markdown("### Site Icon ☕")
    st.write("**Optional:** Choose a site icon. This will also appear in the browser tab next to the site title (examples: 📚,🤖,🙌🏻--to access the emoji keyboard type `Windows key + .` ). Leave blank if you do not wish to use a site icon.")
    site_icon = st.text_input("#", key=2, label_visibility="collapsed")

    st.markdown("### Page Heading Title")
    st.write("Now give the page a catchy page header title. Refer to the  reference template site in the dropdown menu. If this is left blank, the header will be the same as the Site Title you entered above.")
    page_heading = st.text_input("#", site_title, key=3, label_visibility="collapsed")

    st.markdown("### Heading Text Color")
    st.write("Choose a color for the page heading text. You can create headings in any text field that accepts [Markdown](https://www.markdownguide.org/basic-syntax/) text by starting a new line with # (large heading), ## (medium heading), ### (small heading). These will all appear in the color you choose here. If left blank, the default color will be black.")
    heading_color = st.color_picker("#", label_visibility="collapsed")

    st.markdown("### Description")
    st.write("Describe the app for your students.  Below is a sample description to get you started. Note, if you don't change the sample text below, your site description will refer to ACIS 2116 and exclaim \'Go Hokies!\' That might be problematic for faculty in other ACC schools and/or terrify students enrolled in non-accounting courses. Please consider customizing your own message. You may also leave this field empty.")
    description = st.text_area("#", "ACIS 2116 AI Tutor: Always-On Assistance! Dive into managerial accounting with your GPT4-powered helper. Get answers from your class materials, study effectively, and conquer your final exam. Go Hokies! 😎", key=4, label_visibility="collapsed")

    st.markdown("### Instructions")
    st.write("Write clear instructions for your students to follow. Note, this text area accepts [Markdown](https://www.markdownguide.org/basic-syntax/) text, in case you would like to include links to reference materials. The text below provides a starting point, please edit to your liking. Whatever you write here will appear prominently in the chat app\'s instructions section.")
    instructions = st.text_area("#", 'Enter your API key in the left sidebar to get started. If you don\'t have an API key, go to openai.com to create a new one ([here is a quick tutorial](https://youtu.be/UO_i1GhjElQ?si=7VvfWK8AXQG6vdcn)). After you have entered your API key, click on the \"Start a New Chat\" button to start a new chat. Clicking it again will clear your chat and start a new chat thread.', key=5, label_visibility="collapsed")

    st.markdown("### Chat Box Text")
    st.write("Enter the text you would like to appear in the chat box. This is the text that will appear in the chat box when the app is first loaded. You can use this to provide a welcome message to your students or additional instructions.")
    chat_box_text = st.text_input("#", key=6, label_visibility="collapsed")

    st.markdown('### Sidebar Text')
    st.write("**Optional:** Enter text to appear in the sidebar. You can use this to provide additional instructions or links to reference materials. Note, this text area accepts [Markdown](https://www.markdownguide.org/basic-syntax/) text. Leave blank if you do not want to add any text to the sidebar.")
    sidebar_text = st.text_area("#", key=7, label_visibility="collapsed")

    st.markdown('### Footer Text')
    st.write("**Optional:** Enter text to appear in the footer on the bottom left of the page. You can use this to provide additional instructions or links to reference materials. Note, this text area accepts [Markdown](https://www.markdownguide.org/basic-syntax/) text. Leave blank if you do not want to add any text to the sidebar.")
    footer_text = st.text_area("#", key=8, label_visibility="collapsed")

    st.markdown("### Contact Information")
    st.write("Users are advised of the potential for incorrect responses when they initialize a new chat. Your name (with a link to your email address) will appear in this warning message, allowing users to report any errors in chat responses.")
    name_col, email_col = st.columns(2)
    user_name =  name_col.text_input("Enter your name")
    user_email = email_col.text_input("Enter your email address")

    st.write("### Image or Logo")

    image_choice, logo = st.columns([3,1])

    with image_choice:
        image_filepath = st.text_input("**Optional:** You may add an image to the top of the app's sidebar. You will need to upload this file to GitHub along with the files you download here. Enter the exact name of the image file (example: image.png) to display in the app. Leave this option blank if you would prefer to use the chat-lab.ai logo image.", "")
        image_default = st.checkbox("Uncheck this option if you do not wish to use the Chat-lab.ai logo in your app's sidebar. If unchecked and you do not provide an image name, then there will be no image displayed in the app sidebar.", value=True) 

    with logo:
        image_url = "https://chat-lab-asssets.nyc3.cdn.digitaloceanspaces.com/Chat-lab-bubble-logo-no_tail-removebg-white_face.png"

        caption_text = "Chat-lab.ai logo that appears in the app sidebar by default."
        st.markdown(f"""
                <style>
                .container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center; 
                }}
                .image {{
                    max-width: 125px;
                    height: auto;
                }}
                .caption {{
                    color: #666; 
                    font-size: .9em; 
                    text-align: center;
                    margin-top: 2px; 
                }}
                </style>
                <div class="container">
                    <img src="{image_url}" class="image">
                    <div class="caption">{caption_text}</div>
                </div>
                """, unsafe_allow_html=True)

    st.write("#")
    template_py = "https://chat-builder.nyc3.cdn.digitaloceanspaces.com/ta-template.py"
    space_name = 'chat-builder'
    s3_folder_path = 'downloads'
    expiration = 7 * 24 * 60 * 60  # 7 days

    if st.form_submit_button('Generate Script'):
        replacements = {
            'site_title': site_title,
            'site_icon': site_icon,
            'page_heading': page_heading,
            'heading_color': heading_color,
            'description': description,
            'instructions': instructions,
            'chat_box_text': chat_box_text,
            'image_filepath': image_filepath,
            'image_default': str(image_default),
            'sidebar_text': sidebar_text,
            'footer_text': footer_text,
            'user_name': user_name,
            'user_email': user_email
        }
        print(replacements)

        download_url = const.create_and_upload_script(template_py, user_email, access_key, secret_key,space_name, s3_folder_path, expiration, replacements)

        if download_url:
            st.balloons()
            st.success("Script generated successfully!",icon="🎉")
            st.warning("Please download BOTH the script and requirements.txt files. You wil need to upload BOTH to your GitHub repo. Then follow the instructions on the [template's GitHub repo page]({github_repo})", icon="⚠️")
            
            button_style = """color: white; background-color: #3b7dac; border: none; padding: 10px 20px; text-align: center; font-size: 1rem; font-weight: 700; line-height: 1.3; display: inline-block; margin: 20px 20px; cursor: pointer; border-radius: 8px; width: 200px; height: 75px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);"""

            download_button_html = f"""
                <a href="{download_url}" target="_blank">
                    <button style="{button_style}">
                        Download <br>
                        Template Script
                    </button>
                </a>"""
            requirements_download_url = "https://chat-builder.nyc3.cdn.digitaloceanspaces.com/requirements.txt"
            requirements_button_html = f"""
                <a href="{requirements_download_url}" target="_blank">
                    <button style="{button_style}">
                        Download Requirements.txt
                    </button>
                </a>"""

            # Display both buttons side by side
            st.markdown(f"""
                        <div style="display: flex; justify-content: center;">
                        {download_button_html}        {requirements_button_html}
                        </div>
                        """, unsafe_allow_html=True)

        else:
            st.error("Failed to generate download link.")
        deployment_instructions = """
            ### Deployment Instructions
            1. Download the necessary files by clicking the download buttons above. If the file does not download automatically, try right-clicking the button and selecting "Save Link As..." or "Download Linked File As..." (depending on your browser).
            2. The app consists of two files: `requirements.txt` and `[unique prefix]-streamlit_app.py`. You must upload both files to GitHub for your app to work. 
            
                For your sake, rename the python script to `streamlit_app.py` (i.e., delete the unique prefix) before uploading it to GitHub.This will make it easier for Streamlit to find the file.

            3. Upload BOTH of these files (and your optional image file) to your GitHub repo (free) and share it to Streamlit (using your GitHub login) following the instructions found [here]({github_repo}) or by following [this video tutorial](https://youtu.be/HKoOBiAaHGg?si=FZSTLBjbheHtPOd6) (displayed below). 
            """
        st.info(deployment_instructions)

        col1,col2,col3 = st.columns([1,8,1])
        video_tutorial_id = "HKoOBiAaHGg"

        video_tutorial_html = f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_tutorial_id}" frameborder="0" allowfullscreen></iframe>"""

        info_card_html = f"""
            <div style="background-color: #f0f0f0; border-radius: 10px; padding-top: 0px; padding-left: 60px; padding-bottom:30px; padding-right: 60px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin: 10px; text-align: center;">
                <h2>Video tutorial</h2>
                <p><span style="font-size: 20px; font-weight: normal; color: color: #576676;;">This excellent video tutorial will walk you through the process of deploying a Streamlit app from a GitHub repo.</span>
                </p>
            {video_tutorial_html}
            </div>
        """
        col2.markdown(info_card_html, unsafe_allow_html=True)

        user_id = const.check_or_create_user_id(user_email, xata)

        data = xata.records().insert("chat_builder", {
            "user_id": user_id,
            "page_heading": page_heading,
            "site_title": site_title,
            "site_icon": site_icon,
            "description": description,
            "instructions": instructions,
            "image": f"[{image_filepath}, {image_default}]",
            "footer_text": footer_text,
            "chat_prompt_text": chat_box_text,
            "heading_color": heading_color,
            "sidebar_text": sidebar_text,
            "script_url": download_url,
            "email": user_email
        })

        const.print_query_results(data)


st.write("#")
st.write("#")
st.divider()
st.markdown(f"""{const.support_banner}""", unsafe_allow_html=True)
