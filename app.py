import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TechNova OS | Opération ORION", page_icon="🕵️", layout="wide")

# Initialisation des variables de session
if "step" not in st.session_state:
    st.session_state.step = 1
if "etape3_success" not in st.session_state:
    st.session_state.etape3_success = False
# Initialisation des variables de session
if "step" not in st.session_state:
    st.session_state.step = 1
if "etape2_success" not in st.session_state:
    st.session_state.etape2_success = False
if "etape3_success" not in st.session_state:
    st.session_state.etape3_success = False
# ==========================================
# GESTION DES ARRIÈRE-PLANS
# ==========================================
backgrounds = {
    1: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2000&auto=format&fit=crop", # Code Matrix / Cyber
    2: "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?q=80&w=2000&auto=format&fit=crop", # Message intercepté / Ondes
    3: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?q=80&w=2000&auto=format&fit=crop", # Caméra de sécurité
    4: "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2000&auto=format&fit=crop", # Bureaux d'entreprise
    5: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=2000&auto=format&fit=crop"  # Verdict
}
bg_url = backgrounds.get(st.session_state.step, backgrounds[1])

# CSS Avancé (incluant le design du badge)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(10, 14, 18, 0.90), rgba(10, 14, 18, 0.95)), url('{bg_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-title {{
        color: #00FF41; font-family: 'Courier New', Courier, monospace; text-align: center;
        text-shadow: 0px 0px 10px rgba(0, 255, 65, 0.6); margin-bottom: 30px;
    }}
    .terminal-box {{
        background-color: rgba(0, 20, 0, 0.7); border: 1px solid #00FF41; padding: 25px;
        border-radius: 5px; font-family: 'Courier New', Courier, monospace; color: #00FF41;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.1); margin-bottom: 20px;
    }}
    .badge-card {{
        background: linear-gradient(135deg, #1f1f1f, #0a0a0a);
        border: 2px solid #4CAF50; border-radius: 10px; padding: 20px;
        text-align: center; width: 320px; margin: 0 auto 20px auto;
        box-shadow: 0 4px 15px rgba(0,255,65,0.4);
    }}
    .sys-alert {{
        background-color: rgba(220, 53, 69, 0.1); border-left: 5px solid #dc3545;
        padding: 15px; color: #f8f9fa; margin-bottom: 20px; font-family: sans-serif;
    }}
    .hacker-grid {{
        font-family: 'Courier New', Courier, monospace; font-size: 1.2rem; letter-spacing: 5px;
        color: #00FF41; background: #000; padding: 20px; text-align: center; border-radius: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>TechNova_OS // TERMINAL D'ENQUÊTE</h1>", unsafe_allow_html=True)

# ==========================================
# ÉTAPE 1 : Accès au Système (AVEC LE BADGE)
# ==========================================
if st.session_state.step == 1:
    st.markdown("<div class='terminal-box'>[REQUÊTE SYSTÈME] : ALERTE SÉCURITÉ.<br>Protocole ORION compromis. Veuillez scanner votre badge digital pour accéder au serveur d'enquête principal.</div>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='badge-card'>
            <h3 style='color: white; margin-bottom: 5px;'>BADGE ACCÈS VISITEUR</h3>
            <div style='background-color: #4CAF50; height: 3px; width: 100%; margin-bottom: 15px;'></div>
            <p style='color: gray; font-size: 12px; margin-bottom: 5px;'>ID SCAN : 849-B / NIVEAU 1</p>
            <h2 style='color: #00FF41; letter-spacing: 4px; font-family: "Courier New";'>NOIRO ATAD</h2>
            <p style='color: gray; font-size: 11px; margin-top: 15px;'>TechNova Corp. - STRICTEMENT PERSONNEL</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    code_input = st.text_input("Saisissez le mot de passe :", placeholder="ID Visuel")
    if st.button("Initialiser la connexion"):
        if code_input.strip().upper() == "ORION DATA":
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Authentification échouée. Empreinte non reconnue.")

# ==========================================
# ÉTAPE 2 : Décodage du message (Code César Modifié)
# ==========================================
elif st.session_state.step == 2:
    st.header("Étape 2 : Interception de communication")
    
    # L'indice caché est ici au lieu du "-5" explicite
    st.markdown("<div class='sys-alert'>ALERTE : Un paquet de données crypté a été intercepté. <br><i>Note de l'analyste : Le hacker a tenté d'avancer masqué, mais la trace de son algorithme montre qu'il a dû <b>reculer de cinq pas</b> pour brouiller les pistes.</i></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='terminal-box'>MESSAGE INTERCEPTÉ :<br><br><b>Zs htzufgqj ufwrn stzx, xznaje qjx nsinhjx utzw qj ywtzajw.</b></div>", unsafe_allow_html=True)
    
    st.write("Déchiffrez le message. Pour prouver que vous avez compris, entrez les **deux premiers mots** du message décodé.")
    
    cesar_input = st.text_input("Les deux premiers mots du message :")
    if st.button("Déchiffrer le paquet"):
        reponse = cesar_input.strip().lower()
        # Le système accepte "un coupable" OU la phrase complète (en ignorant la ponctuation finale)
        if reponse == "un coupable" or reponse.startswith("un coupable parmi nous"):
            st.success("✅ Message décodé : 'Un coupable parmi nous, suivez les indices pour le trouver.'")
            st.info("Le pare-feu est tombé. Accès aux caméras autorisé.")
            if st.button("Connecter au flux de vidéosurveillance"):
                st.session_state.step = 3
                st.rerun()
        else:
            st.error("Traduction incorrecte. Le système rejette votre requête.")
# ==========================================
# ÉTAPE 3 : Ordonnancement & Traitement d'image
# ==========================================
elif st.session_state.step == 3:
    st.header("Étape 3 : Restauration du flux vidéo")
    st.markdown("<div class='sys-alert'>Rapport de sécurité : Le fichier vidéo de 23h30 a été fragmenté par le pirate. Vous devez réaligner les processeurs de rendu pour reconstituer l'image.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    **Protocole d'alignement des processeurs :**
    Le système utilise 4 noyaux d'images intermédiaires (I1, I2, I3, I4) traités par 7 processeurs (P1 à P7).
    Pour compiler la vidéo sans faire crasher le serveur, vous devez :
    1. Établir l'ordre strict d'exécution en identifiant les processeurs n'ayant **aucun antécédent** dans la matrice.
    2. Les placer en tête de séquence, puis purger leurs liaisons.
    3. Répéter l'opération en cascade jusqu'à l'ordonnancement total.
    """)
    
    st.write("Matrice des dépendances processeurs extraite :")
    st.markdown("""
    | Processeurs \ Images | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | **I1** | | | 2 | 3 | 4 | | 1 |
    | **I2** | 3 | | 1 | | 4 | 2 | |
    | **I3** | 4 | 2 | | | | 3 | 1 |
    | **I4** | | 2 | | 1 | 4 | 3 | |
    """)

    reponse_etape3 = st.text_input("Séquence numérique finale (7 chiffres) :")
    
    if st.button("Compiler la vidéo"):
        if reponse_etape3.strip() == "7342615":
            st.session_state.etape3_success = True
        else:
            st.error("Crash système. L'ordre des processeurs est incorrect.")
            st.session_state.etape3_success = False

    if st.session_state.etape3_success:
        st.success("✅ Séquence vidéo restaurée ! Sur l'image floue, vous distinguez une silhouette accédant au serveur principal. Détail troublant : la personne porte une montre en argent massif très spécifique.")
        if st.button("Infiltrer les disques durs des suspects"):
            st.session_state.step = 4
            st.session_state.etape3_success = False
            st.rerun()

# ==========================================
# ÉTAPE 4 : Investigation Numérique
# ==========================================
elif st.session_state.step == 4:
    st.header("Étape 4 : Serveurs Personnels")
    st.markdown("<div class='terminal-box'>Connecté au réseau interne. Extraction des données des 4 profils suspects. Chaque dossier est verrouillé par la logique personnelle de son propriétaire.</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["💻 Sarah Benali", "💻 Yassine Gharbi", "💻 Lina Kacem", "💻 Mehdi Trabelsi"])

    with tab1:
        st.subheader("Disque de Sarah (Cheffe de Projet)")
        st.write("Un fichier crypté contient les derniers échanges de Sarah. Le mot de passe est dissimulé dans ce dump mémoire. Cherchez deux mots (en anglais).")
        st.markdown("""
        <div class='hacker-grid'>
        A T K W Q P Z L<br>
        R A R T I F I C I A L<br>
        M O N D A S E X<br>
        X P I N T E L L I G E N C E<br>
        V C H J K M T R
        </div>
        """, unsafe_allow_html=True)
        code_sarah = st.text_input("Mot de passe (2 mots) :", key="sarah")
        if st.button("Déchiffrer Sarah"):
            if code_sarah.strip().lower() in ["artificial intelligence", "intelligence artificielle"]:
                st.success("✅ **Preuve récupérée :** Email de Sarah à un chasseur de tête. *'Je refuse catégoriquement l'offre financière de vos clients. Le projet ORION appartient à TechNova, j'y ai mis trop d'années de travail pour le trahir.'* -> Elle est loyale.")
            else:
                st.error("Accès refusé.")

    with tab2:
        st.subheader("Disque de Yassine (Ingénieur Réseau)")
        st.write("Le pare-feu de Yassine est basé sur une séquence logique de paquets réseau. Complétez la suite pour trouver le port de destination.")
        st.markdown("<div class='terminal-box'>Paquets envoyés sur les ports :<br>Port 2<br>Port 6<br>Port 14<br>Port 30<br>Port ?</div>", unsafe_allow_html=True)
        code_yassine = st.text_input("Numéro du port final :", key="yassine")
        if st.button("Forcer le pare-feu"):
            if code_yassine.strip() == "62":
                st.success("✅ **Preuve récupérée :** Historique web. Yassine passait ses nuits à postuler à d'autres emplois très ordinaires. Lettre de motivation trouvée : *'Je cherche une entreprise avec moins de pression.'* -> Il voulait juste partir légalement.")
            else:
                st.error("Mauvais port. Connexion rejetée.")

    with tab3:
        st.subheader("Disque de Lina (Assistante de Direction)")
        st.write("Lina protège ses notes avec une énigme liée à son emploi du temps.")
        st.info("« L'incident réseau a eu lieu un jour précis. Ce n'est pas le lendemain de lundi, ni la veille de vendredi. Ce n'est pas non plus le jour où je rédige les comptes-rendus de réunion (mercredi). Quel jour sommes-nous ? »")
        code_lina = st.text_input("Jour de la semaine :", key="lina")
        if st.button("Ouvrir les notes"):
            if code_lina.strip().lower() == "jeudi":
                st.success("✅ **Preuve récupérée :** Journal de bord de Lina. *'J'ai quitté le bureau à 18h. Mais j'ai remarqué que Mehdi était étrangement nerveux. Il a annulé tous ses rendez-vous de la semaine et m'a demandé de ne laisser aucune trace de ses appels vers des numéros étrangers.'*")
            else:
                st.error("Erreur de calendrier.")

    with tab4:
        st.subheader("Disque de Mehdi (Directeur Adjoint)")
        st.write("Le coffre-fort numérique de Mehdi exige un code PIN à 5 chiffres. Résolvez les définitions : **le code est le nombre de lettres de chaque réponse.**")
        st.markdown("""
        1. On le résout grâce à la recherche opérationnelle.
        2. Instrument à aiguille qui indique toujours le Nord.
        3. Saison où les feuilles tombent des arbres.
        4. Organe qui bat dans notre poitrine.
        5. Le contraire exact de la nuit.
        """)
        code_mehdi = st.text_input("Code PIN (5 chiffres) :", key="mehdi")
        if st.button("Déverrouiller le coffre"):
            if code_mehdi.strip() == "88754":
                st.success("✅ **Preuve récupérée :** Relevé bancaire offshore à 23h35 (heure du vol). Virement entrant de 2 millions. Juste à côté, des avis d'huissiers pour des dettes de poker colossales. Et la facture pour une montre en argent massif sur-mesure.")
            else:
                st.error("Code PIN erroné.")

    st.write("---")
    if st.button("Ouvrir l'interface d'inculpation finale"):
        st.session_state.step = 5
        st.rerun()

# ==========================================
# ÉTAPE 5 : Verdict Final
# ==========================================
elif st.session_state.step == 5:
    st.markdown("<h2 class='main-title' style='color:#FF4136;'>MANDAT D'ARRÊT NUMÉRIQUE</h2>", unsafe_allow_html=True)
    st.markdown("<div class='sys-alert'>D'après les logs, les motivations et les alibis... Qui a dérobé ORION ?</div>", unsafe_allow_html=True)
    
    coupable = st.selectbox("Désigner le coupable :", ["-- Sélectionner --", "Sarah Benali", "Yassine Gharbi", "Mehdi Trabelsi", "Lina Kacem"])
    
    if st.button("Confirmer l'arrestation"):
        if coupable == "Mehdi Trabelsi":
            st.balloons()
            st.success("🎉 AFFAIRE RÉSOLUE ! Acculé par ses dettes de jeu, Mehdi a utilisé son accès de direction pour voler le code source. La montre en argent visible sur la vidéo restaurée et l'heure du virement offshore l'ont définitivement confondu. L'équipe du Club GI a sauvé TechNova !")
        elif coupable != "-- Sélectionner --":
            st.error("❌ INCOHÉRENCE DANS L'ENQUÊTE. Les preuves innocentent cette personne. Relisez attentivement les documents trouvés dans les dossiers.")
