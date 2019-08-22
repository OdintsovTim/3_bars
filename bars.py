import json

from geopy import distance


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def get_biggest_bar(bars_info):
    biggest_bar_info = max(bars_info['features'], 
                    key=lambda bars: bars['properties']['Attributes']['SeatsCount'])
    biggest_bar_name = biggest_bar_info['properties']['Attributes']['Name']
    return biggest_bar_name


def get_smallest_bar(bars_info):
    smallest_bar_info = min(bars_info['features'], 
                    key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    smallest_bar_name = smallest_bar_info['properties']['Attributes']['Name']
    return smallest_bar_name


def get_closest_bar(bars_info, longitude, latitude):
    my_coords = (longitude, latitude)
    closet_bar_info = min(bars_info['features'],
                        key=lambda bar: distance.distance(my_coords, 
                                                    bar['geometry']['coordinates']).km)
    closet_bar_name = closet_bar_info['properties']['Attributes']['Name']
    return closet_bar_name
        


def main():
    longitude = float(input('Введите вашу долготу: '))
    latitude = float(input('Введите вашу широту: '))
    bars_info = load_data('bars.json')
    biggest_bar = get_biggest_bar(bars_info)
    smallest_bar = get_smallest_bar(bars_info)
    closet_bar = get_closest_bar(bars_info, longitude, latitude)
    print('Самый большой бар:', biggest_bar)
    print('Самый маленький бар:', smallest_bar)
    print('Самый близкий бар:', closet_bar)


if __name__ == '__main__':
    main()
