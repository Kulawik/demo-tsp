import matplotlib.pyplot as plt

from tspsolver.path import Path


class PathPlotter:
    """ Path plotting wrapper
    """

    def plot(self, path: Path):
        """Plots path"""
        vertices = path.get_vertices()
        if len(vertices) > 1:
            vertices.append(vertices[0])
        x, y = zip(*vertices)
        plt.plot(x, y)

    def show(self):
        """Shows plot"""
        plt.show()
