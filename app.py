import streamlit as st

def main():
    st.title("Esempio Streamlit")

    st.header("Introduzione")
    st.write("Questo è un esempio base di Streamlit.")

    # Input di testo
    user_input = st.text_input("Inserisci un testo:", "Streamlit")

    # Checkbox
    show_text = st.checkbox("Mostra testo")

    if show_text:
        st.write(f"Hai inserito: {user_input}")

    # Selettore radio
    option = st.radio("Scegli un numero:", [1, 2, 3])

    st.write(f"Hai selezionato: {option}")

    # Slider
    slider_value = st.slider("Scegli un valore:", 0, 100, 25)

    st.write(f"Valore selezionato dallo slider: {slider_value}")

    # Selectbox
    option_selectbox = st.selectbox("Scegli una frutta:", ["Mela", "Banana", "Arancia"])
    st.write(f"Hai selezionato: {option_selectbox}")

    # Caricamento file
    uploaded_file = st.file_uploader("Carica un file:", type=["txt", "csv", "png", "jpg"])

    if uploaded_file is not None:
        st.write("File caricato con successo!")

if __name__ == "__main__":
    main()
