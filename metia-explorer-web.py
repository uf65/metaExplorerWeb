import streamlit as st
from shared.info.title import title
        
title()

st.markdown("<hr style='margin-top:0;'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    section = st.segmented_control(
        "",
        options=["Home", "Installation", "FAQ"],
        default="Home",
    )

if section == "Home":

    st.markdown("""
    ## Willkommen beim Metia-Explorer

    Der **Metia-Explorer** ist eine lokale Anwendung für leistungsfähiges
    Foto- und Videomanagement.

    ### Hauptfunktionen

    - 🔎 Intelligente Attribut-Filter
    - 🗺️ Kartenbasierte Geosuche
    - 🤖 KI-gestützte Abfragen per Chat
    - 🔀 Kreuzfilterung mehrerer Metadaten
    - 🎞️ Präsentationsmodus für Bild- und Videoserien

    Der Metia-Explorer läuft bewusst lokal in einem Docker-Container.
    So bleiben deine Medien und Metadaten vollständig unter deiner Kontrolle.
    """)

elif section == "Installation":

    st.markdown("## Installation in 3 Schritten")

    with st.expander("Schritt 1: Docker Desktop installieren"):
        st.markdown("""
        Der Metia-Explorer läuft auf Windows, macOS und Linux
        mithilfe der Docker Engine.

        Lade Docker Desktop hier herunter:
        https://www.docker.com/products/docker-desktop/
        
        """)
        st.image("assets/install_step1-1.png", use_container_width=True)
        st.markdown("Lade die Version, die zu deinem Rechner passt und installiere sie. Es kann sein, dass Docker dich fragt, ob du einen Docker-Account anlegen möchtest. Das kannst du machen, musst du aber nicht, um den Media Explorer zu nutzen.")

    with st.expander("Schritt 2: Metia-Explorer laden"):
        st.markdown("""
        Öffne im Docker Desktop den Bereich **Docker Hub**
        und suche nach:

        `uf65/media-explorer`

        Wähle die aktuelle Version und klicke auf **Pull**.
        """)
        st.image("assets/install_step2-1.png", use_container_width=True)

    with st.expander("Schritt 3: Metia-Explorer starten"):
        st.markdown("""
        Gehe zu **Images** im Docker Desktop.

        - Host port: `8501`
        - Host path: dein Medienverzeichnis
        - Container path: `/media`

        Danach mit **Run** starten.
        """)
        st.image("assets/install_step3-1.png", use_container_width=True)

elif section == "FAQ":

    st.markdown("## Häufige Fragen")

    with st.expander("Warum heißt es Metia-Explorer? Ist das ein Schreibfehler?"):
        st.markdown("""
        Nein 😊

        Der Name wurde bewusst geändert, um Verwechslungen
        mit anderen Produkten namens „Media Explorer“
        zu vermeiden.

        „Metia“ verweist auf Metadaten – das Herzstück der Anwendung.
        """)

    with st.expander("Warum kann ich den Metia-Explorer nicht einfach herunterladen?"):
        st.markdown("""
        Der Metia-Explorer greift direkt auf dein lokales
        Medienverzeichnis zu.

        Deshalb läuft er in einem Docker-Container
        auf deinem eigenen Rechner und nicht als
        klassische Web-App.
        """)

    with st.expander("Wie nutze ich die KI-Funktionen?"):
        st.markdown("""
        Die KI-Funktionen stehen im Chat-Modus zur Verfügung.

        Du kannst natürliche Sprache verwenden wie z.B.:

        - „Zeige mir alle Videos vom Sommer 2023.“
        - „Fotos, die an einem Sonntag aufgenommen wurden.“
        - „Bilder von Peter in Italien.“

        Die KI übersetzt deine Anfrage automatisch
        in passende Metadaten-Filter.
        """)
