import streamlit as st

VERSION = "1.7 Beta"
CONTACT_EMAIL = "[metia.explorer@gmx.net](mailto:metia.explorer@gmx.net)"


@st.dialog("Über Media-Explorer")
def show_about_dialog():
    st.markdown(f"""
    ### Was ist der Media-Explorer?
    Dieses Tool hilft dabei, große Mengen an Bild- und Videodateien anhand von 
    Metadaten zu durchsuchen, zu filtern und zu organisieren. 
    
    Es kombiniert die Power von **ExifTool** mit einer benutzerfreundlichen 
    Oberfläche, um systemseitige und nutzerdefinierte Tags effizient zu verwalten.
    
    **Entwickelt für:** Lokale Medienarchive und schnelle Exploration.
                    
    ---
                
    **Kontakt:** Fragen oder Feedback? Dann schreib an:  
    {CONTACT_EMAIL}

    ---

    Wenn dir der Media-Explorer gefällt, würden wir uns über deine Spende freuen, um die Weiterentwicklung zu unterstützen:
    """)
    _, col2, _ = st.columns(3)
    with col2:
        st.markdown("""
    [![PayPal](https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_111x69.jpg)](https://www.paypal.com/paypalme/Richard98f)
    """)
     
    st.divider()
    st.markdown(f"""
    **Version {VERSION}** | Stand: Februar 2026
    """)
    if st.button("OK", use_container_width=True):
        st.rerun()
        
@st.dialog("KI-Expertenmodus einrichten")
def show_expert_setup_info():
    st.markdown("""
    Um den Expertenmodus zu aktivieren, lege bitte ein **.env-File** an. 
    Dieses muss mindestens folgende Parameter enthalten:
    
    * `OPENAI_API_KEY`, `GOOGLE_API_KEY` oder `MISTRAL_API_KEY`: Deine(n) persönlichen Schlüssel vom Provider. Wenn du mehrere hast, kannst du alle angeben und zur Laufzeit zwischen den Modellen wechseln.
    
    *Optional:* Du kannst auch `OPENAI_MODEL`, `GOOGLE_MODEL`, `MISTRAL_MODEL` und/oder `LLM_TEMPERATURE` setzen, wenn du die KI-Antworten feinjustieren möchtest.
    
    Viel Spaß!
    """)
    if st.button("Verstanden", use_container_width=True):
        st.rerun()

@st.dialog("📖 Kurzanleitung: So nutzt du den Media-Explorer")
def show_help_dialog():
    st.markdown("""
    Der **Media-Explorer** hilft dir, Ordnung in deine Bild- und Videoschätze zu bringen. 
    Hier sind die zwei Wege zum Ziel:
    """)

    # --- Schritt 1 ---
    st.error("### 🔴 Schritt 1: Metadaten einlesen")
    st.write("""
    Bevor es losgeht, müssen die Metadaten deiner Medien im Basisverzeichnis geladen werden. 
    Du kannst sie entweder neu erzeugen (das dauert ungefähr 1 Minute pro 10.000 Bilder) oder gleich auf den **großen roten Knopf** klicken, um den letzten Stand zu laden.
    """)

    st.divider()

    # --- Die zwei Wege ---
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🤖 Weg A: KI-Experte")
        st.write("""
        Frag einfach! Nutze den **Chat**, um komplexe Suchen zu starten (z.B. *'Zeige mir alle Sonnenuntergänge aus 2023'*).
        """)
    with col2:
        st.success("### 🔍 Weg B: Manueller Filter")
        st.write("""
        Wähle in der Auswahlliste die Attribute aus (z.B. Ort, Zeit oder Profi-Tags), die du nutzen möchtest.
        """)

    # --- Schritt 2 & 3 ---
    st.error("### 🔴 Schritt 2 & 3: Filter aufbauen & anwenden")
    st.write("""
    Nachdem du Attribute gewählt hast, klicke auf den **roten Knopf für Schritt 2**, um die Filter-Container zu erstellen. 
    Stelle die Filter ein und drücke **Schritt 3**, um die Medienliste final zu filtern.
    """)

    st.divider()

    st.markdown("""
    > **📍 Besonderheit Kartendarstellung:** > Die Weltkarte erscheint automatisch, sobald du die Attribute **GPSLatitude** und **GPSLongitude** ausgewählt und die Filter angewendet hast.
    """)

    if st.button("Verstanden!", use_container_width=True):
        st.rerun()
        

@st.dialog("⚖️ Lizenzen & Haftung")
def show_license_dialog():
    # --- NEU: Haftungsausschluss & Beta-Hinweis ---
    st.warning("⚠️ **Wichtiger Hinweis (Beta-Stadium)**")
    st.write(f"""
    Diese Software befindet sich im **Beta-Teststadium**. Die Nutzung erfolgt ausschließlich zu Testzwecken 
    und auf **eigenes Risiko**. 
    
    * **Haftungsausschluss:** Jegliche Haftung für Schäden (insbesondere Datenverlust oder Fehlfunktionen), 
        die aus der Nutzung dieser Anwendung resultieren, wird ausdrücklich ausgeschlossen.
    * **Nutzungsbedingungen:** Die private Nutzung ist kostenlos gestattet. Eine **kommerzielle Nutzung** der Software ist untersagt.
    """)
    
    st.write(f"Bei Interesse an einer kommerziellen Lizenzierung oder Kooperation bitten wir um **Kontaktaufnahme** unter: {CONTACT_EMAIL}")

    st.divider()

    # --- Bestehende Inhalte ---
    st.markdown("### OpenStreetMap")
    st.write("""
    Diese Anwendung nutzt Kartendaten von **OpenStreetMap**. 
    Die Daten sind unter der [Open Database License (ODbL)](https://www.openstreetmap.org/copyright) verfügbar.
    """)
    st.info("© OpenStreetMap-Mitwirkende")
    
    st.divider()
    
    st.markdown("### Weitere Software & Bibliotheken")
    st.write("""
    - **ExifTool**: Metadaten-Extraktion (Phil Harvey, Public Domain / GPL).
    - **Streamlit**: User Interface Framework (Apache License 2.0).
    - **Pandas/Pillow**: Daten- und Bildverarbeitung (BSD/MIT).
    - **LLM-Konnektivität**: OpenAI / Google GenAI / Mistral AI API Integration.
    """)

    if st.button("Schließen", key="close_license", use_container_width=True):
        st.rerun()
