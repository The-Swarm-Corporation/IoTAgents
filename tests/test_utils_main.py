from iotagents.main import (
    map_to_pandas,
    map_to_json,
    map_to_csv,
    map_to_text,
    map_to_sql,
    map_to_xml,
    map_to_markdown,
    map_to_graph,
    map_to_heatmap_data,
)
import pandas
import matplotlib

iot_data = [
    {
        "Device ID": "001",
        "Device Type": "Temperature",
        "Data Type": "Temperature",
        "Timestamp": "2024-08-23 10:00:00",
        "Location": "Warehouse A",
        "Sensor Reading": 22.5,
        "Unit": "°C",
        "Status": "Active",
        "Description": "Temperature inside Warehouse A",
    },
    {
        "Device ID": "002",
        "Device Type": "Humidity",
        "Data Type": "Humidity",
        "Timestamp": "2024-08-23 10:01:00",
        "Location": "Warehouse B",
        "Sensor Reading": 55.3,
        "Unit": "%",
        "Status": "Active",
        "Description": "Humidity level inside Warehouse B",
    },
]


def test_map_to_pandas():
    result = map_to_pandas(iot_data)
    assert callable(map_to_pandas)
    assert isinstance(result, pandas.DataFrame)


def test_map_to_json():
    result = map_to_json(iot_data)
    assert callable(map_to_json)
    assert isinstance(result, str)


def test_map_to_csv():
    result = map_to_csv(iot_data)
    assert callable(map_to_csv)
    assert isinstance(result, str)


def test_map_to_text():
    result = map_to_text(iot_data)
    assert callable(map_to_text)
    assert isinstance(result, str)


def test_map_to_sql():
    result = map_to_sql(iot_data)
    assert callable(map_to_sql)
    assert isinstance(result, str)


def test_map_to_xml():
    result = map_to_xml(iot_data)
    assert callable(map_to_xml)
    assert isinstance(result, str)


def test_map_to_markdown():
    result = map_to_markdown(iot_data)
    assert callable(map_to_markdown)
    assert isinstance(result, str)


def test_map_to_graph():
    result = map_to_graph(iot_data)
    assert callable(map_to_graph)
    assert isinstance(result, matplotlib.figure.Figure)


def test_map_to_heatmap_data():
    result = map_to_heatmap_data(iot_data)
    assert callable(map_to_heatmap_data)
    assert isinstance(result, matplotlib.figure.Figure)


# Run the tests
# $ pytest tests/test_main.py
# ============================= test session starts ==============================
