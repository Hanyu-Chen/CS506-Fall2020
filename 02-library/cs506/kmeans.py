from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    x = 0;
    y = 0;
    for i in range(len(points)):
        x += points[i][0];
        y += points[i][1];
    return [x/len(points), y/len(points)];


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = 0;
    for i in range(len(assignments)):
        k = max(k, assignments[i]);

    points = [];
    for i in range(k+1):
        points.append([]);

    for i in range(len(assignments)):
        points[assignments[i]].append(dataset[i]);

    centers = [];
    for i in range(len(points)):
        centers.append(point_avg(points[i]));

    return centers;

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    res = 0
    for i in range(len(a)):
        res += (a[i]-b[i]) ** 2
    return res ** 0.5

def distance_squared(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i]-b[i]) ** 2
    return res

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    res = [];
    used = [];
    while (len(res) < k) :
        tmp = random.randint(0, len(dataset)-1);
        if (tmp not in used):
            used.append(tmp);
            res.append(dataset[tmp]);
    return res;

def cost_function(clustering):
    centers = {};
    distances = [0 for i in range(len(clustering))];
    for i in clustering:
        centers[i] = point_avg(clustering[i]);

    for i in clustering:
        for point in clustering[i]:
            distances[i] += distance_squared(point, centers[i]);

    res = 0;
    for i in range(len(distances)):
        distances[i] **= 0.5;
        res += distances[i];

    return res;


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    
    centers = [];
    tmp = random.randint(0, len(dataset)-1);
    centers.append(dataset[tmp]);
    for i in range(k-1):
        centers.append(findMinDistance(centers, dataset));
    return centers;
    # raise NotImplementedError()

def findMinDistance(centers, dataset):
    minVal = 2147483647;
    res = [];
    for i in range(len(centers)):
        for j in range(len(dataset)):
            if (dataset[j] not in centers):
                if minVal > distance(centers[i],dataset[j]):
                    res = dataset[j];
                    minVal = distance(centers[i],dataset[j]);
    return res;




def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)

# test = [[179,260],[298,317],[381,464],[387,459],[507,634],[243,291],[256,288]];
# generate_k_pp(test, 2);
