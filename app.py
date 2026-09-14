import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TechNova OS | Affaire ORION", page_icon="🕵️‍♂️", layout="wide")

# Initialisation de la progression et des états de validation
if "step" not in st.session_state:
    st.session_state.step = 1
if "etape2_success" not in st.session_state:
    st.session_state.etape2_success = False

# ==========================================
# GESTION DES ARRIÈRE-PLANS DYNAMIQUES
# ==========================================
# L'image de fond change en fonction de l'étape (Serveur -> Caméra de sécurité -> Bureau d'enquête -> Verdict)
backgrounds = {
    1: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2000&auto=format&fit=crop", # Salle Serveur / Cyber
    2: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?q=80&w=2000&auto=format&fit=crop", # Ambiance Caméra CCTV / Sombre
    3: "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=2000&auto=format&fit=crop", # Dossiers sur un bureau
    4: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=2000&auto=format&fit=crop"  # Ambiance polar / ombres
}

bg_url = backgrounds.get(st.session_state.step, backgrounds[1])

# Injection de CSS pour le design Hacker/Enquêteur avec fond dynamique
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.95)), url('{bg_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-title {{
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        text-shadow: 0px 0px 15px rgba(0, 255, 65, 0.5);
        background: rgba(0,0,0,0.6);
        padding: 10px;
        border-radius: 10px;
    }}
    .terminal-box {{
        background-color: rgba(0, 0, 0, 0.8);
        border: 1px solid #00FF41;
        padding: 20px;
        border-radius: 8px;
        font-family: 'Courier New', Courier, monospace;
        color: #00FF41;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.2);
    }}
    .instruction-box {{
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #d9534f;
        margin-bottom: 20px;
        font-family: sans-serif;
    }}
    .badge-card {{
        background: linear-gradient(135deg, #1f1f1f, #0a0a0a);
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        width: 320px;
        margin: 0 auto;
        box-shadow: 0 4px 15px rgba(0,255,65,0.4);
    }}
    /* Stylisation des onglets pour l'étape 3 */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: rgba(0,0,0,0.6);
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>TechNova Security OS // INVESTIGATION</h1>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# ÉTAPE 1 : Accès au Système
# ==========================================
if st.session_state.step == 1:
    st.markdown("<div class='terminal-box'>ALERTE SÉCURITÉ : PROTOCOLE ORION COMPROMIS.<br>Veuillez scanner votre badge digital pour accéder au serveur d'enquête principal.</div>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='badge-card'>
            <h3 style='color: white; margin-bottom: 5px;'>BADGE ACCÈS VISITEUR</h3>
            <div style='background-color: #4CAF50; height: 3px; width: 100%; margin-bottom: 15px;'></div>
            <p style='color: gray; font-size: 12px; margin-bottom: 5px;'>ID SCAN : 849-B / NIVEAU 1</p>
            <h2 style='color: #00FF41; letter-spacing: 4px; font-family: "Courier New";'>NOIRO ATAD</h2>
            <p style='color: gray; font-size: 11px; margin-top: 15px;'>TechNova Corp. - STRICTEMENT PERSONNEL</p>
        </div>
        <br>
        """, unsafe_allow_html=True
    )
    
    st.info("💡 Indice : Déchiffrez le code visuel de votre badge pour déverrouiller la session.")
    code_input = st.text_input("Entrez le mot de passe du système :")
    
    if st.button("Valider l'accès"):
        if code_input.strip().upper() == "ORION DATA":
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Accès refusé. Empreinte visuelle non reconnue.")

# ==========================================
# ÉTAPE 2 : Ordonnancement & Traitement d'image
# ==========================================
elif st.session_state.step == 2:
    st.header("Étape 2 : Restauration Vidéo")
    st.markdown("<div class='terminal-box'>La caméra du serveur a capté une silhouette à 23h30. L'image est fragmentée. Initialisation du protocole de restauration d'image par alignement des postes...</div>", unsafe_allow_html=True)
    
    # Intégration exacte du texte de l'image (instruction box blanche pour contraster avec le fond sombre)
    st.markdown("""
    <div class='instruction-box'>
        <h4>Document technique extrait du manuel d'ingénierie :</h4>
        <p><strong>Etape 3 :</strong> Nous allons utiliser la <strong>méthode de mise en ligne des postes</strong>. Cette méthode permet de déterminer le <strong>bon ordre des postes de traitement</strong> à partir des relations existantes entre les images intermédiaires et les postes.</p>
        <ul>
            <li>les images intermédiaires : <strong>I1, I2, I3, I4</strong></li>
            <li>les postes de traitement : <strong>P1, P2, P3, P4, P5, P6, P7</strong></li>
        </ul>
        <p>Plusieurs images sont générées en utilisant ce processus. La méthode de mise en ligne consiste à :</p>
        <ol>
            <li><strong>Remplir un tableau</strong> indiquant, pour chaque poste <strong>Px</strong>, les postes qui doivent être réalisés avant lui.</li>
            <li>Identifier les postes qui n'<strong>ont aucun antécédent</strong> (aucun poste précédent).</li>
            <li>Placer ces postes en <strong>premier</strong> dans l'ordre de traitement, puis les <strong>éliminer du tableau</strong>.</li>
            <li>Répéter l'opération jusqu'à ce que <strong>tous les postes soient ordonnés</strong>.</li>
        </ol>
        <p>On vous donne :</p>
        <ul>
            <li>le <strong>tableau de relations entre les postes et les images</strong>,</li>
            <li>le <strong>tableau à remplir</strong> (sur votre feuille de brouillon).</li>
        </ul>
        <p><strong>Objectif :</strong> trouver le <strong>bon ordre</strong> des postes de traitement afin d'obtenir l'image finale restaurée.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Base de données des relations (Extraite du système) :")
    
    # Tableau exact de l'image reproduit en Markdown
    st.markdown("""
    | Postes \ Images | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | **I1** | | | 2 | 3 | 4 | | 1 |
    | **I2** | 3 | | 1 | | 4 | 2 | |
    | **I3** | 4 | 2 | | | | 3 | 1 |
    | **I4** | | 2 | | 1 | 4 | 3 | |
    """)

    st.write("---")
    reponse_etape2 = st.text_input("Séquence numérique finale des postes (ex: 1234567) :")
    
    # Bouton de validation (La correction du bug se trouve ici, séparée du bouton d'ouverture des dossiers)
    if st.button("Exécuter la restauration"):
        if reponse_etape2.strip() == "7342615":
            st.session_state.etape2_success = True
        else:
            st.error("Erreur de séquence. Restauration échouée. Veuillez revoir votre méthode de mise en ligne.")
            st.session_state.etape2_success = False

    # Si la restauration est un succès, on affiche le message et le NOUVEAU bouton pour passer à la suite
    if st.session_state.etape2_success:
        st.success("✅ Image restaurée avec succès ! Vous distinguez l'ombre d'une silhouette portant une montre en argent distincte...")
        if st.button("Ouvrir les dossiers des suspects"):
            st.session_state.step = 3
            st.session_state.etape2_success = False # Réinitialisation
            st.rerun()

# ==========================================
# ÉTAPE 3 : Investigation Numérique
# ==========================================
elif st.session_state.step == 3:
    st.header("Étape 3 : Base de Données des Employés")
    st.markdown("<div class='terminal-box'>Accès accordé aux postes de travail personnels. Attention : certains fichiers cruciaux sont protégés par chiffrement.</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📁 Sarah Benali", "📁 Yassine Gharbi", "📁 Lina Kacem", "📁 Mehdi Trabelsi"])

    with tab1:
        st.subheader("Poste de Sarah (Cheffe de Projet)")
        st.write("Une analyse sémantique du disque dur révèle un fichier crypté.")
        st.markdown("<div class='terminal-box' style='color:#ffaa00; border-color:#ffaa00;'>Mots-clés interceptés dans le buffer :<br><br>Z R E <strong>A R T I F I C I A L</strong> X O<br>P M B <strong>I N T E L L I G E N C E</strong> W<br>Q T P R O J E C T N O V A L K</div>", unsafe_allow_html=True)
        st.info("Identifiez la phrase clé cachée dans cette matrice (2 mots en anglais).")
        code_sarah = st.text_input("Mot de passe du fichier :", key="sarah")
        if st.button("Déchiffrer le fichier de Sarah"):
            if code_sarah.strip().lower() in ["artificial intelligence", "intelligence artificielle"]:
                st.success("✅ E-mail récupéré : 'Je refuse catégoriquement l'offre de DataSphere. TechNova n'a rien à partager. Mon équipe a trop travaillé sur ce projet.'")
            else:
                st.error("Clé invalide.")

    with tab2:
        st.subheader("Poste de Yassine (Ingénieur Réseau)")
        st.write("Le pare-feu personnel de Yassine exige de résoudre un jeu de mots de passe fractionnés :")
        st.markdown("> **Partie 1 :** Information brute non traitée (4 lettres)<br>> **Partie 2 :** Forme géométrique tridimensionnelle parfaitement ronde (6 lettres)", unsafe_allow_html=True)
        code_yassine = st.text_input("Mot de passe recomposé (1 mot) :", key="yassine")
        if st.button("Forcer le pare-feu de Yassine"):
            if code_yassine.strip().lower() == "datasphere":
                st.success("✅ Historique de navigation récupéré. Brouillon trouvé : 'Bonjour, suite à notre entretien, je souhaite intégrer votre entreprise pour de nouveaux défis techniques.'")
            else:
                st.error("Échec de l'authentification réseau.")

    with tab3:
        st.subheader("Poste de Lina (Assistante de Direction)")
        st.write("Un test de sécurité anti-bot bloque l'accès à son bloc-notes.")
        st.markdown("Suite logique requise : **🔺 🟢 🟦 🔺 🟢 ?**")
        choix = st.radio("Sélectionnez la forme manquante pour déverrouiller :", ["--", "🔺 (Triangle rouge)", "🟦 (Carré bleu)", "🟢 (Cercle vert)"])
        if st.button("Valider le CAPTCHA de Lina"):
            if choix == "🟦 (Carré bleu)":
                st.success("✅ Note personnelle trouvée : 'Ce n’est pas toujours devant nous que l’on trouve les indices. Il faut parfois baisser les yeux... Le mot de passe de Mehdi est toujours la chose la plus simple possible.'")
            else:
                st.error("Analyse échouée. Modèle logique incorrect.")

    with tab4:
        st.subheader("Poste de Mehdi (Directeur Adjoint)")
        st.write("Le disque dur est protégé par un coffre-fort numérique à 5 chiffres. Résolvez son énigme mnémotechnique :")
        st.markdown("""
        *Le code correspond au nombre de lettres de chaque réponse :*
        1. On le résout ou on le pose ? (8 lettres)
        2. Il met fin légalement à un mariage ? (7 lettres)
        3. Sentiment d'amertume après un espoir envolé ? (9 lettres)
        4. Il peut nouer l'estomac avant un examen ? (7 lettres)
        5. L'unité de base de la société, ou le premier cercle ? (7 lettres)
        """)
        code_mehdi = st.text_input("Code PIN du coffre (5 chiffres) :", key="mehdi")
        if st.button("Déverrouiller le disque de Mehdi"):
            if code_mehdi.strip() == "87977":
                st.success("✅ DISQUE DÉVERROUILLÉ ! Fichier confidentiel : Convocation judiciaire attestant d'une faillite personnelle imminente et de dettes de jeu astronomiques. Facture récente pour l'achat d'une montre de luxe en argent massif.")
            else:
                st.error("Code PIN erroné. Accès refusé.")

    st.write("---")
    if st.button("Lancer l'interface d'accusation"):
        st.session_state.step = 4
        st.rerun()

# ==========================================
# ÉTAPE 4 : Verdict Final
# ==========================================
elif st.session_state.step == 4:
    st.markdown("<h2 class='main-title' style='color:#FF4136; text-shadow: 0px 0px 15px rgba(255, 65, 54, 0.7);'>RAPPORT D'ENQUÊTE FINAL</h2>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:rgba(0,0,0,0.7); padding: 20px; border-radius:10px; color:white;'>Vous avez rassemblé toutes les preuves. L'ombre sur la caméra, le mobile financier, les faux-semblants... Qui a volé le projet ORION et l'a vendu à DataSphere ?</div><br>", unsafe_allow_html=True)
    
    coupable = st.selectbox("Émettre un mandat d'arrêt contre :", ["-- Sélectionner le coupable --", "Sarah Benali", "Yassine Gharbi", "Mehdi Trabelsi", "Lina Kacem"])
    
    if st.button("Valider l'accusation"):
        if coupable == "Mehdi Trabelsi":
            st.balloons()
            st.success("🎉 AFFAIRE RÉSOLUE ! Accablé de dettes, Mehdi (le Directeur Adjoint) a utilisé ses privilèges pour dérober le code ORION et le vendre à la concurrence. Son unique erreur ? Avoir gardé sa montre fétiche au poignet lors de son infiltration nocturne !")
        elif coupable != "-- Sélectionner le coupable --":
            st.error("❌ FAUSSE PISTE ! Le vrai coupable court toujours. Relisez attentivement les indices des disques durs.")
