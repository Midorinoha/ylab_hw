class TV():
    def create_news(hero, place):
        place_name = getattr(place, 'name', 'place')
        place_planet = getattr(place, 'planet', 'place')
        print(f'Live! {hero.name} saved the {place_name}! Planet [{place_planet[0]}, {place_planet[1]}] saved!')
