#2

Capitals = dict()
Capitals['Ukraine'] = 'Kyiv'
Capitals['Canada'] = 'Toronto'
Capitals['USA'] = 'Washington'

Countries = ['Germany', 'USA', 'Ukraine']

for country in Countries:
    if country in Capitals:
        print(f'{Capitals[country]} is a capital of {country}')
