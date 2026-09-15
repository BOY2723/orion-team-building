import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TechNova OS | Projet ORION", page_icon="🏢", layout="wide")

# ==========================================
# INITIALISATION DES VARIABLES DE SESSION
# ==========================================
if "step" not in st.session_state:
    st.session_state.step = 1
if "etape2_success" not in st.session_state:
    st.session_state.etape2_success = False
if "etape3_success" not in st.session_state:
    st.session_state.etape3_success = False

for suspect in ["sarah", "yassine", "lina", "mehdi"]:
    if f"doc_{suspect}_unlocked" not in st.session_state:
        st.session_state[f"doc_{suspect}_unlocked"] = False

def passer_etape_3():
    st.session_state.step = 3
    st.session_state.etape2_success = False

def passer_etape_4():
    st.session_state.step = 4
    st.session_state.etape3_success = False

# ==========================================
# GESTION DES ARRIÈRE-PLANS
# ==========================================
backgrounds = {
    1: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2000&auto=format&fit=crop", 
    2: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2000&auto=format&fit=crop", 
    3: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?q=80&w=2000&auto=format&fit=crop", 
    4: "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2000&auto=format&fit=crop", 
    5: "https://images.unsplash.com/photo-1533422902700-50b208b73c8e?q=80&w=2000&auto=format&fit=crop"  
}
bg_url = backgrounds.get(st.session_state.step, backgrounds[1])

# CSS Avancé
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(5, 10, 15, 0.90), rgba(5, 10, 15, 0.95)), url('{bg_url}');
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .main-title {{
        color: #00FF41; font-family: 'Courier New', Courier, monospace; text-align: center;
        text-shadow: 0px 0px 10px rgba(0, 255, 65, 0.6); margin-bottom: 30px; letter-spacing: 2px;
    }}
    .terminal-box {{
        background-color: rgba(0, 20, 0, 0.8); border: 1px solid #00FF41; padding: 25px;
        border-radius: 5px; font-family: 'Courier New', Courier, monospace; color: #00FF41;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.2); margin-bottom: 20px;
    }}
    .document-box {{
        background-color: rgba(240, 240, 240, 0.95); border-left: 6px solid #4CAF50;
        padding: 20px; border-radius: 3px; font-family: 'Times New Roman', Times, serif; 
        color: #1a1a1a; margin-top: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}
    .doc-header {{
        border-bottom: 2px solid #ccc; margin-bottom: 15px; padding-bottom: 5px;
        font-family: 'Courier New', Courier, monospace; font-size: 0.9em; color: #555;
    }}
    .badge-card {{
        background: linear-gradient(135deg, #1f1f1f, #0a0a0a); border: 2px solid #4CAF50; 
        border-radius: 10px; padding: 20px; text-align: center; width: 320px; 
        margin: 0 auto 20px auto; box-shadow: 0 4px 15px rgba(0,255,65,0.4);
    }}
    .hacker-grid {{
        font-family: 'Courier New', Courier, monospace; font-size: 1.1rem; letter-spacing: 8px;
        color: #a8b2d1; background: #0a192f; padding: 25px; text-align: center; border-radius: 5px;
        line-height: 1.8; border: 1px solid #64ffda;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>TechNova Corp // SYSTEME DE SECURITE INTERNE</h1>", unsafe_allow_html=True)

# ==========================================
# ÉTAPE 1 : Accès au Système
# ==========================================
if st.session_state.step == 1:
    st.markdown("<div class='terminal-box'>[ERREUR CRITIQUE] : Base de données ORION compromise.<br>Les portes du département R&D sont verrouillées. Identifiez-vous au scanner mural pour commencer l'investigation.</div>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='badge-card'>
            <h3 style='color: white; margin-bottom: 5px;'>BADGE INVESTIGATEUR</h3>
            <div style='background-color: #4CAF50; height: 3px; width: 100%; margin-bottom: 15px;'></div>
            <p style='color: gray; font-size: 12px; margin-bottom: 5px;'>ID SCAN : 849-B / NIVEAU MAX</p>
            <h2 style='color: #00FF41; letter-spacing: 4px; font-family: "Courier New";'>NOIRO ATAD</h2>
            <p style='color: gray; font-size: 11px; margin-top: 15px;'>Accès autorisé aux serveurs centraux</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    code_input = st.text_input("Vérification d'identité (Saisissez l'ID Visuel) :", placeholder="Mot de passe...")
    if st.button("Déverrouiller les portes"):
        if code_input.strip().upper() == "ORION DATA":
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Accès refusé. La sécurité a été alertée.")

# ==========================================
# ÉTAPE 2 : Décodage du message
# ==========================================
elif st.session_state.step == 2:
    st.header("Étape 2 : Extraction des logs réseau")
    
    st.markdown("<div class='terminal-box'>[ANALYSEUR DE PAQUETS] : Un fichier de communication a été envoyé vers un serveur externe.<br><br><i>Note de l'analyste : Le hacker a tenté d'avancer masqué, mais la trace de son algorithme montre qu'il a dû <b>reculer de cinq pas</b> pour brouiller les pistes.</i></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='terminal-box'>MESSAGE EXTRAIT :<br><br><b>Zs htzufgqj ufwrn stzx, xznaje qjx nsinhjx utzw qj ywtzajw.</b></div>", unsafe_allow_html=True)
    
    st.write("Déchiffrez l'entête du message. Pour calibrer le traducteur, entrez les **deux premiers mots** du texte décodé.")
    
    cesar_input = st.text_input("Entête du message (2 mots) :")
    
    if st.button("Forcer le déchiffrement"):
        reponse = cesar_input.strip().lower()
        if reponse == "un coupable" or reponse.startswith("un coupable parmi nous"):
            st.session_state.etape2_success = True
        else:
            st.session_state.etape2_success = False
            st.error("Algorithme incorrect. Les données restent cryptées.")

    if st.session_state.etape2_success:
        st.success("✅ Traduction complétée : 'Un coupable parmi nous, suivez les indices pour le trouver.'")
        st.info("Le système de vidéosurveillance de la salle des serveurs est maintenant accessible.")
        st.button("Ouvrir les caméras de sécurité", on_click=passer_etape_3)

# ==========================================
# ÉTAPE 3 : Ordonnancement & Traitement d'image
# ==========================================
elif st.session_state.step == 3:
    st.header("Étape 3 : Restauration de la caméra 04")
    st.markdown("<div class='terminal-box'>[SYSTÈME VIDÉO] : Le fichier d'enregistrement de 23h30 (heure du vol) a été fragmenté. Vous devez réaligner les processeurs de rendu pour reconstituer la frame image par image.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    **Protocole de compilation vidéo :**
    1. Identifier les processeurs n'ayant **aucun antécédent** dans la matrice et les placer en tête.
    2. Purger leurs liaisons.
    3. Répéter l'opération en cascade jusqu'à l'ordonnancement total.
    """)
    
    st.write("Matrice des dépendances extraite du cache :")
    st.markdown("""
    | Images \ Processeurs | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | **I1** | | | 2 | 3 | 4 | | 1 |
    | **I2** | 3 | | 1 | | 4 | 2 | |
    | **I3** | 4 | 2 | | | | 3 | 1 |
    | **I4** | | 2 | | 1 | 4 | 3 | |
    """)

    reponse_etape3 = st.text_input("Séquence de boot des processeurs (7 chiffres) :")
    
    if st.button("Lancer le rendu vidéo"):
        if reponse_etape3.strip() == "7342615":
            st.session_state.etape3_success = True
        else:
            st.error("Erreur de segmentation. L'ordre provoque une surcharge.")
            st.session_state.etape3_success = False

    if st.session_state.etape3_success:
        st.success("✅ Rendu terminé ! L'image est sombre. On distingue une silhouette à 23h34 tapant le code d'extraction de données. \n\n**DÉTAILS CRUCIAUX OBSERVÉS PAR L'IA :**\n1. La personne porte une **montre en argent massif** très brillante.\n2. L'analyse cinétique montre que la personne **tape au clavier à une vitesse estimée de 120 mots/minute** (vitesse de frappe professionnelle).")
        st.info("Fouillez les disques durs. Lisez TOUT avec un esprit critique d'ingénieur. Les évidences sont souvent des pièges.")
        st.button("Accéder aux bureaux virtuels", on_click=passer_etape_4)

# ==========================================
# ÉTAPE 4 : Investigation Numérique (Les Dossiers)
# ==========================================
elif st.session_state.step == 4:
    st.header("Étape 4 : Fouille des terminaux de travail")
    st.markdown("<div class='terminal-box'>[RÉSEAU INTERNE] : Connecté aux postes. Analysez les documents. Croisez les alibis. Méfiez-vous des apparences.</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📁 Sarah (Projet)", "📁 Yassine (Réseau)", "📁 Lina (Assistante)", "📁 Mehdi (Direction)"])

    # --- BUREAU DE SARAH ---
    with tab1:
        st.subheader("Terminal de Sarah Benali")
        st.write("Trouvez la commande source dissimulée (2 mots en anglais) pour récupérer ses mémos vocaux.")
        st.markdown("""
        <div class='hacker-grid'>
        A T K W Q P Z L X O V<br>
        B M A R T I F I C I A L<br>
        R K M O N D A S M X P<br>
        W P I N T E L L I G E N C E<br>
        V C H J K M T R Z N S
        </div>
        """, unsafe_allow_html=True)
        code_sarah = st.text_input("Commande d'extraction :", key="sarah")
        
        if st.button("Exécuter", key="btn_sarah"):
            if code_sarah.strip().lower() in ["artificial intelligence", "intelligence artificielle"]:
                st.session_state.doc_sarah_unlocked = True
            else:
                st.error("Commande introuvable.")

        if st.session_state.doc_sarah_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>MÉMO VOCAL TRANSCRIT | 19:45 (Hier)</div>
                "L'ambiance est insupportable. Mehdi est sous l'eau avec ses dettes, il a passé la journée à hurler sur tout le monde. En plus, lors du pot de départ à 18h, <b>il a perdu sa fameuse montre en argent massif</b> qu'il venait d'acheter. Il était paniqué. Quelqu'un a dû la ramasser dans la salle de pause, mais personne ne s'est dénoncé."
            </div>
            """, unsafe_allow_html=True)

    # --- BUREAU DE YASSINE ---
    with tab2:
        st.subheader("Terminal de Yassine Gharbi")
        st.write("Complétez la séquence des ports pour accéder au log de sécurité :")
        st.markdown("<div class='terminal-box'>Port 2 -> Port 6 -> Port 14 -> Port 30 -> Port ?</div>", unsafe_allow_html=True)
        code_yassine = st.text_input("Port de destination final :", key="yassine")
        
        if st.button("Craquer", key="btn_yassine"):
            if code_yassine.strip() == "62":
                st.session_state.doc_yassine_unlocked = True
            else:
                st.error("Connexion refusée.")

        if st.session_state.doc_yassine_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>RAPPORT D'AUDIT SÉCURITÉ | 08:00 (Ce matin)</div>
                "Le piratage de 23h30 a été réalisé depuis l'ordinateur de Direction (Mehdi). 
                Cependant, une anomalie me frappe : le keylogger du serveur a enregistré une <b>vitesse de frappe de 125 mots par minute</b> lors de la saisie des commandes d'exfiltration. C'est impossible que ce soit Mehdi : il tape avec deux doigts en regardant son clavier (maximum 30 mots/minute). Quelqu'un d'autre était derrière son écran."
            </div>
            """, unsafe_allow_html=True)

    # --- BUREAU DE LINA ---
    with tab3:
        st.subheader("Terminal de Lina Kacem")
        st.write("Lina, ancienne étudiante en GI, a verrouillé son PC avec un problème de combinatoire.")
        st.info("« Le comité d'organisation TechNova doit être formé de **3 membres** choisis parmi un groupe de **8 ingénieurs**. Cependant, deux de ces ingénieurs (A et B) sont en conflit et refusent catégoriquement de faire partie du même comité ensemble. Combien de comités différents peut-on former ? »")
        code_lina = st.text_input("Nombre de combinaisons possibles :", key="lina")
        
        if st.button("Valider la solution mathématique", key="btn_lina"):
            # Solution : C(8,3) - C(6,1) = 56 - 6 = 50
            if code_lina.strip() == "50":
                st.session_state.doc_lina_unlocked = True
            else:
                st.error("Calcul erroné. Accès refusé.")

        if st.session_state.doc_lina_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>BROUILLON D'EMAIL SUPPRIMÉ | 23:55 (Hier) | Dest: Inconnu</div>
                "Le transfert du code source est terminé. J'ai utilisé le poste de Mehdi comme prévu. Ce crétin m'avait même donné son mot de passe pour que je lui imprime ses documents. Avec ses dettes de jeu, la direction sera convaincue que c'est lui qui a vendu ORION à DataSphere.<br><br>
                P.S : J'ai trouvé sa montre en argent dans la salle de pause, je l'ai portée pendant le téléchargement au cas où les caméras de secours fonctionneraient. Envoyez mon paiement en Bitcoin. Je quitte le pays demain."
            </div>
            """, unsafe_allow_html=True)

    # --- BUREAU DE MEHDI ---
    with tab4:
        st.subheader("Terminal de Mehdi Trabelsi")
        st.write("Code PIN de la direction (5 chiffres basés sur la longueur des mots).")
        st.markdown("""
        1. Un ingénieur GI cherche toujours à le maximiser.
        2. Instrument indiquant le Nord.
        3. Saison où les feuilles tombent.
        4. Organe vital dans la poitrine.
        5. L'opposé exact de la nuit.
        """)
        code_mehdi = st.text_input("Code PIN (5 chiffres) :", key="mehdi")
        
        if st.button("Déverrouiller", key="btn_mehdi"):
            if code_mehdi.strip() == "68754":
                st.session_state.doc_mehdi_unlocked = True
            else:
                st.error("Code PIN erroné.")

        if st.session_state.doc_mehdi_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>BLOC-NOTES DIRECTION | 18:45 (Hier)</div>
                "Je suis ruiné. Mes dettes de jeu ont fuité. Je suis tellement stressé que j'en ai perdu ma montre porte-bonheur en argent tout à l'heure. <br><br>
                J'ai demandé à Lina de chercher ma montre et de préparer mes dossiers pour demain. Je lui ai laissé mon PC déverrouillé car je n'arrivais plus à me concentrer. Heureusement qu'elle est là, son efficacité au clavier est redoutable (elle tape à la vitesse de l'éclair, on dirait un robot). Elle gère toute ma vie numérique en ce moment."
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.info("Avez-vous bien croisé TOUTES les informations ? La réponse la plus évidente est souvent un piège.")
    if st.button("Ouvrir l'interface de mise en accusation"):
        st.session_state.step = 5
        st.rerun()

# ==========================================
# ÉTAPE 5 : Verdict Final
# ==========================================
elif st.session_state.step == 5:
    st.markdown("<h2 class='main-title' style='color:#FF4136;'>MANDAT D'ARRÊT NUMÉRIQUE</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='terminal-box' style='border-color: #FF4136; color: #fff;'>
    <b>ATTENTION :</b> Vous n'avez droit qu'à une seule chance. Si vous accusez un innocent, le vrai coupable s'échappera avec les données d'ORION. Réfléchissez comme de vrais ingénieurs.
    </div>
    """, unsafe_allow_html=True)
    
    coupable = st.selectbox("Désigner le cerveau de l'opération :", ["-- Sélectionner --", "Sarah Benali (Cheffe de Projet)", "Yassine Gharbi (Réseau)", "Mehdi Trabelsi (Dir. Adjoint)", "Lina Kacem (Assistante)"])
    
    if st.button("Lancer le protocole d'arrestation"):
        if coupable == "Lina Kacem (Assistante)":
            st.balloons()
            st.success("🎉 DÉDUCTION MAGISTRALE ! L'AFFAIRE EST RÉSOLUE !")
            st.markdown("""
            **Rapport de clôture :**
            Félicitations, vous n'êtes pas tombés dans le piège ! Mehdi était le coupable idéal (dettes, ordinateur utilisé, montre sur la vidéo). 
            
            Mais votre esprit d'analyse a fait la différence : 
            1. Yassine a prouvé que la personne tapait très vite au clavier (Mehdi est lent, Lina est experte).
            2. Sarah a confirmé que Mehdi avait perdu sa montre avant le vol.
            3. Mehdi a avoué avoir laissé son PC déverrouillé à Lina.
            4. Lina a mis la montre de Mehdi pour faire diversion et l'accuser à sa place.
            
            **Le Club GI ENIT a brillamment sauvé le projet ORION !**
            """)
        elif coupable == "Mehdi Trabelsi (Dir. Adjoint)":
            st.error("❌ ÉCHEC CRITIQUE ! Vous êtes tombés dans le panneau de la facilité.")
            st.warning("Indice : Mehdi avait des dettes, oui. Mais avez-vous lu l'anomalie sur la vitesse de frappe au clavier (Dossier Yassine) ? Et avez-vous noté que Mehdi avait perdu sa montre AVANT l'heure du vol (Dossier Sarah) ? Cherchez qui l'a manipulé !")
        elif coupable != "-- Sélectionner --":
            st.error("❌ ÉCHEC CRITIQUE ! Vous accusez un innocent.")
