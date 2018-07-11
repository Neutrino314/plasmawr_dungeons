class map_engine:

    def load_map(file):
        file = open(file, "r")
        data = file.readline()

        map_data = data.split("|")
        del map_data[(len(map_data) - 1)]

        for tile in map_data:
            map_data[map_data.index(tile)] = tile.split(",")

        for tile in map_data:
            tile[1] = int(tile[1])
            tile[2] = int(tile[2])
            map_data[map_data.index(tile)] = tile

        return map_data
