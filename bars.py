import json

from geopy import distance


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def get_biggest_bar(data):
    biggest_bar = ''
    biggest_seats_count = 1
    for bar in data['features']:
        if bar['properties']['Attributes']['SeatsCount'] > biggest_seats_count:
            biggest_seats_count = bar['properties']['Attributes']['SeatsCount']
            biggest_bar = bar['properties']['Attributes']['Name']
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = ''
    smallest_seats_count = 100000
    for bar in data['features']:
        if bar['properties']['Attributes']['SeatsCount'] < smallest_seats_count:
            smallest_seats_count = bar['properties']['Attributes']['SeatsCount']
            smallest_bar = bar['properties']['Attributes']['Name']
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    my_coords = (longitude, latitude)
    min_spacing = 1000000000
    closet_bar = ''
    for bar in data['features']:
        spacing = distance.distance(my_coords, bar['geometry']['coordinates']).km
        if spacing < min_spacing:
            min_spacing = spacing
            closet_bar = bar['properties']['Attributes']['Name']
    return closet_bar
        


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
