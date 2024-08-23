from typing import List, Dict, Union, Any
import pandas as pd
import json
import csv
from io import StringIO
import xml.etree.ElementTree as ET


def map_to_pandas(
    data: List[Dict[str, Union[str, float, int]]],
) -> str:
    """
    Maps IoT data to a Pandas DataFrame and returns it as a string.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: String representation of the Pandas DataFrame.
    """
    df = pd.DataFrame(data)
    return df.to_string()


def map_to_json(data: List[Dict[str, Any]]) -> str:
    """
    Maps IoT data to a JSON string.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: JSON string representation of the IoT data.
    """
    return json.dumps(data, indent=2)


def map_to_csv(data: List[Dict[str, Union[str, float, int]]]) -> str:
    """
    Maps IoT data to a CSV string.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: CSV string representation of the IoT data.
    """
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def map_to_text(data: List[Dict[str, Union[str, float, int]]]) -> str:
    """
    Maps IoT data to a plain text summary string.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: Plain text summary of the IoT data.
    """
    lines = []
    for entry in data:
        line = f"Device {entry['Device ID']} ({entry['Device Type']}) recorded {entry['Data Type']} of {entry['Sensor Reading']} {entry['Unit']} at {entry['Location']} on {entry['Timestamp']}. Status: {entry['Status']}."
        lines.append(line)
    return "\n".join(lines)


def map_to_sql(data: List[Dict[str, Union[str, float, int]]]) -> str:
    """
    Maps IoT data to a SQL INSERT statement.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: SQL INSERT statement string.
    """
    columns = ", ".join(data[0].keys())
    values = ", ".join([str(tuple(entry.values())) for entry in data])
    return f"INSERT INTO IoT_data ({columns}) VALUES {values};"


def map_to_xml(data: List[Dict[str, Union[str, float, int]]]) -> str:
    """
    Maps IoT data to an XML string.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: XML string representation of the IoT data.
    """
    root = ET.Element("IoTData")
    for entry in data:
        device = ET.SubElement(root, "Device")
        for key, value in entry.items():
            elem = ET.SubElement(device, key.replace(" ", ""))
            elem.text = str(value)
    return ET.tostring(root, encoding="unicode")


def map_to_markdown(
    data: List[Dict[str, Union[str, float, int]]],
) -> str:
    """
    Maps IoT data to a Markdown string.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: Markdown string representation of the IoT data.
    """
    lines = [
        "| " + " | ".join(data[0].keys()) + " |",
        "| " + " | ".join(["---"] * len(data[0])) + " |",
    ]
    for entry in data:
        lines.append(
            "| "
            + " | ".join(str(value) for value in entry.values())
            + " |"
        )
    return "\n".join(lines)


def map_to_graph(
    data: List[Dict[str, Union[str, float, int]]],
) -> str:
    """
    Maps IoT data to a graph description string (node-edge).

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: Node-edge representation of the IoT data.
    """
    lines = []
    for entry in data:
        lines.append(
            f"Device {entry['Device ID']} -> {entry['Device Type']}: {entry['Data Type']} at {entry['Location']}"
        )
    return "\n".join(lines)


def map_to_heatmap_data(
    data: List[Dict[str, Union[str, float, int]]],
) -> str:
    """
    Prepares IoT data for heatmap visualization by representing it in a suitable format.

    Args:
        data (List[Dict[str, Union[str, float, int]]]): List of IoT data dictionaries.

    Returns:
        str: Heatmap-compatible data string.
    """
    heatmap_data = {}
    for entry in data:
        location = entry["Location"]
        if location not in heatmap_data:
            heatmap_data[location] = {}
        heatmap_data[location][entry["Data Type"]] = entry[
            "Sensor Reading"
        ]
    return json.dumps(heatmap_data, indent=2)


# iot_data = [
#     {
#         "Device ID": "001",
#         "Device Type": "Temperature",
#         "Data Type": "Temperature",
#         "Timestamp": "2024-08-23 10:00:00",
#         "Location": "Warehouse A",
#         "Sensor Reading": 22.5,
#         "Unit": "°C",
#         "Status": "Active",
#         "Description": "Temperature inside Warehouse A",
#     },
#     {
#         "Device ID": "002",
#         "Device Type": "Humidity",
#         "Data Type": "Humidity",
#         "Timestamp": "2024-08-23 10:01:00",
#         "Location": "Warehouse B",
#         "Sensor Reading": 55.3,
#         "Unit": "%",
#         "Status": "Active",
#         "Description": "Humidity level inside Warehouse B",
#     },
# ]

# # Examples of calling the functions
# print(map_to_pandas(iot_data))
# print(map_to_json(iot_data))
# print(map_to_csv(iot_data))
# print(map_to_text(iot_data))
# print(map_to_sql(iot_data))
# print(map_to_xml(iot_data))
# print(map_to_markdown(iot_data))
# print(map_to_graph(iot_data))
# print(map_to_heatmap_data(iot_data))
