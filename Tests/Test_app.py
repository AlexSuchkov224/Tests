import folium
import pytest
import sys
sys.path.append('C:/Users/Александр/Desktop/Python/app')

#Тест проверяет различные аспекты карты, такие как её местоположение по умолчанию, масштаб и плитки, а так же присутсвует ли маркер в указаном месте.
def test_map_creater():
  def map_creater():
    default_location = (57.70414723434193, -108.28125000000001)
    default_zoom_level = 3
    default_tiles = "openstreetmap"
    marker_location = (50, 50)

    #Создает карту со стандартным местоположением и масштабом.
    map_1 = map_creater(None)
    assert map_1.get_root().find_all('div', {'class': 'leaflet-top leaflet-left'})[0]['style']['left'] == f'{default_location[1]}px'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-top leaflet-right'})[0]['style']['left'] == f'{default_location[0]}px'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-bottom leaflet-left'})[0]['style']['left'] == f'{default_location[1]}px'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-bottom leaflet-right'})[0]['style']['left'] == f'{default_location[0]}px'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-map-pane'})[0]['style']['transform'] == f'translate({default_location[1]}px, {default_location[0]}px)'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-control-container'})[0]['style']['left'] == '0px'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-control-container'})[0]['style']['top'] == '0px'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-control-container'})[0]['style']['transform'] == 'translate(0px, 0px)'
    assert map_1.get_root().find_all('div', {'class': 'leaflet-control-scale'})[0]['style']['left'] == '50%'

    #Создает карту со стандартным местоположением, масштабом и плитками.
    map_2 = map_creater(None, default_tiles=None)
    assert map_2.get_root().find_all('div', {'class': 'leaflet-tile-pane'})[0]['style']['transform'] == 'translate(0px, 0px)'
    assert map_2.get_root().find_all('img', {'class': 'leaflet-tile'})[0]['src'].endswith('tile.openstreetmap.org')

    #Создает карту с маркером в опреленном месте.
    map_3 = map_creater(marker_location)
    marker_element = map_3.get_root().find_all('div', {'class': 'leaflet-marker-icon leaflet-zoom-animated'})[0]
    assert marker_element['style']['left'] == f'{marker_location[1]}px'
    assert marker_element['style']['top'] == f'{marker_location[0]}px'

    #Создает карту с маркером в опреленном месте и стандартными плитками.
    map_4 = map_creater(marker_location, default_tiles=None)
    marker_element = map_4.get_root().find_all('div', {'class': 'leaflet-marker-icon leaflet-zoom-animated'})[0]
    assert marker_element['style']['left'] == f'{marker_location[1]}px'
    assert marker_element['style']['top'] == f'{marker_location[0]}px'
    assert map_4.get_root().find_all('img', {'class': 'leaflet-tile'})[0]['src'].endswith('tile.stamen.com')
