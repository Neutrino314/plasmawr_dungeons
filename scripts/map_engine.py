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

    def blocked(map_data, blocked_types, blocked):
        for i in range(0, len(map_data)):
            if map_data[i][0] in blocked_types:
                blocked.append([map_data[i][1] / 64, map_data[i][2] / 64])

        return blocked
