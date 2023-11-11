import streamlit as st
import folium
import streamlit_folium as st_folium
from streamlit_folium import folium_static
import plotly.express as px
import geopandas as gpd
from geopy import Nominatim
# Load the shapefile
gdf = gpd.read_file('EPSG900913.shp')
print(gdf.head())






st.set_page_config(page_title="Estuda SP", page_icon=":books:", layout="wide")
st.title("Estuda SP")

col1, col2 = st.columns([2,1])
with col1:
    st.subheader("Locais")
    col11, col12 = st.columns([1,1])
    with col11:
        st.markdown(
        """
        <div style="background-color: #BCCCEC; padding: 20px; border-radius: 10px;">
            <h3 style="color: #000000;">
                <a href="https://www.exemplo.com" target="_blank" style="color: inherit; text-decoration: underline;">
                    Biblioteca 1
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
                    Biblioteca 3
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
                    Biblioteca 2
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

    m = folium.Map(location=[-23.5505, -46.6333], zoom_start=13)
    for i in range(len(gdf)):
        try:
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode(gdf['eq_enderec'].iloc[i])

            latitude = location.latitude
            longitude = location.longitude

            # Create the follium map
            folium.Marker(location=[latitude, longitude], popup=gdf["eq_nome"][i]).add_to(m)
        except:
            pass

    # Exibe o mapa no Streamlit
    folium_static(m)


    