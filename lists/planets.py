planet_list = ["Mercury", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(['Uranus', 'Neptune'])

planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')

planet_list.append('Pluto')


rocky_planets = planet_list[0:4]

del(planet_list[8])

spacecraft_1 = ('Cassini', 'Saturn')
spacecraft_2 = ('Mars Surveyor Program', 'Mars')
spacecraft_3 = ('Wind', 'Earth')
spacecraft_4 = ('Ulysses', 'Jupiter')
spacecraft_5 = ('Hubble Space Telescope', 'Mars')
spacecraft_6 = ('Hubble Space Telescope', 'Neptune')
spacecraft_7 = ('Pathfinder', 'Mars')
spacecraft_8 = ('Mars 96', 'Mars')
spacecraft_9 = ('Galileo', 'Jupiter')
spacecraft_10 = ('Magellan', 'Venus')
spacecraft_11 = ('Voyager 2', 'Uranus')
spacecraft_12 = ('Voyager 2', 'Neptune')
spacecraft_13 = ('Voyager 1', 'Uranus')
spacecraft_14 = ('Voyager 1', 'Neptune')
spacecraft_15 = ('Voyager 1', 'Saturn')
spacecraft_16 = ('Voyager 1', 'Jupiter')
spacecraft_17 = ('Viking 2', 'Mars')
spacecraft_18 = ('Viking 1', 'Mars')
spacecraft_19 = ('Pioneer Venus', 'Venus')
spacecraft_20 = ('Venera 9', 'Venus')
spacecraft_21 = ('Venera 7', 'Venus')
spacecraft_22 = ('Mariner 10', 'Venus')
spacecraft_23 = ('Mariner 10', 'Mercury')
spacecraft_24 = ('Pioneer 10', 'Jupiter')
spacecraft_25 = ('Pioneer 11', 'Saturn')
spacecraft_26 = ('Mariner 9', 'Mars')
spacecraft_27 = ('Mariner 4', 'Mars')
spacecraft_28 = ('Mariner 3', 'Mars')
spacecraft_29 = ('Mariner 2', 'Venus')

t_list = [spacecraft_1, spacecraft_2, spacecraft_3, spacecraft_4, spacecraft_5, spacecraft_6, spacecraft_7, spacecraft_8, spacecraft_9, spacecraft_10, spacecraft_11, spacecraft_12, spacecraft_13, spacecraft_14, spacecraft_15, spacecraft_16, spacecraft_17, spacecraft_18, spacecraft_19, spacecraft_20, spacecraft_21, spacecraft_22, spacecraft_23, spacecraft_24, spacecraft_25, spacecraft_26, spacecraft_27, spacecraft_28, spacecraft_29]


def printing (biglist):
    for planet in biglist:
        print(f'Spacecrafts that have landed on {planet}:')
        for tupleItem in t_list:
            if tupleItem[1] == planet:
                print(tupleItem[0])
    return

printing(planet_list)