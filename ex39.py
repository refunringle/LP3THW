

country_names={
    'ind' : 'india',
    'nz' : 'newsland',
    'sz' : 'sewzerland',
    'uk' : 'unated kingdome'
}

city={
    'india' : 'tamilnadu',
    'unated kingdome' : 'parice',
    'newsland' : 'new delhi',
    'ln' : 'london'
}
city['kr'] = 'kerale'
print(city.values())
print(city[country_names['ind']])
for city,i in list(city.items()):
    print(f" {city} has the city {i}")

cit=city.get('india')
if not cit:
    print(f"{cit} is not found")




