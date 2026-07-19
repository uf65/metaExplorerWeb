from pathlib import Path
import sys
import subprocess
from dotenv import load_dotenv
import streamlit as st

VERSION = "1.15 Beta"
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
    **Version {VERSION}** | Stand: Juli 2026
    """)
    if st.button("OK", use_container_width=True):
        st.rerun()

def create_and_open_env_template():
    """Erstellt eine .env-Datei im Basisverzeichnis basierend auf dem Template

    und öffnet sie im Standard-Editor des Betriebssystems.
    """
    base_dir = st.session_state.get("active_base_dir")
    if not base_dir:
        st.error("Kein aktives Basisverzeichnis ausgewählt.")
        return

    env_path = Path(base_dir) / ".env"
    
    # Template-Inhalt festlegen
    template_content = """# KI-Konfigurationen für das Tagging-System
# Bitte fülle mindestens einen API-Schlüssel aus, um die KI-Integration zu aktivieren.

# Global
LLM_TEMPERATURE=1

# OpenAI
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
OPENAI_MM_MODEL=gpt-5-mini

# Google Gemini
GOOGLE_API_KEY=your_google_api_key
GOOGLE_MODEL=gemini-2.5-flash
GOOGLE_MM_MODEL=gemini-2.5-flash

# Mistral
MISTRAL_API_KEY=your_mistral_api_key
MISTRAL_MODEL=magistral-medium-latest
MISTRAL_MM_MODEL=ministral-14b-2512

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key
ANTHROPIC_MODEL=claude-haiku-4-5-20251001
ANTHROPIC_MM_MODEL=claude-haiku-4-5-20251001
"""

    try:
        # 1. Datei schreiben (falls sie noch nicht existiert, um Überschreiben zu verhindern)
        if env_path.exists():
            st.warning(f"Eine `.env`-Datei existiert bereits unter `{env_path}`. Öffne bestehende Datei...")
        else:
            env_path.write_text(template_content, encoding="utf-8")
            st.toast("`.env`-Vorlage erfolgreich erstellt!")

        # 2. Plattformabhängig im Editor öffnen (Windows: Notepad, Mac: TextEdit, Linux: xdg-open)
        if sys.platform.startswith('win'):
            # "start" blockiert Streamlit nicht, "notepad.exe" stellt sicher, dass es der Texteditor ist
            subprocess.Popen(["notepad.exe", str(env_path)])
        elif sys.platform == 'darwin':
            # -e öffnet es spezifisch in TextEdit
            subprocess.Popen(["open", "-e", str(env_path)])
        else:
            # Linux-Fallback (öffnet den registrierten Texteditor)
            subprocess.Popen(["xdg-open", str(env_path)])
            
        st.success(f"Die Datei wurde im Texteditor geöffnet. Bitte Keys eintragen und speichern!")

    except Exception as e:
        st.error(f"Fehler beim Erstellen/Öffnen der Datei: {e}")

        
@st.dialog("KI-Expertenmodus einrichten")
def show_expert_setup_info():
    st.markdown("""
    Um den Expertenmodus zu aktivieren, lege bitte ein **.env-File** an. 
    Dieses muss mindestens folgende Parameter enthalten:
    
    * `OPENAI_API_KEY`, `GOOGLE_API_KEY` oder `MISTRAL_API_KEY`: Deine(n) persönlichen Schlüssel vom Provider. Wenn du mehrere hast, kannst du alle angeben und zur Laufzeit zwischen den Modellen wechseln.
    
    *Optional:* Du kannst auch `OPENAI_MODEL`, `GOOGLE_MODEL`, `MISTRAL_MODEL` und/oder `LLM_TEMPERATURE` setzen, wenn du die KI-Antworten feinjustieren möchtest.
    
    Viel Spaß!
    """)
    col_env, col_reload, col_ok = st.columns([1, 1, 1])
    with col_env:
        if st.button("📝 `.env`-Vorlage erstellen & im Editor öffnen", use_container_width=True, key="btn_create_env_helper", type="primary"):
            create_and_open_env_template()
            st.rerun()
    with col_reload:
        if st.button("🔄 `.env`-Datei neu laden. Ich habe meinen API-Key gerade eingetragen.", use_container_width=True, key="btn_reload_env"):
            load_dotenv(dotenv_path=Path(st.session_state.active_base_dir) / ".env", override=True)
            st.rerun()
    with col_ok:
        if st.button("Verstanden. Mache ich später.", use_container_width=True):
            st.rerun()

@st.dialog("📖 Kurzanleitung: So nutzt du den Media-Explorer", width="large")
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
        

@st.dialog("⚖️ Lizenzen & Haftung", width="medium")
def show_license_dialog():
    # --- Haftungsausschluss & Beta-Hinweis ---
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

    # --- Kartendaten ---
    st.markdown("### 🗺️ Kartendaten")
    st.write("""
    - **OpenStreetMap**: Kartendaten verfügbar unter der [Open Database License (ODbL)](https://www.openstreetmap.org/copyright).
    - **Folium**: Karten-Rendering Framework (MIT License).
    """)
    st.info("© OpenStreetMap-Mitwirkende")
    
    st.divider()
    
    # --- Kern-Technologien ---
    st.markdown("### 🛠️ Software & Bibliotheken")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Daten & Engine**")
        st.write("""
        - **DuckDB**: Datenbank (MIT).
        - **ExifTool**: Metadaten (GPL).
        - **Pandas**: Datenanalyse (BSD).
        - **ImageHash**: Duplikaterkennung.
        """)
    
    with col2:
        st.markdown("**UI & Media**")
        st.write("""
        - **Streamlit**: UI Framework (Apache).
        - **Pillow**: Bildverarbeitung (HPND).
        - **MoviePy**: Videoverarbeitung (MIT).
        - **RapidFuzz**: Fuzzy Search (MIT).
        """)

    st.markdown("**KI-Integrationen**")
    st.caption("OpenAI, Google GenAI, Mistral AI, Anthropic")

    if st.button("Schließen", key="close_license", use_container_width=True):
        st.rerun()