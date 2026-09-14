import streamlit as st
import time

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

# Variables pour mémoriser la découverte des indices
for suspect in ["sarah", "yassine", "lina", "mehdi"]:
    if f"doc_{suspect}_unlocked" not in st.session_state:
        st.session_state[f"doc_{suspect}_unlocked"] = False

# Fonctions de transition
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
    1: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2000&auto=format&fit=crop", # Salle de serveurs sécurisée
    2: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2000&auto=format&fit=crop", # Code vert Matrix / Cyber
    3: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?q=80&w=2000&auto=format&fit=crop", # Murs d'écrans de sécurité
    4: "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2000&auto=format&fit=crop", # Bureaux d'entreprise sombres, documents
    5: "https://images.unsplash.com/photo-1533422902700-50b208b73c8e?q=80&w=2000&auto=format&fit=crop"  # Gyrophares de police dans la nuit
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
    
    st.markdown("<div class='terminal-box'>[ANALYSEUR DE PAQUETS] : Un fichier de communication a été envoyé vers un serveur externe (IP appartenant à l'entreprise concurrente DataSphere).<br><br><i>Note de l'analyste : Le hacker a tenté d'avancer masqué, mais la trace de son algorithme montre qu'il a dû <b>reculer de cinq pas</b> pour brouiller les pistes.</i></div>", unsafe_allow_html=True)
    
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
    Le système utilise 4 noyaux d'images intermédiaires (I1, I2, I3, I4) traités par 7 processeurs (P1 à P7).
    Pour compiler la vidéo sans faire crasher le serveur, vous devez :
    1. Identifier les processeurs n'ayant **aucun antécédent** dans la matrice et les placer en tête.
    2. Purger leurs liaisons.
    3. Répéter l'opération en cascade jusqu'à l'ordonnancement total.
    """)
    
    st.write("Matrice des dépendances extraite du cache :")
    st.markdown("""
    | Processeurs \ Images | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | **I1** | | | 2 | 3 | 4 | | 1 |
    | **I2** | 3 | | 1 | | 4 | 2 | |
    | **I3** | 4 | 2 | | | | 3 | 1 |
    | **I4** | | 2 | | 1 | 4 | 3 | |
    """)

    reponse_etape3 = st.text_input("Séquence de boot des processeurs (7 chiffres continus) :")
    
    if st.button("Lancer le rendu vidéo"):
        if reponse_etape3.strip() == "7342615":
            st.session_state.etape3_success = True
        else:
            st.error("Erreur de segmentation. L'ordre provoque une surcharge.")
            st.session_state.etape3_success = False

    if st.session_state.etape3_success:
        st.success("✅ Rendu terminé à 100% ! Une silhouette est visible dans la salle des serveurs à 23h34. L'image est sombre, mais un éclat métallique trahit une **montre au poignet gauche de l'individu**.")
        st.info("Nous devons fouiller les disques durs des 4 personnes présentes dans le bâtiment ce soir-là pour croiser les alibis.")
        st.button("Accéder aux bureaux virtuels", on_click=passer_etape_4)

# ==========================================
# ÉTAPE 4 : Investigation Numérique (Les Dossiers)
# ==========================================
elif st.session_state.step == 4:
    st.header("Étape 4 : Fouille des terminaux de travail")
    st.markdown("<div class='terminal-box'>[RÉSEAU INTERNE] : Connecté aux postes de travail. Lisez attentivement les documents trouvés. Chaque détail compte pour l'accusation finale.</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📁 Sarah Benali (Cheffe de Projet)", "📁 Yassine Gharbi (Réseau)", "📁 Lina Kacem (Assistante)", "📁 Mehdi Trabelsi (Dir. Adjoint)"])

    # --- BUREAU DE SARAH ---
    with tab1:
        st.subheader("Terminal de Sarah Benali")
        st.write("Sarah a mis en place un script de nettoyage sur ses brouillons d'emails. Pour récupérer le dernier message effacé, trouvez la commande source dissimulée dans ce dump mémoire (2 mots en anglais).")
        st.markdown("""
        <div class='hacker-grid'>
        A T K W Q P Z L X O V<br>
        B M A R T I F I C I A L<br>
        R K M O N D A S E X P<br>
        W P I N T E L L I G E N C E<br>
        V C H J K M T R Z N S
        </div>
        """, unsafe_allow_html=True)
        code_sarah = st.text_input("Commande d'extraction (2 mots) :", key="sarah")
        
        if st.button("Exécuter le script", key="btn_sarah"):
            if code_sarah.strip().lower() in ["artificial intelligence", "intelligence artificielle"]:
                st.session_state.doc_sarah_unlocked = True
            else:
                st.error("Commande introuvable.")

        if st.session_state.doc_sarah_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>EXPÉDITEUR: S. Benali | DESTINATAIRE: Recrutement@DataSphere.com | OBJET: Re: Offre de rachat</div>
                Je vous l'ai déjà dit, je refuse votre chèque. Le projet ORION est l'aboutissement de mes recherches, il appartient à TechNova.<br><br>
                Par contre, dites à votre PDG d'arrêter de soudoyer mes collègues. Hier, j'ai retrouvé <b>mon ordinateur allumé sur le bureau de Mehdi</b>. Quelqu'un s'est servi de mon compte pour vérifier l'architecture des serveurs. N'essayez plus de me contacter.
            </div>
            """, unsafe_allow_html=True)

    # --- BUREAU DE YASSINE ---
    with tab2:
        st.subheader("Terminal de Yassine Gharbi")
        st.write("Le journal des événements du pare-feu est protégé par un algorithme de routage. Complétez la séquence des ports utilisés pour le contournement :")
        st.markdown("<div class='terminal-box'>Séquence de test de vulnérabilité :<br>Port 2 -> Port 6 -> Port 14 -> Port 30 -> Port ?</div>", unsafe_allow_html=True)
        code_yassine = st.text_input("Port de destination final :", key="yassine")
        
        if st.button("Craquer l'algorithme", key="btn_yassine"):
            if code_yassine.strip() == "62":
                st.session_state.doc_yassine_unlocked = True
            else:
                st.error("Connexion au port refusée. Séquence brisée.")

        if st.session_state.doc_yassine_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>LOG SYSTÈME - PARE-FEU CENTRAL | HORODATAGE: 23:25</div>
                <b>ALERTE SÉCURITÉ :</b> Désactivation manuelle du pare-feu détectée.<br>
                <b>UTILISATEUR :</b> Inconnu.<br>
                <b>MÉTHODE :</b> Protocole 'Executive Override' (Privilèges exclusifs de la Direction).<br><br>
                <i>Note technique de Yassine : "Je ne comprends pas, seul le bureau de la direction possède les codes 'Executive Override'. Mon propre compte ingénieur n'a même pas les droits pour faire ça sans déclencher l'alarme générale."</i>
            </div>
            """, unsafe_allow_html=True)

    # --- BUREAU DE LINA ---
    with tab3:
        st.subheader("Terminal de Lina Kacem")
        st.write("Lina crypte ses notes de réunion grâce à un problème d'affectation de ressources (clin d'œil à son passé en Génie Industriel).")
        st.info("Trois dossiers stratégiques (D1, D2, D3) doivent être traités par trois employés (Alice, Bob, Charlie). Une seule règle : un dossier par personne. \n\n* Alice refuse catégoriquement le dossier D3.\n* Bob exige de travailler uniquement sur le dossier D1.\n\n**Quel dossier (D1, D2 ou D3) revient obligatoirement à Charlie ?**")
        code_lina = st.text_input("Dossier assigné à Charlie (ex: D1) :", key="lina")
        
        if st.button("Déchiffrer les notes", key="btn_lina"):
            if code_lina.strip().upper() == "D3":
                st.session_state.doc_lina_unlocked = True
            else:
                st.error("Erreur d'affectation. Accès refusé.")

        if st.session_state.doc_lina_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>BLOC-NOTES PERSONNEL (L. Kacem) | CONFIDENTIEL</div>
                L'ambiance est lourde aujourd'hui. Mehdi m'a demandé de bloquer son agenda pour toute la journée et d'annuler son vol de demain. <br><br>
                Plus étrange encore : il m'a donné l'ordre strict de placer les caméras du couloir ouest (celles qui mènent à la salle des serveurs) en 'maintenance programmée' hier soir à 23h00. Juste après, je l'ai entendu au téléphone discuter d'un paiement en cryptomonnaie avec un certain 'Contact D.S.'.
            </div>
            """, unsafe_allow_html=True)

    # --- BUREAU DE MEHDI ---
    with tab4:
        st.subheader("Terminal de Mehdi Trabelsi")
        st.write("Le coffre-fort numérique de la direction nécessite un code PIN à 5 chiffres. La longueur (nombre de lettres) des mots répondant à ces définitions forme le code.")
        st.markdown("""
        1. On l'optimise souvent en Génie Industriel grâce à la RO. (8 lettres)
        2. Instrument indiquant le Nord. (8 lettres)
        3. Saison où les feuilles tombent. (7 lettres)
        4. Organe vital dans la poitrine. (5 lettres)
        5. L'opposé exact de la nuit. (4 lettres)
        """)
        code_mehdi = st.text_input("Code PIN (5 chiffres) :", key="mehdi")
        
        if st.button("Déverrouiller le coffre de Direction", key="btn_mehdi"):
            if code_mehdi.strip() == "88754":
                st.session_state.doc_mehdi_unlocked = True
            else:
                st.error("Code PIN erroné. Tentative enregistrée.")

        if st.session_state.doc_mehdi_unlocked:
            st.markdown("""
            <div class='document-box'>
                <div class='doc-header'>DOSSIER FINANCIER CACHÉ | FICHIERS RÉCUPÉRÉS</div>
                - <b>Avis d'huissier :</b> Dettes de jeux clandestins s'élevant à plusieurs centaines de milliers de dinars. Menaces de saisie immobilière imminente.<br>
                - <b>Reçu d'achat (Hier, 14h00) :</b> Bijouterie de luxe. Achat d'une <i>montre en argent massif édition limitée</i>.<br>
                - <b>Notification Bancaire (23h45) :</b> Virement entrant de 2,5 millions depuis un compte offshore basé aux Îles Caïmans, rattaché à la société mère de DataSphere.
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.info("Avez-vous lu tous les documents et croisé les pistes ? Une fois l'accusation lancée, il n'y aura pas de retour en arrière.")
    if st.button("Ouvrir l'interface de mise en accusation"):
        st.session_state.step = 5
        st.rerun()

# ==========================================
# ÉTAPE 5 : Verdict Final
# ==========================================
elif st.session_state.step == 5:
    st.markdown("<h2 class='main-title' style='color:#FF4136; text-shadow: 0px 0px 15px rgba(255, 0, 0, 0.8);'>MANDAT D'ARRÊT NUMÉRIQUE</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='terminal-box' style='border-color: #FF4136; color: #fff;'>
    <b>RÉCAPITULATIF DES FAITS :</b><br>
    - Le vol a eu lieu à 23h30. Une montre en argent a été aperçue sur les caméras.<br>
    - Le pare-feu a été désactivé via un accès privilégié de Direction.<br>
    - Le code source était destiné à l'entreprise concurrente DataSphere.<br><br>
    <i>Croisez les témoignages et les preuves. Qui avait l'accès, le mobile, et l'opportunité ?</i>
    </div>
    """, unsafe_allow_html=True)
    
    coupable = st.selectbox("Désigner le coupable principal :", ["-- Sélectionner --", "Sarah Benali (Cheffe de Projet)", "Yassine Gharbi (Réseau)", "Mehdi Trabelsi (Dir. Adjoint)", "Lina Kacem (Assistante)"])
    
    if st.button("Lancer le protocole d'arrestation"):
        if coupable == "Mehdi Trabelsi (Dir. Adjoint)":
            st.balloons()
            st.success("🎉 AFFAIRE RÉSOLUE ! LE COUPABLE EST SOUS LES VERROUS.")
            st.markdown("""
            **Rapport de clôture de l'enquête :**
            Votre déduction est parfaite. Acculé par ses dettes de jeu, Mehdi Trabelsi a accepté l'offre de DataSphere (dont Sarah avait refusé les avances). 
            
            Il a ordonné à Lina de couper les caméras, mais la caméra 04 a pu être restaurée par votre équipe. Il a utilisé son privilège de direction ('Executive Override') pour contourner les défenses de Yassine, puis s'est servi du poste de Sarah pour voler le code d'ORION, espérant la faire accuser. L'heure du virement et l'achat de sa montre en argent massif ont scellé son destin.
            
            **Le Club GI ENIT a sauvé le projet ORION ! Félicitations à toute l'équipe !**
            """)
        elif coupable != "-- Sélectionner --":
            st.error("❌ ERREUR JUDICIAIRE. Les pièces du dossier contredisent cette hypothèse. Relisez les documents interceptés. Qui a utilisé un 'Executive Override' ? Qui avait besoin d'argent ?")
