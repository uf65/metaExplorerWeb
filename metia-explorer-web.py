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

        """)
        st.image("assets/install_step2-1.png", use_container_width=True)
        st.markdown("Wähle „uf65/media-explorer“ aus:")
        st.image("assets/install_step2-2.png", use_container_width=True)
        st.markdown("""
                    In der Auswahlliste **Tags** ist automatisch die letzte Version eingestellt. Nimm diese. Theoretisch kannst du auch ältere Versionen laden, wenn dir an der neuesten irgendetwas nicht gefällt. Normalerweise brauchst du das aber nicht. Klicke auf **Pull**, um den Media-Explorer zu laden.
Wenn du möchtest, kannst du auch gleich auf **Run** klicken, um den Media Explorer zu starten. Dann geht es weiter wie im Schritt 3.
                    """)
        st.image("assets/install_step2-3.png", use_container_width=True)
        

    with st.expander("Schritt 3: Metia-Explorer starten"):
        st.markdown("""
                    Gehe im Docker Desktop auf **Images**. Dort siehst du im **Local** Tab den Media Explorer, den du gerade heruntergeladen hast. Starte ihn mit einem Klick auf den **Play**-Knopf.
        """)
        st.image("assets/install_step3-1.png", use_container_width=True)
        st.markdown("""
                    Klappe die **Optional Setting** aus und gib ein:
                    
        - Host port: `8501`
        - Host path: dein Medienverzeichnis
        - Container path: `/media`

        Danach mit **Run** starten.
        """)
        st.image("assets/install_step3-2.png", use_container_width=True)
        st.markdown("""
        Der Media Explorer läuft jetzt ganz sicher in einem Docker-Container, und du bekommst diese Anzeige:
        """)
        st.image("assets/install_step3-3.png", use_container_width=True)
        st.markdown("""
        Dass der Container im gezeigten Beispiel **cranky_dubinsky** heißt, hat nichts zu bedeuten. Bei dir kann irgendein anderer Name stehen, den sich die Docker Engine gerade ausgedacht hat.

        Ein letzter Klick noch auf die angezeigte URL, und der Media Explorer öffnet sich im Browser:
        """)
        st.image("assets/install_step3-4.png", use_container_width=True)
        st.markdown("""
        Herzlichen Glückwunsch! Du hast den schwierigsten Teil geschafft. Beim nächsten Mal brauchst du nichts mehr zu installieren, sondern den Media Explorer nur noch aus dem Docker Desktop heraus zu starten. Weitere Hinweise zur Benutzung findest du in der Hilfe.
        """)

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
        Medienverzeichnis zu und läuft auf Windows, Mac und Linux ohne jede Anpassung.

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
