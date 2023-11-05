from typing import List

class ShortestDistance:

    def find_manhatten_distance(self, x: int, y: int, locations: List[int]) -> int:
        """
        Given your current position on cartesian plane represented by integers x and y, along with an array
        called locations where each element locations[i] = x[i], y[i] signifies the presence of a point
        at co-ordinates. We need to find the index of the valid point that is closest to your present location
        according to manhatten distance.

        A point is considered valid if it shares same x or y co-ordinate as your current position. If there are 
        multiple valid points with the same distance then return the valid point with the smallest index. If no
        valid points are found then return -1

        Args:
            x (int): current position on x co-ordinate
            y (int): current position on y co-ordinate
            locations (List[int]): locations on the map.
        
        Retuns:
            int: index in the locations which is closest to your location
        """
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
