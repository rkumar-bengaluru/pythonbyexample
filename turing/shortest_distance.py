class ShortestDistance:

    def find_manhatten_distance(self, x, y, locations):
        distance_index_tuple = []
        for current_index, point in enumerate(locations):
            # point is valid if it shares the same x or y coordinates
            if x == point[0] or y == point[1]:
                distance = abs(point[0] - x) + abs(point[1] - y)
                distance_index_tuple.append((distance, current_index))
        # short distance index array and return the first distance index
        distance_index_tuple = sorted(distance_index_tuple)
        if len(distance_index_tuple) == 0:
            return -1
        return distance_index_tuple[0][1]
