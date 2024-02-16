def get_person():
    number_of_persons = int(input('enter number of member:'))
    return number_of_persons


def get_olympic_members(number: int):
    list_of_member = []
    print('enter your gender, namae and language programming')
    for i in range(number):
        # separate user input according '.' and put to the list
        information_member = list(map(str, input().split('.')))
        list_of_member.append(information_member)  # each information_list input append to list_of_members
    for member in list_of_member:
        member[1] = member[1].capitalize()  # capitalize second item in each nested list
    list_of_member.sort(key=lambda x: (x[0], x[1]))  # sorted according first and second item in list
    return list_of_member


numbers = get_person()
all_member = get_olympic_members(numbers)
# print(" ".join(str(item) for item in user))
for user in all_member:
    print(f'{user[0]} {user[1]} {user[2]}')

