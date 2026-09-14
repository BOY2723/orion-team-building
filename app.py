import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TechNova OS | Affaire ORION", page_icon="💻", layout="wide")

# Injection de CSS pour un look "Bureau d'enquête / Hacker" et une image de fond
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
    }
    .main-title {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        text-shadow: 0px 0px 10px #00FF41;
    }
    .terminal-box {
        background-color: #000000;
        border: 1px solid #00FF41;
        padding: 20px;
        border-radius: 5px;
        font-family: 'Courier New', Courier, monospace;
        color: #00FF41;
        margin-bottom: 20px;
    }
    .badge-card {
        background: linear-gradient(135deg, #2b2b2b, #1a1a1a);
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        width: 300px;
        margin: 0 auto;
        box-shadow: 0 4px 8px rgba(0,255,65,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialisation de la progression
if "step" not in st.session_state:
    st.session_state.step = 1

st.markdown("<h1 class='main-title'>TechNova Security OS // INVESTIGATION</h1>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# ÉTAPE 1 : Accès au Système (Zéro papier)
# ==========================================
if st.session_state.step == 1:
    st.markdown("<div class='terminal-box'>ALERTE SÉCURITÉ : PROTOCOLE ORION COMPROMIS.<br>Veuillez scanner votre badge digital pour accéder au serveur d'enquête.</div>", unsafe_allow_html=True)
    
    # Badge Virtuel
    st.markdown(
        """
        <div class='badge-card'>
            <h3 style='color: white;'>BADGE ACCÈS VISITEUR</h3>
            <hr>
            <p style='color: gray; font-size: 12px;'>ID SCAN : 849-B</p>
            <h2 style='color: #00FF41; letter-spacing: 3px;'>NOIRO ATAD</h2>
            <p style='color: gray; font-size: 10px;'>TechNova Corp.</p>
        </div>
        <br>
        """, unsafe_allow_html=True
    )
    
    st.write("Déchiffrez le code visuel de votre badge pour déverrouiller la session.")
    code_input = st.text_input("Entrez le mot de passe du système :")
    
    if st.button("Valider l'accès"):
        if code_input.strip().upper() == "ORION DATA":
            st.success("Accès autorisé !")
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Accès refusé. Vérifiez l'ID visuel.")

# ==========================================
# ÉTAPE 2 : Ordonnancement
# ==========================================
elif st.session_state.step == 2:
    st.header("Étape 2 : Restauration Vidéo")
    st.markdown("<div class='terminal-box'>La caméra du serveur a capté une silhouette à 23h30. L'image est corrompue. Procédure de restauration : Alignement des modules de traitement (P1 à P7).</div>", unsafe_allow_html=True)
    
    st.write("Analysez les contraintes d'antériorité pour trouver l'ordre d'exécution (Mise en ligne des postes).")
    
    # Affichage de la table de précédence virtuellement
    col1, col2 = st.columns(2)
    with col1:
        st.table({
            "Poste": ["P1", "P2", "P3", "P4", "P5", "P6", "P7"],
            "Antécédents": ["P6", "P4", "P7", "P3", "P1", "P2", "Aucun"]
        })
    with col2:
        reponse_etape2 = st.text_input("Séquence numérique des postes (ex: 1234567) :")
        if st.button("Exécuter la restauration"):
            if reponse_etape2.strip() == "7342615":
                st.success("Image restaurée ! Vous distinguez une main avec une montre brillante...")
                if st.button("Ouvrir les dossiers des suspects"):
                    st.session_state.step = 3
                    st.rerun()
            else:
                st.error("Erreur de séquence. Restauration échouée.")

# ==========================================
# ÉTAPE 3 : Investigation Numérique
# ==========================================
elif st.session_state.step == 3:
    st.header("Étape 3 : Base de Données des Employés")
    st.markdown("Fouillez les répertoires personnels des suspects. Tous les indices ont été numérisés.")

    tab1, tab2, tab3, tab4 = st.tabs(["📁 Sarah Benali", "📁 Yassine Gharbi", "📁 Lina Kacem", "📁 Mehdi Trabelsi"])

    # BUREAU DE SARAH (Mots mêlés digitalisés)
    with tab1:
        st.subheader("Fichiers de Sarah (Cheffe de Projet)")
        st.markdown("<div class='terminal-box'>Fichier crypté trouvé. Mots-clés interceptés :<br><br>Z R E A R T I F I C I A L X O<br>P M B I N T E L L I G E N C E W<br>Q T P R O J E C T N O V A L K</div>", unsafe_allow_html=True)
        st.write("Identifiez la phrase clé cachée dans ce flux de données (2 mots en anglais).")
        code_sarah = st.text_input("Mot de passe du fichier :", key="sarah")
        if st.button("Déchiffrer", key="btn_sarah"):
            if code_sarah.strip().lower() in ["artificial intelligence", "intelligence artificielle"]:
                st.success("✅ E-mail récupéré : 'Je refuse catégoriquement l'offre de DataSphere. TechNova n'a rien à partager.'")
            else:
                st.error("Clé invalide.")

    # BUREAU DE YASSINE (Mots croisés digitalisés en définitions)
    with tab2:
        st.subheader("Logs de Yassine (Ingénieur Réseau)")
        st.write("Le pare-feu bloque l'accès. Répondez aux requêtes de sécurité pour recomposer le mot de passe :")
        st.markdown("- Première partie : Information non traitée (4 lettres) -> DATA")
        st.markdown("- Deuxième partie : Forme géométrique tridimensionnelle ronde (6 lettres) -> SPHERE")
        code_yassine = st.text_input("Entrez le mot de passe recomposé :", key="yassine")
        if st.button("Forcer l'accès", key="btn_yassine"):
            if code_yassine.strip().lower() == "datasphere":
                st.success("✅ Brouillon trouvé : 'Je souhaite intégrer votre entreprise pour de nouveaux défis.'")
            else:
                st.error("Échec de l'authentification.")

    # BUREAU DE LINA (Test de logique visuelle)
    with tab3:
        st.subheader("Session de Lina (Assistante)")
        st.write("Un test de sécurité de type CAPTCHA psychotechnique bloque son dossier.")
        st.markdown("Trouvez la logique : **🔺 🟢 🟦 🔺 🟢 ?**")
        choix = st.radio("Sélectionnez la forme suivante :", ["--", "🔺 (Triangle rouge)", "🟦 (Carré bleu)", "🟢 (Cercle vert)"])
        if st.button("Valider le CAPTCHA"):
            if choix == "🟦 (Carré bleu)":
                st.success("✅ Notes trouvées : 'Ce n’est pas toujours devant nous que l’on trouve les indices. Il faut parfois baisser les yeux... Le mot de passe le plus simple est toujours le plus sûr.'")
            else:
                st.error("Test échoué.")

    # BUREAU DE MEHDI
    with tab4:
        st.subheader("Disque dur crypté de Mehdi (Directeur Adjoint)")
        st.write("Le disque est protégé par un code à 5 chiffres. Résolvez l'algorithme sémantique (Le code est le nombre de lettres de chaque réponse) :")
        st.markdown("1. On le résout ou on le pose ? (8)")
        st.markdown("2. Il met fin légalement à un mariage ? (7)")
        st.markdown("3. Amertume après un espoir envolé ? (9)")
        st.markdown("4. Il peut nouer l'estomac ? (7)")
        st.markdown("5. Premier cercle de l'amour ? (7)")
        code_mehdi = st.text_input("Code PIN :", key="mehdi")
        if st.button("Déverrouiller le disque"):
            if code_mehdi.strip() == "87977":
                st.success("✅ Disque déverrouillé ! Document trouvé : Convocation judiciaire attestant d'une faillite personnelle et de lourdes dettes.")
            else:
                st.error("Code PIN erroné.")

    st.markdown("---")
    if st.button("Lancer l'interface d'accusation"):
        st.session_state.step = 4
        st.rerun()

# ==========================================
# ÉTAPE 4 : Verdict Final
# ==========================================
elif st.session_state.step == 4:
    st.markdown("<h2 class='main-title'>RAPPORT D'ENQUÊTE FINAL</h2>", unsafe_allow_html=True)
    st.write("Synthétisez les preuves numériques. Qui a vendu le projet ORION à DataSphere ?")
    
    coupable = st.selectbox("Sélectionnez le suspect :", ["-- Choisir --", "Sarah Benali", "Yassine Gharbi", "Mehdi Trabelsi", "Lina Kacem"])
    
    if st.button("Émettre le mandat d'arrêt"):
        if coupable == "Mehdi Trabelsi":
            st.balloons()
            st.success("🎉 AFFAIRE RÉSOLUE ! Mehdi, ruiné, a utilisé son accès de Directeur pour voler ORION et a couvert ses traces en utilisant le réseau de Yassine.")
        elif coupable != "-- Choisir --":
            st.error("❌ FAUSSE PISTE ! Les indices ne soutiennent pas cette accusation. Relisez les fichiers numériques.")
