import streamlit as st

# Configuration de la page (doit être la première commande Streamlit)
st.set_page_config(page_title="Jeu de Piste - Club GI ENIT", page_icon="🏭", layout="centered")

def main():
    st.title("🧩 Jeu de Piste Interactif - Intégration")
    
    st.markdown("""
    Bienvenue dans cette aventure interactive ! Pour avancer et prouver votre esprit d'équipe, 
    vous allez devoir mobiliser vos connaissances en génie industriel et en recherche opérationnelle.
    """)

    # Initialisation de la progression du joueur dans la session (session_state)
    if 'etape' not in st.session_state:
        st.session_state.etape = 1

    # --- ÉTAPE 1 ---
    if st.session_state.etape == 1:
        st.header("Étape 1 : L'Optimisation du Transport")
        st.write("""
        L'usine partenaire fait face à un problème logistique. Vous avez un réseau de distribution avec 
        plusieurs nœuds, et vous devez trouver le coût minimal pour acheminer la matière première.
        """)
        
        reponse_1 = st.text_input("Entrez la valeur du coût optimal calculé :", key="rep1")

        if st.button("Valider la réponse", key="btn1"):
            # Remplace "42" par la solution exacte de ton énigme
            if reponse_1.strip() == "42": 
                st.success("Bonne réponse ! La logistique est sauvée.")
                st.session_state.etape = 2
                st.rerun()
            elif reponse_1 != "":
                st.error("Ce n'est pas le coût optimal. Vérifiez vos calculs et réessayez !")

    # --- ÉTAPE 2 ---
    elif st.session_state.etape == 2:
        st.header("Étape 2 : Le Défi de l'Ordonnancement")
        st.write("""
        Maintenant que le transport est assuré, vous devez ordonnancer 3 tâches (A, B et C) sur une seule machine 
        pour minimiser le retard maximal.
        """)
        
        reponse_2 = st.text_input("Entrez la séquence optimale (par exemple : A-B-C) :", key="rep2")

        if st.button("Valider la séquence", key="btn2"):
            # Remplace "B-A-C" par la séquence correcte
            if reponse_2.strip().upper() == "B-A-C":
                st.success("Excellent ! L'ordonnancement est parfait.")
                st.session_state.etape = 3
                st.rerun()
            elif reponse_2 != "":
                st.error("La séquence n'est pas optimale. Réessayez !")

    # --- ÉTAPE 3 (VICTOIRE) ---
    elif st.session_state.etape == 3:
        st.header("🏆 Félicitations !")
        st.write("Vous avez brillamment résolu toutes les énigmes de recherche opérationnelle.")
        st.balloons()
        
        if st.button("Recommencer le jeu", key="btn3"):
            st.session_state.etape = 1
            st.rerun()

if __name__ == "__main__":
    main()
