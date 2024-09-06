"""
Test if points are in a given bounding polygon using shapely.

Zachary Katz
zachary_katz@mines.edu
September 2024

Functions
---------
inPolygon
    Return true if point is in polygon.
"""

import shapely.geometry


class BoundingPolygon:
    """Rectangular bounding box given by its four corners."""

    def __init__(self, box: list[tuple]) -> None:
        """Initialize a bounding polygon.

        Parameters
        ----------
        box : list[tuple]
            List of tuples representing the vertices of the polygon.
            The last vertex should be the same as the first.
        """
        assert box[0] == box[-1], "First and last vertices must be the same."
        self.box = shapely.geometry.Polygon(box)

    def inPolygon(self, points: list[tuple]) -> list[bool]:
        """Determine if points are in the bounding box.

        Parameters
        ----------
        points : list[tuple]
            List of tuples representing points to check.

        Returns
        -------
        list[bool]
            List of bools, true if point is in box.
        """
        return self.box.contains(shapely.geometry.Points(points))
