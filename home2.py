import streamlit as st
import folium
import streamlit_folium as st_folium
from streamlit_folium import folium_static
import plotly.express as px
import pandas as pd
from geopy import Nominatim
geolocator = Nominatim(user_agent="my_app")

bibliotecas_data = {
    'Biblioteca': ['Biblioteca Mario de Andrade', 'Biblioteca Villa-Lobos', 'Biblioteca Belmonte', 'Biblioteca Pública Alceu Amoroso Lima'],
    'Latitude': [-23.5474534, -23.5467546, -23.6506861, -23.5579659],
    'Longitude': [-46.6420769, -46.7298958, -46.7110663, -46.6825918],
    'Endereco': ['Rua Mario de Andrade, 123 - Centro', 'Av. Queirós Filho, 1150 - Vila Hamburguesa',"R. Paulo Eiró, 525 " ,'Av. Henrique Schaumann, 777 - Pinheiros'],
    'Horario': ['Seg-Sex: 8h-18h', 'Seg-Sex: 9h-17h', 'Seg-Sex: 10h-19h', 'Seg-Sab: 10h-18h'],
    'Wifi': [True, True, False, True],
    'CadeiraDeRodas': [True, False, True, False],
    'FoneDeOuvido': [False, True, True, False],
    'Site': ['https://www.prefeitura.sp.gov.br/cidade/secretarias/cultura/bma/','https://bvl.org.br','https://www.prefeitura.sp.gov.br/cidade/secretarias/cultura/bibliotecas/biblioteca_belmonte/','https://www.prefeitura.sp.gov.br/cidade/secretarias/cultura/bibliotecas/bibliotecas_bairro/bibliotecas_a_l/alceu/']
}

# Criar DataFrame
bibliotecas_df = pd.DataFrame(bibliotecas_data)

st.set_page_config(page_title="Estuda SP", page_icon=":books:", layout="wide")
st.title("Estuda SP")

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Locais")
    for i in range(len(bibliotecas_data['Biblioteca'])):
        st.markdown(
            f"""
            <div style="background-color: #BCCCEC; padding: 20px; border-radius: 10px; margin-top: 20px">
                <h3 style="color: #000000;">
                    <a href={bibliotecas_data['Site'][i]} target="_blank" style="color: inherit; text-decoration: underline;">
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
with col2:
    st.subheader("Mapa")

    endereco_input = st.text_input("Digite um endereço:", placeholder="Rua endereço, 123 - Bairro")
    if endereco_input:
        location = geolocator.geocode(endereco_input)
        lat = location.latitude
        lon = location.longitude
    else:
        lat = -23.5505
        lon = -46.6333

    # Adiciona um mapa com a biblioteca Folium
    m = folium.Map(location=[lat,lon], zoom_start=15, width=500)
    for i in range(len(bibliotecas_data['Biblioteca'])):
        popup_text = f"{bibliotecas_data['Biblioteca'][i]}\n{bibliotecas_data['Endereco'][i]}\n{bibliotecas_data['Horario'][i]}"
        if bibliotecas_data['Wifi'][i]:
            popup_text += "\nWi-Fi disponível"
        if bibliotecas_data['CadeiraDeRodas'][i]:
            popup_text += "\nCadeira de rodas disponível"
        if bibliotecas_data['FoneDeOuvido'][i]:
            popup_text += "\nFone de ouvido disponível"

        folium.Marker(
            location=[bibliotecas_data['Latitude'][i], bibliotecas_data['Longitude'][i]],
            popup=popup_text,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # Exibe o mapa no Streamlit
    folium_static(m)

