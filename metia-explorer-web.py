import streamlit as st
from shared.info.title import title
import shared.info.dialog_boxes as info
        
title()

st.markdown("<hr style='margin-top:0;'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    section = st.segmented_control(
        "section",
        options=["Home", "Installation", "FAQ"],
        default="Home",
        label_visibility="collapsed"
    )

if section == "Home":

    st.markdown("""
    ## Willkommen beim Metia-Explorer
    ### Lokales Foto- und Videomanagement mit KI-Unterstützung
    
    Der **Metia-Explorer** ist eine lokale Anwendung für leistungsfähiges
    Foto- und Videomanagement.
    
    Hast du eine unüberschaubare Menge an Fotos und Videos auf deinem Rechner, die du nicht mehr richtig durchblickst?
    Und du möchtest sie nicht in die Cloud hochladen, weil das zu teuer ist oder weil du findest, dass sie da nicht hingehören?
    Dann bist du richtig hier! Der Metia-Explorer hilft dir dabei, deine Medien zu organisieren, zu durchsuchen und zu präsentieren - und das alles mit Unterstützung von Künstlicher Intelligenz (wenn du magst).

    ### Hauptfunktionen

    - 🔎 Automatische Generierung von Metadaten
    - 🗺️ Kartenbasierte Geosuche
    - 🏷️ Automatische Verschlagwortung ("Auto-Tagging") mit KI
    - 🤖 KI-gestützte Abfragen per Chat
    - 👯 Erkennung und Verwaltung von Duplikaten
    - 🔀 Kreuzfilterung beliebiger Foto-Attribute
    - 🎞️ Präsentationsmodus für Bild- und Videoserien

    Der **Metia-Explorer** läuft bewusst lokal in einem "Docker-Container".
    So bleiben deine Medien und Metadaten vollständig unter deiner Kontrolle.
    
    Und last but not least: Der **Metia-Explorer** ist kostenlos für private Nutzer. Das gilt sogar für die KI-Funktionen, solange du einen eigenen API-Key einrichtest und das kostenlose Kontingent des Providers nicht überschreitest.
    
    So könnte der **Metia-Explorer** bei dir aussehen:
    """)
    _, col2, _ = st.columns([1,4,1])
    with col2:
        st.image("assets/20260217_metia-explorer-screenshot.png", use_container_width=True)

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
        st.markdown("Lade die Version, die zu deinem Rechner passt und installiere sie. Es kann sein, dass Docker dich fragt, ob du einen Docker-Account anlegen möchtest. Das kannst du machen, musst du aber nicht, um den Metia-Explorer zu nutzen.")

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
                    In der Auswahlliste **Tags** ist automatisch die letzte Version eingestellt. Nimm diese. Theoretisch kannst du auch ältere Versionen laden, wenn dir an der neuesten irgendetwas nicht gefällt. Normalerweise brauchst du das aber nicht. Klicke auf **Pull**, um den Metia-Explorer zu laden.
Wenn du möchtest, kannst du auch gleich auf **Run** klicken, um den Metia-Explorer zu starten. Dann geht es weiter wie im Schritt 3.
                    """)
        st.image("assets/install_step2-3.png", use_container_width=True)
        

    with st.expander("Schritt 3: Metia-Explorer starten"):
        st.markdown("""
                    Gehe im Docker Desktop auf **Images**. Dort siehst du im **Local** Tab den Metia-Explorer, den du gerade heruntergeladen hast. Starte ihn mit einem Klick auf den **Play**-Knopf.
        """)
        st.image("assets/install_step3-1.png", use_container_width=True)
        st.markdown("""
                    Klappe die **Optional Settings** aus und gib ein:
                    
        - Host port: `8501`
        - Host path: dein Medienverzeichnis
        - Container path: `/media`

        Danach mit **Run** starten.
        """)
        st.image("assets/install_step3-2.png", use_container_width=True)
        st.markdown("""
        Der Metia-Explorer läuft jetzt ganz sicher in einem Docker-Container, und du bekommst diese Anzeige:
        """)
        st.image("assets/install_step3-3.png", use_container_width=True)
        st.markdown("""
        Dass der Container im gezeigten Beispiel **xenodochial_nightingale** heißt, hat nichts zu bedeuten. Bei dir kann irgendein anderer Name stehen, den sich die Docker Engine gerade ausgedacht hat.

        Ein letzter Klick noch auf die angezeigte **Local URL**, und der Metia-Explorer öffnet sich im Browser:
        """)
        st.image("assets/install_step3-4.png", use_container_width=True)
        st.markdown("""
        Herzlichen Glückwunsch! Du hast den schwierigsten Teil geschafft. Beim nächsten Mal brauchst du nichts mehr zu installieren, sondern den Metia-Explorer nur noch aus dem Docker Desktop heraus zu starten. Weitere Hinweise zur Benutzung findest du in der Hilfe.
        """)

elif section == "FAQ":

    st.markdown("## Häufige Fragen")

    with st.expander("Warum heißt es Metia-Explorer? Ist das ein Schreibfehler?"):
        st.markdown("""
        Nein 😊

        Der Name wurde bewusst so gewählt, um Verwechslungen
        mit anderen Produkten namens „Media Explorer“
        zu vermeiden.

        „Metia“ verweist außerdem auf Metadaten, die das Herzstück der Anwendung sind.
        """)

    with st.expander("Warum kann ich den Metia-Explorer nicht einfach herunterladen?"):
        st.markdown("""
        Der Metia-Explorer greift direkt auf dein lokales
        Medienverzeichnis zu und läuft auf Windows, Mac und Linux ohne jede Anpassung.

        Deshalb läuft er in einem Docker-Container
        auf deinem eigenen Rechner und nicht als
        klassische Web-App.
        """)

    with st.expander("Wie aktiviere ich die KI-Funktionen?"):
        st.markdown(f"""
        Dazu musst du dir bei mindestens einem LLM-Provider einen API-Key einrichten.
        Derzeit unterstützt der Metia-Explorer die folgenden LLM-Provider: Google, Mistral, OpenAI.

        Deinen API-Key trägst du in ein **.env**-File im Medienverzeichnis ein.
        Du kannst dort auch mehrere API-Keys angeben, wenn du möchtest, und dann zur Laufzeit zwischen den Modellen wechseln.
        Die Modelle <provider>_MODEL werden im Chat benutzt, die Modelle <provider>_MM_MODEL für das Auto-Tagging.

        `# Global`\n
        `LLM_TEMPERATURE=1`\n
        `# OpenAI`\n
        `OPENAI_API_KEY=sk-proj-...dein OpenAI API-Key...`\n
        `OPENAI_MODEL=gpt-5-mini`\n
        `OPENAI_MM_MODEL=gpt-5-mini`\n
        `# Google Gemini`\n
        `GOOGLE_API_KEY=...dein Gemini API-Key...`\n
        `GOOGLE_MODEL=gemini-2.5-flash`
        `GOOGLE_MM_MODEL=gemini-2.5-flash`
        `# Mistral`\n
        `MISTRAL_API_KEY=...dein Mistral API-Key...`\n
        `MISTRAL_MODEL=magistral-medium-latest`\n
        `MISTRAL_MM_MODEL=pixtral-12b-2409`\n
        
        **Wenn du die KI-Funktionen lieber ohne Einrichtungsaufwand nutzen möchtest, lass es uns bitte wissen: {info.CONTACT_EMAIL}. Bei ausreichender Nachfrage würden wir eine Version mit integrierten KI-Funktionen publizieren. Diese müsste dann allerdings notgedrungen kostenpflichtig sein.**
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
        
    with st.expander("Ich kann die Kartendarstellung nicht finden."):
        st.markdown("""
        Die Kartendarstellung wird angezeigt, wenn du
        
        - selbst filterst (also die Filterung nicht der KI überlässt)
        - mindestens die beiden Attribute **GPSLatitude** und **GPSLongitude** ausgewählt...
        - ...und die Filter angewendet hast.
        """)

    with st.expander("Wie funktioniert Auto-Tagging?"):
        st.markdown("""
        Fürs Auto-Tagging sind 3 Schritte erforderlich:
        1. Die KI-Funktionen aktivieren (siehe oben)
        2. Nach dem Einlesen der Metadaten wählst du aus "Ich filtere selbst"
        3. Du klickst auf einen der "Tag"-Knöpfe (entweder im Preview der Kartendarstellung oder in der Ergbnispräsentation)
        Für einzelne Files hast du dann einen Knopf "Tags generieren", für die gesamte aktuelle Auswahl einen Knopf "Massen-Tagging starten".
        Wenn dabei komplett neue Tags entstehen, die im gesamten Bestand noch nicht vorhanden sind, musst du noch einmal bestätigen, dass du sie wirklich hinzufügen willst, um die Anzahl Tags nicht unkontrolliert wachsen zu lassen.
        """)
        
    with st.expander("Erkennt der Metia-Explorer Duplikate?"):
        st.markdown("""
        Ja. Wähle dazu nach dem Einlesen der Metadaten "Ich filtere selbst". Zusammen mit den Ergebnissen erscheint dann ein zusätzlicher Button "Duplikate erkennen".
        Einfach anklicken und den Anweisungen folgen.
        """)

    with st.expander("Was bedeuten die keep_if und move_if Tags bei der Duplikat-Erkennung?"):
        st.markdown("""
        Diese Tags sind optional. Vielleicht möchtest du Bilder in einem Ordner "Camera Uploads" eher behalten, Bilder im Ordner "WhatsApp Images" eher nicht.
        Dann kannst du "Camera Uploads" mit keep_if und "WhatsApp Images" mit move_if markieren. Aber keine Sorge: bevor tatsächlich Bilder verschoben werden, kannst du dir
        alles noch einmal ansehen und bestätigen oder verwerfen.
        """)

    with st.expander("Ich möchte die KI-Funktionen lokal auf meinem Rechner nutzen, ohne einen API-Key einzurichten. Geht das?"):
        st.markdown("""
        Ja, das geht - aber nur auf einem leistungsfähigen Rechner. Du solltest 32GB Hauptspeicher und eine leistungsfähige GPU haben.
        Dann kannst du dir mit Docker Desktop ein Modell laden wie z.B. ai/gemma3, und der Metia-Explorer wird es erkennen und dir zur Auswahl anbieten.
        """)

    with st.expander("Warum sollte ich in den Datenbank-Modus wechseln, wenn Metia-Explorer das anbietet?"):
        st.markdown("""
        Normalerweise hält der Metia-Explorer alle Metadaten im Hauptspeicher deines Rechners. Das wird bei mehreren 10.000 Medien irgendwann langsam oder aus Speichermangel sogar unmöglich.
        In diesem Fall solltest du in den Datenbank-Modus wechseln. Dann werden die Metadaten in einr Cache-DB im Medienordner gehalten, und die Anzahl Medien, die du verwalten kannst, ist praktisch unbegrenzt.
        Außerdem merkt sich der Metia-Explorer im Datenbank-Modus manche Dinge, die sonst mühsam neu berechnet werden müssten, z.B. die Attributtypen und die visuellen Hashes zum Erkennen von Dubletten. Das macht die Nutzung insgesamt komfortabler.
        """)

                    
# Fusszeile

# schönere Darstellung, nicht von streamlit unterstützt

# st.markdown("""
# <style>
# .footer {
#     position: fixed;
#     bottom: 0;
#     left: 0;
#     width: 100%;
#     background-color: #fafafa;
#     border-top: 1px solid #eaeaea;
#     padding: 10px 0;
#     text-align: center;
#     font-size: 0.9rem;
#     z-index: 100;
# }
# .footer a {
#     margin: 0 15px;
#     color: #444;
#     text-decoration: none;
#     cursor: pointer;
# }
# .footer a:hover {
#     text-decoration: underline;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div class="footer">
#     <a onclick="window.parent.postMessage({type: 'impressum'}, '*')">
#         Impressum
#     </a>
#     |
#     <a onclick="window.parent.postMessage({type: 'datenschutz'}, '*')">
#         Datenschutz
#     </a>
# </div>
# """, unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col2:
    if st.button("Impressum", key="impressum_btn"):
        st.session_state.show_impressum = True

with col3:
    if st.button("Datenschutz", key="ds_btn"):
        st.session_state.show_datenschutz = True


@st.dialog("Impressum")
def show_impressum_dialog():
    st.markdown(f"""
    **Angaben gemäß § 5 TMG**

    Richard Fastenrath  
    Birkenweg 7,
    85399 Hallbergmoos  
    Deutschland  

    E-Mail: {info.CONTACT_EMAIL}
    """)

if st.session_state.get("show_impressum"):
    show_impressum_dialog()
    st.session_state.show_impressum = False


@st.dialog("Datenschutzerklärung")
def show_datenschutz_dialog():
    st.markdown("""
    Diese Website verwendet ausschließlich technisch notwendige
    Cookies zur Sitzungsverwaltung.

    Es werden keine Tracking- oder Analyse-Tools eingesetzt.

    Beim Besuch der Seite werden durch den Hosting-Anbieter
    technisch notwendige Server-Logfiles erfasst.
    """)

if st.session_state.get("show_datenschutz"):
    show_datenschutz_dialog()
    st.session_state.show_datenschutz = False
