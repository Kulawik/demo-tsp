import matplotlib.pyplot as plt

from tspsolver.path import Path


class PathPlotter:
    """ Path plotting wrapper
    """

    def plot(path: Path):
        """Plots path"""
        vertices = path.get_vertices()
        if len(vertices) > 1:
            vertices.append(vertices[0])
        plt.plot(vertices, style="o-")

    def show():
        """Shows plot"""
        plt.show()
