import streamlit as st
import shared.info.dialog_boxes as info

def title():

    st.set_page_config(
        page_title="Metia-Explorer - Lokales Foto- & Video-Management mit KI",
        page_icon="📸",
        layout="wide"
    )

    # UI Layout
    col_logo, col_title, col_help, col_about, col_license = st.columns([1, 5, 1, 1, 1])

    with col_logo:
        st.image("shared/assets/mex_t.jpeg", use_container_width=True)

    with col_title:
        st.caption("")
        st.markdown(
            f"""
            <div style="
                display:flex;
                flex-direction:column;
                justify-content:center;
                height:100%;
                text-align:center;
            ">
                <div style="font-weight:600; font-size:1.1rem;">
                    Foto- und Videomanagement
                </div>
                <div style="font-weight:600; font-size:1.1rem; margin-top:4px;">
                    ChatBot  •  Karte  •  Kreuzfilterung  •  Präsentation
                </div>
                <div style="color:#888; font-size:0.85rem; margin-top:8px;">
                    Version {info.VERSION}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_help:
        # Der Button wird durch ein st.dialog-Fenster ergänzt
        # Abstandshalter, damit der Button optisch auf der Höhe des Titels sitzt
        st.container(height=24, border=False)
        if st.button("❓ Hilfe...", use_container_width=True):
            info.show_help_dialog()
                        
    with col_about:
        # Der Button wird durch ein st.dialog-Fenster ergänzt
        # Abstandshalter, damit der Button optisch auf der Höhe des Titels sitzt
        st.container(height=24, border=False)
        if st.button("ℹ️ Über...", use_container_width=True):
            info.show_about_dialog()
            
    with col_license:
        # Der Button wird durch ein st.dialog-Fenster ergänzt
        # Abstandshalter, damit der Button optisch auf der Höhe des Titels sitzt
        st.container(height=24, border=False)
        if st.button("⚖️ Lizenzen", use_container_width=True):
            info.show_license_dialog()
