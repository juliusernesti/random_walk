# -*- coding: utf-8 -*-
""" Playground class for the random walk simulation """

from shapely.geometry import Polygon, Point


class Playground:
    """Defines a playground with obstacles for RandomWalkers"""
    def __init__(self, scaling: int = 1, x_max: int = 250, y_max: int = 250, seed: int = 0):
        """
        Create a new Playground

        :param scaling: scale factor for x and y
        :param x_max: x range
        :param y_max: y range
        :param seed: map seed
        """
        self.x_max = scaling * x_max
        self.y_max = scaling * y_max
        x_max = self.x_max
        y_max = self.y_max
        border_polygon = [
            (-x_max, -y_max),
            (-x_max, y_max),
            (x_max, y_max),
            (x_max, -y_max),
        ]
        holes = []
        if seed == 1:
            moon_lake = [
                (x_max/2.5, y_max/2.5),
                (x_max/2.5, -y_max/2.5),
                (0, -y_max/2),
                (0, -y_max/1.5),
                (x_max*2/3, -y_max/1.5),
                (x_max*3/4, 0),
                (x_max * 1 / 2, y_max * 5 / 6),
                (x_max/4, y_max*3/4),
                (x_max / 2.5, y_max / 2.5)
            ]
            holes.append(moon_lake)
        ''' In Development:
        elif seed == 2:
            outer_lake_border = [
                (0, y_max/10),
                (x_max/15, y_max/15),
                (x_max / 10, 0),
                (x_max / 15, -y_max / 15),
                (0, -y_max / 10),
                (-x_max / 15, -y_max / 15),
                (-x_max / 10, 0),
                (-x_max / 15, y_max / 15),
                (0, y_max/10)
            ]
            inner_lake_border = [
                (0, y_max/30),
                (x_max/25, y_max/25),
                (x_max/30, 0),
                (x_max/25, -y_max/25),
                (0, -y_max/30),
                (-x_max/25, -y_max/25),
                (-x_max/30, 0),
                (-x_max/25, y_max/25),
                (0, y_max/30)
            ]
            holes.append(outer_lake_border)
            holes.append(inner_lake_border)
        '''
        self.holes = holes
        self.shape = Polygon(border_polygon, holes)

    def is_position_in_playground(self, x_position: float, y_position: float) -> bool:
        """
        Check, whether the given walker position is valid on the playground

        :param x_position: walker position
        :param y_position: walker position
        :return: True for a valid position, else False
        """
        position = Point((x_position, y_position))
        return self.shape.contains(position)

    def get_line_segments(self) -> list:
        """
        Get all parts from the playground in order to print them with py plot

        :return: list of polygon border
        """
        result = []
        for hole in self.holes:
            poly = Polygon(hole)
            result.append(poly.exterior.xy)
        result.append(self.shape.exterior.xy)
        return result
