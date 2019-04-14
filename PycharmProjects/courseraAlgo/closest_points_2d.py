list_of_points = [(1, 3), (5, 4), (2, 1), (3, 3)]

points_sorted_by_x_cord = sorted(list_of_points, key=lambda x: x[0])
points_sorted_by_y_cord = sorted(list_of_points, key=lambda y: y[1])
print(points_sorted_by_x_cord)
print(points_sorted_by_y_cord)


def get_distance(list_of_points):
    p1 = list_of_points[0]
    p2 = list_of_points[1]
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def get_closest_split_points(p_x, p_y, delta):
    mid = len(p_x) // 2
    split_line = p_x[mid]
    left_boundary = split_line[0] - delta
    right_boundary = split_line[0] + delta
    # form S_y based on splits p_y wher x is within split_line + delta
    best_distance = delta
    best_points = None
    for i in range(len(p_y) - 1):
        for j in range(1, 8):
            if p_y[i][0] > left_boundary and p_y[i][0] < right_boundary:
                p = p_y[i]
            if i + j < len(p_x):
                if p_y[i + j][0] > left_boundary and p_y[i + j][0] < right_boundary:
                    q = p_y[i + j]
                    dist = get_distance([p, q])
                    if dist < best_distance:
                        best_distance = dist
                        best_points = [p, q]
    print(best_distance, best_points)
    return best_points


# start the recursion (based on x , sort on left , sort on right, count split-inversions)
# at the start of the recursion of each array , we have the arrays sorted in x as well as y
# here we are interested in pair of points :
def get_closest_points(p_x, p_y):
    print(p_x[:], p_y[:])
    if len(p_x) == 2:
        return p_x
    else:
        points_sorted_by_x_cord = sorted(p_x, key=lambda x: x[0])
        points_sorted_by_y_cord = sorted(p_x, key=lambda y: y[1])
        mid = len(list_of_points) // 2
        q_x = points_sorted_by_x_cord[:mid]
        q_y = points_sorted_by_y_cord[:mid]
        r_x = points_sorted_by_x_cord[mid:]
        r_y = points_sorted_by_y_cord[mid:]

        left_closest_points = get_closest_points(q_x, q_y)
        print(left_closest_points, "left closest points")
        right_closest_points = get_closest_points(r_x, r_y)
        delta = min(get_distance(left_closest_points), get_distance(right_closest_points))
        split_closest_points = get_closest_split_points(p_x, p_y, delta)
        return split_closest_points


p_x = sorted(list_of_points, key=lambda x: x[0])
p_y = sorted(list_of_points, key=lambda y: y[1])
get_closest_points(p_x, p_y)






