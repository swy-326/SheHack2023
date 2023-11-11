import streamlit as st
import folium
import streamlit_folium as st_folium
from streamlit_folium import folium_static
import plotly.express as px
import pandas as pd

# bibliotecas_data = {
#     'Biblioteca': ['Biblioteca Mario de Andrade', 'Biblioteca Villa-Lobos', 'Biblioteca Belmonte'],
#     'Latitude': [-23.5474534, -23.5467546, -23.6506861],
#     'Longitude': [-46.6420769, -46.7298958, -46.7110663]
# }

bibliotecas_data = {
    'Biblioteca': ['Biblioteca Mario de Andrade', 'Biblioteca Villa-Lobos', 'Biblioteca Belmonte'],
    'Latitude': [-23.5474534, -23.5467546, -23.6506861],
    'Longitude': [-46.6420769, -46.7298958, -46.7110663],
    'Endereco': ['Rua Mario de Andrade, 123 - Centro', 'Av. Queirós Filho, 1150 - Vila Hamburguesa', 'Av. Henrique Schaumann, 777 - Pinheiros'],
    'Horario': ['Seg-Sex: 8h-18h', 'Seg-Sex: 9h-17h', 'Seg-Sex: 10h-19h'],
    'Wifi': [True, True, False],
    'CadeiraDeRodas': [True, False, True],
    'FoneDeOuvido': [False, True, True]
}

# Criar DataFrame
bibliotecas_df = pd.DataFrame(bibliotecas_data)

st.set_page_config(page_title="Estuda SP", page_icon=":books:", layout="wide")
st.title("Estuda SP")

col1, col2 = st.columns([2,1])
with col1:
    st.subheader("Locais")
    col11, col12 = st.columns([1,1])
    with col11:
        for i in range(len(bibliotecas_data['Biblioteca'])):
            st.markdown(
                f"""
                <div style="background-color: #BCCCEC; padding: 20px; border-radius: 10px; margin-top: 20px">
                    <h3 style="color: #000000;">
                        <a href="https://www.exemplo.com" target="_blank" style="color: inherit; text-decoration: underline;">
                            {bibliotecas_data['Biblioteca'][i]}
                        </a>
                    </h3>
                    <p>{bibliotecas_data['Endereco'][i]}</p>
                    <p>{bibliotecas_data['Horario'][i]}</p>
                    <p>{'Wi-Fi disponível' if bibliotecas_data['Wifi'][i] else ''}</p>
                    <p>{'Cadeira de rodas disponível' if bibliotecas_data['CadeiraDeRodas'][i] else ''}</p>
                    <p>{'Fone de ouvido disponível' if bibliotecas_data['FoneDeOuvido'][i] else ''}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown(
        """
        <div style="background-color: #BCCCEC; padding: 20px; border-radius: 10px;">
            <h3 style="color: #000000;">
                <a href="https://www.exemplo.com" target="_blank" style="color: inherit; text-decoration: underline;">
                    Local 1
                </a>
            </h3>
            <p>Rua endereço, 123 - Bairro</p>
            <p>Seg à Sex - 9hrs à 18hrs</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
        st.markdown(
        """
        <div style="background-color: #BCCCEC; padding: 20px; border-radius: 10px; margin-top: 20px">
            <h3 style="color: #000000;">
                <a href="https://www.exemplo.com" target="_blank" style="color: inherit; text-decoration: underline;">
                    Local 3
                </a>
            </h3>
            <p>Rua endereço, 123 - Bairro</p>
            <p>Seg à Sex - 9hrs à 18hrs</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    with col12:  
        st.markdown(
        """
        <div style="background-color: #BCCCEC; padding: 20px; border-radius: 10px;">
            <h3 style="color: #000000;">
                <a href="https://www.exemplo.com" target="_blank" style="color: inherit; text-decoration: underline;">
                    Local 2
                </a>
            </h3>
            <p>Rua endereço, 123 - Bairro</p>
            <p>Seg à Sex - 9hrs à 18hrs</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.subheader("Mapa")

    st.text_input("Digite um endereço:", placeholder="Rua endereço, 123 - Bairro")


    # Adiciona um mapa com a biblioteca Folium
    m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
    for i in range(len(bibliotecas_data)):
        folium.Marker([bibliotecas_data['Latitude'][i], bibliotecas_data['Longitude'][i]], popup=bibliotecas_data['Biblioteca'][i]).add_to(m)
    # folium.Marker([-23.547408,-46.6421673], popup="Local 1").add_to(m)

    # Exibe o mapa no Streamlit
    folium_static(m)


    