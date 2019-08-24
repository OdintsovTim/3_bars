import json

from geopy import distance


def load_data(filepath):
    with open(filepath, 'r') as file1:
        return json.load(file1)


def get_biggest_bar(bars_info):
    biggest_bar_info = max(
        bars_info['features'],
        key=lambda bars: bars['properties']['Attributes']['SeatsCount'])
    return biggest_bar_info


def get_smallest_bar(bars_info):
    smallest_bar_info = min(
        bars_info['features'],
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return smallest_bar_info


def get_closest_bar(bars_info, longitude, latitude):
    my_coords = (longitude, latitude)
    closet_bar_info = min(
        bars_info['features'],
        key=lambda bar: distance.distance(
            my_coords,
            bar['geometry']['coordinates']).km)
    return closet_bar_info


def main():
    while True:
        try:
            filepath = input('Введите путь до файла: ')
            bars_info = load_data(filepath)
            break
        except FileNotFoundError:
            print('Такой файл не найден')
        except json.decoder.JSONDecodeError:
            print('Это файл не формата json')
    while True:
        try:
            longitude = float(input('Введите вашу долготу: '))
            break
        except ValueError:
            print('Введите числовое значение')
    while True:
        try:
            latitude = float(input('Введите вашу широту: '))
            break
        except ValueError:
            print('Введите числовое значение')
    biggest_bar = get_biggest_bar(bars_info)
    biggest_bar_name = biggest_bar['properties']['Attributes']['Name']
    smallest_bar = get_smallest_bar(bars_info)
    smallest_bar_name = smallest_bar['properties']['Attributes']['Name']
    closet_bar = get_closest_bar(bars_info, longitude, latitude)
    closet_bar_name = closet_bar['properties']['Attributes']['Name']
    print('Самый большой бар:', biggest_bar_name)
    print('Самый маленький бар:', smallest_bar_name)
    print('Самый близкий бар:', closet_bar_name)


if __name__ == '__main__':
    main()
