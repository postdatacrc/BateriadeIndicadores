import subprocess
import sys
import pip
import streamlit.components.v1 as components
import streamlit as st
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
if __name__ == '__main__':
    install('streamlit_folium')

import streamlit as st
from streamlit_folium import folium_static
import folium

# center on Liberty Bell
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

# add marker for Liberty Bell
tooltip = "Liberty Bell"
folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)
    
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
st.plotly_chart(fig)
    
HtmlFile = open("Grafica5TigoETB.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code,height=600,width=1000)

from urllib.request import urlopen
import json

resource_idvozmovilAB = '3a9c0304-3795-4c55-a78e-079362373b4d'

url_envios_vozmovilAB = 'https://www.postdata.gov.co/api/action/datastore/search.json?resource_id=' + resource_idvozmovilAB + '' \
                       '&fields[]=anno&fields[]=trimestre&fields[]=modalidad'\
                       '&group_by=anno,trimestre,modalidad'\
                       '&sum=abonados' 

responsevozmovilAB = urlopen(url_envios_vozmovilAB + '&limit=10000') # Se obtiene solo un registro para obtener el total de registros en la respuesta
json_envios_vozmovilAB = json.loads(responsevozmovilAB.read())
Total_registrosvozmovilAB = json_envios_vozmovilAB['result']['total']
ResponsevozmovilAB = urlopen(url_envios_vozmovilAB + '&limit=' + str(Total_registrosvozmovilAB))
Abonados_vozmovilAB = json.loads(ResponsevozmovilAB.read())
# Extracción de registros del json
vozmovilAB = pd.DataFrame(Abonados_vozmovilAB['result']['records'])

st.write(vozmovilAB)
