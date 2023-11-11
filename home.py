import streamlit as st
import folium
import streamlit_folium as st_folium
from streamlit_folium import folium_static
import plotly.express as px


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

    # st.markdown(
    #     """
    #     <style>
    #         input[type="text"] {
    #             color: #808080;
    #         }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # Adiciona um mapa com a biblioteca Folium
    m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
    folium.Marker([-23.5505, -46.6333], popup="Local 1").add_to(m)

    # Exibe o mapa no Streamlit
    folium_static(m)

    # fig = px.scatter_mapbox(
    #     lat=[-23.5505],
    #     lon=[-46.6333],
    #     zoom=12,
    #     height=500,
    # )

    # fig.update_layout(
    #     mapbox_style="open-street-map",
    #     margin=dict(r=150, t=0, b=0, l=0),
    # )

    # st.plotly_chart(fig)
    