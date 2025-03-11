from statistics import mean
import math

class Distance_Functions:
    @staticmethod
    def average_link_distance(point_distance_matrix, cluster_i, cluster_j): 
        if cluster_i == cluster_j: 
            return 0
        
        return mean([
        mean(row)
        for row in point_distance_matrix
        ])
    
    @staticmethod
    def complete_link_distance(point_distance_matrix, cluster_i, cluster_j): 
        if cluster_i == cluster_j: 
            return -math.inf

        return max([
        max(row)
        for row in point_distance_matrix
        ])
    
    @staticmethod
    def single_link_distance(point_distance_matrix, cluster_i, cluster_j): 
        if cluster_i == cluster_j: 
            return math.inf

        return min([
        min(row)
        for row in point_distance_matrix
        ])
    
    @staticmethod
    def euclidean_distance(point_v, point_p):
        dims = len(point_v)
        return math.sqrt(sum(
        [
            (point_v[i] - point_p[i]) ** 2
            for i in range(dims)
        ]
        ))

    

