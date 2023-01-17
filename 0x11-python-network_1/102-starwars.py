#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://swapi.co/api/people', params={'search': argv[1]})
    people = r.json()
    print("Number of results: {}".format(people.get('count')))
    for person in people.get('results'):
        print(person.get('name'))
        films = person.get('films')
        for film in films:
            r = requests.get(film)
            film = r.json()
            print("\t{}".format(film.get('title')))
    next_page = people.get('next')
    while next_page is not None:
        r = requests.get(next_page)
        people = r.json()
        for person in people.get('results'):
            print(person.get('name'))
            films = person.get('films')
            for film in films:
                r = requests.get(film)
                film = r.json()
                print("\t{}".format(film.get('title')))
        next_page = people.get('next')
