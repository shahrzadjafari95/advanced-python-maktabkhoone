# get numbers of user and return number:int
def get_person():
    number_of_person = int(input())
    return number_of_person


def person_information_genre(numbers: int):  # input number of people that we get from get_person()
    # define all genre in dictionary
    all_genres = {'Horror': 0, 'Romance': 0, 'Comedy': 0, 'History': 0, 'Adventure': 0, 'Action': 0}
    for i in range(numbers):  # loop in range of numbers
        genres = list(map(str, input('').split(' ')))  # get name and 3 genres
        if len(genres) == 4:
            for genre in genres[1:]:
                if genre == 'Horror':
                    all_genres['Horror'] += 1
                elif genre == 'Romance':
                    all_genres['Romance'] += 1
                elif genre == 'Comedy':
                    all_genres['Comedy'] += 1
                elif genre == 'History':
                    all_genres['History'] += 1
                elif genre == 'Adventure':
                    all_genres['Adventure'] += 1
                elif genre == 'Action':
                    all_genres['Action'] += 1
                else:
                    print('enter genre according all genre list')
                    break
    all_genres = dict(sorted(all_genres.items(), key=lambda item: item[0]))  # sorted by key according alphabet
    all_genres = dict(sorted(all_genres.items(), key=lambda item: item[1], reverse=True))  # sorted by value by decreasing
    for key, value in all_genres.items():  # output is vertically
        print(f"{key}: {value}")


number_of_persons = get_person()
person_information_genre(number_of_persons)
