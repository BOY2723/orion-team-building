import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Affaire ORION | Team Building GI", page_icon="🔍", layout="centered")

# Initialisation de la progression
if "step" not in st.session_state:
    st.session_state.step = 1

st.title("🕵️‍♂️ Enquête Interne : L'Affaire ORION")
st.markdown("---")

# ==========================================
# ÉTAPE 1 : Accès au Système
# ==========================================
if st.session_state.step == 1:
    st.header("Étape 1 : Le Poste Central")
    st.write("Le projet ORION a été compromis. Déchiffrez le badge d'accès pour entrer dans le système.")
    st.info("💡 Indice sur le badge : NOIRO ATAD")
    
    code_input = st.text_input("Entrez le mot de passe du système :")
    if st.button("Valider l'accès"):
        if code_input.strip().upper() == "ORION DATA":
            st.success("Accès autorisé !")
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Mot de passe incorrect.")

# ==========================================
# ÉTAPE 2 : Ordonnancement (GI)
# ==========================================
elif st.session_state.step == 2:
    st.header("Étape 2 : Restauration de l'Image")
    st.write("La caméra a capté une silhouette à 23h30, mais l'image est floue. Appliquez la méthode de mise en ligne des postes de traitement (P1 à P7) pour la restaurer.")
    
    reponse_etape2 = st.text_input("Entrez la séquence numérique exacte (ex: 1234567) :")
    if st.button("Restaurer l'image"):
        # La solution GI exacte de l'année dernière : P7 -> P3 -> P4 -> P2 -> P6 -> P1 -> P5
        if reponse_etape2.strip() == "7342615":
            st.success("Image restaurée ! Vous distinguez une montre brillante appartenant à un membre de l'équipe...")
            if st.button("Passer à l'inspection des bureaux"):
                st.session_state.step = 3
                st.rerun()
        else:
            st.error("Séquence incorrecte. Vérifiez vos antécédents !")

# ==========================================
# ÉTAPE 3 : Investigation des Bureaux
# ==========================================
elif st.session_state.step == 3:
    st.header("Étape 3 : Investigation des Bureaux")
    st.write("Analysez les indices physiques trouvés dans chaque bureau et entrez les codes pour débloquer les dossiers.")

    tab1, tab2, tab3, tab4 = st.tabs(["📁 Sarah", "📁 Yassine", "📁 Lina", "📁 Mehdi"])

    with tab1:
        st.subheader("Bureau de Sarah (Cheffe de Projet)")
        st.write("Résolvez la grille de mots mêlés. Quelle est la phrase cachée ?")
        code_sarah = st.text_input("Code de l'ordinateur de Sarah :", key="sarah")
        if st.button("Déverrouiller le PC de Sarah"):
            if code_sarah.strip().lower() in ["artificial intelligence", "intelligence artificielle"]:
                st.success("✅ Accès accordé. Vous trouvez un e-mail envoyé à DataSphere : 'Je refuse catégoriquement votre proposition de partenariat. TechNova n'a pas de nouveau projet à partager.'")
                st.info("🔎 Déduction : Elle est intègre et a protégé l'entreprise.")
            else:
                st.error("Code incorrect.")

    with tab2:
        st.subheader("Bureau de Yassine (Ingénieur Réseau)")
        st.write("Résolvez les mots croisés. Quel est le mot caché ?")
        code_yassine = st.text_input("Code du PC de Yassine :", key="yassine")
        if st.button("Déverrouiller le PC de Yassine"):
            if code_yassine.strip().lower() == "datasphere":
                st.success("✅ Accès accordé. Vous trouvez un brouillon d'e-mail : 'Bonjour, je souhaite intégrer votre entreprise. Je cherche de nouveaux défis hors de TechNova.'")
                st.info("🔎 Déduction : Il voulait partir, ce qui le rend suspect, mais cela prouve-t-il qu'il a volé le projet ?")
            else:
                st.error("Code incorrect.")

    with tab3:
        st.subheader("Bureau de Lina (Assistante)")
        st.write("En réussissant son test psychotechnique, vous accédez à ses notes d'observation.")
        if st.button("Lire les notes de Lina"):
            st.success("✅ Notes trouvées : 'Ce n’est pas toujours devant nous que l’on trouve les indices. Il faut parfois baisser les yeux... Le mot de passe le plus simple est toujours le plus sûr.'")

    with tab4:
        st.subheader("Bureau de Mehdi (Directeur Adjoint)")
        st.write("Un cadenas à combinaison de 5 chiffres verrouille le tiroir. Résolvez les devinettes (le code correspond au nombre de lettres de chaque réponse) :")
        st.markdown("1. On le résout ou on le pose ? (8 lettres)")
        st.markdown("2. Il met fin légalement à un mariage ? (7 lettres)")
        st.markdown("3. Amertume après un espoir envolé ? (9 lettres)")
        st.markdown("4. Il peut nouer l'estomac ? (7 lettres)")
        st.markdown("5. Premier cercle de l'amour ? (7 lettres)")
        
        # Solution : Problème (8), Divorce (7), Déception (9), Stresse (7), Famille (7) -> 87977
        code_mehdi = st.text_input("Entrez le code à 5 chiffres :", key="mehdi")
        if st.button("Ouvrir le tiroir de Mehdi"):
            if code_mehdi.strip() == "87977":
                st.success("✅ Tiroir ouvert ! Vous trouvez une convocation judiciaire révélant de lourdes dettes et un divorce difficile.")
                st.info("🔎 Déduction : Mehdi est ruiné financièrement. Un mobile parfait pour vendre ORION.")
            else:
                st.error("Cadenas bloqué.")

    st.markdown("---")
    if st.button("Poursuivre vers le verdict final"):
        st.session_state.step = 4
        st.rerun()

# ==========================================
# ÉTAPE 4 : Verdict Final
# ==========================================
elif st.session_state.step == 4:
    st.header("Étape Finale : Le Verdict")
    st.write("Toutes les preuves ont été récoltées. Qui a vendu le projet ORION à DataSphere ?")
    
    coupable = st.selectbox("Désignez le traître :", ["-- Choisissez --", "Sarah Benali", "Yassine Gharbi", "Mehdi Trabelsi", "Lina Kacem"])
    
    if st.button("Accuser"):
        if coupable == "Mehdi Trabelsi":
            st.balloons()
            st.success("🎉 GAGNÉ ! Mehdi Trabelsi, submergé par ses dettes, a utilisé les accès de Yassine pour voler ORION et revendre les plans à DataSphere.")
        elif coupable != "-- Choisissez --":
            st.error("❌ Mauvaise déduction ! Vous accusez un innocent ou tombez dans le panneau. Revoyez vos indices !")
