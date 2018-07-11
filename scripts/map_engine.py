class map_engine:

    def load_map(file):
        file = open(file, "r")
        data = file.readline()

        map_data = data.split("|")
        del map_data[(len(map_data) - 1)]

        for i in range(0, len(map_data)):
            map_data[i] = map_data[i].split(",")
            for j in range(1, 3):
                map_data[i][j] = int(map_data[i][j])

        return map_data
