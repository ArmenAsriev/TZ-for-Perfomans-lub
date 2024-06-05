import math
import sys


def read_circle(file_path):
    with open(file_path, 'r') as f:
        center_x, center_y, radius = map(float, f.read().split())
    return center_x, center_y, radius


def read_points(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(center_x, center_y, radius, points):
    results = []
    for x, y in points:
        distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        if distance < radius:
            results.append(1)
        elif distance > radius:
            results.append(2)
        else:
            results.append(0)
    return results


def main(circle_file, points_file):
    center_x, center_y, radius = read_circle(circle_file)
    points = read_points(points_file)
    results = point_position(center_x, center_y, radius, points)

    for result in results:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    main(circle_file, points_file)
