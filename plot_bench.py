from bench import _points1, _points2, _points3, _points4, _points5, _points6

import matplotlib.pyplot as plt

def plot_points(func):
    points = func(1000)
    plt.scatter([p.x for p in points], [p.y for p in points])
    plt.show()

plot_points(_points1)
plot_points(_points2)
plot_points(_points3)
plot_points(_points4)
plot_points(_points5)
plot_points(_points6)
