import requests
import xml.etree.ElementTree as ET

url = 'https://apigw.tmoney.co.kr:5556/gateway/saStationByArsIdGet/v1/stationinfo/getStationByUidCon'

def get_station_info(ars_id, bus_route_type = '1'):
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'x-Gateway-APIKey': 'b6b3763f-c016-45e3-8d66-3e53632c5757'
    }

    params = {
        'serviceKey': '01234567890',
        'arsId': '22394',
        'busRouteType': 1
    }

    response = requests.get(url, headers=headers, params=params)
    return response

def get_response(station_id, bus_route_type):
    
    response = get_station_info(station_id, bus_route_type)

    print(f"Status Code: {response.status_code}")

    def xml_to_dict(element):
        result = {}
        for child in element:
            if len(child) > 0: 
                result[child.tag] = xml_to_dict(child)
            else:  
                result[child.tag] = child.text
        return result

    try:
        root = ET.fromstring(response.text)  
        response_dict = xml_to_dict(root) 
        print("Response as Dictionary:")
        print(response_dict)
    except ET.ParseError:
        print("Error: Response is not in valid XML format.")

get_response('01126', '2')