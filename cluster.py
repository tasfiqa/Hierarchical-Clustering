from typing import List
import math
from copy import deepcopy
from distance_functions import Distance_Functions

class Clustering:
  def clustering(self, X, K, distance_function):
    # Initialize - every point is its own clusters
    clusters = [[point] for point in X]
    while len(clusters) > K:
      cluster_size = len(clusters)

      # Initialize distance matrix - (cluster_size * cluster_size)
      cluster_dist_matrix = [[0.0] * cluster_size for _ in range(cluster_size)]

      # Distance between all clusters
      for i in range(cluster_size):
        for j in range(cluster_size): 
          point_distance_matrix = self.get_point_distance_matrix(clusters[i], clusters[j])
          cluster_dist_matrix[i][j] =  distance_function(
            point_distance_matrix,
            clusters[i],
            clusters[j]
            )
      
      # Join the two most similar clusters
      row_num, col_num = self.get_most_similar_clusters(cluster_dist_matrix)
      clusters[row_num].extend(deepcopy(clusters[col_num]))
      del clusters[col_num]

    return clusters

  def get_most_similar_clusters(self, cluster_dist_matrix): 
    """ 
    Return the indices of the two most similar clusters.
    We have to filter out the values on the diagonal. 
    """
    # First pass to find the minimum value
    min_cluster_distance = min([
      min([val for val in row if val != math.inf and val != -math.inf and val != 0])
      for row in cluster_dist_matrix
    ])
    
    # Find indices
    row_num, col_num = None, None
    for i in range(len(cluster_dist_matrix)): 
      if min_cluster_distance in cluster_dist_matrix[i]:
        row_num, col_num = i, cluster_dist_matrix[i].index(min_cluster_distance)

    # The indices of the clusters to merge
    return row_num, col_num 

  def get_point_distance_matrix(self, cluster_i, cluster_j): 
    """ Get Euclidean distance between every pair of points. """
    dist_matrix = [[0.0] * len(cluster_j) for _ in range(len(cluster_i))]
    for i in range(len(cluster_i)): 
      for j in range(len(cluster_j)): 
          dist_matrix[i][j] = Distance_Functions.euclidean_distance(cluster_i[i], cluster_j[j])

    return dist_matrix
  
  def map_data_to_clusters(self, X: List[List[float]], clusters: List[List[float]]) -> List[int]: 
    return [
      i
      for dat in X
      for i, cluster in enumerate(clusters)
      if dat in cluster
    ]
  
  def hclus_single_link(self, X: List[List[float]], K: int) -> List[int]:
    """Single link hierarchical clustering"""
    clusters = self.clustering(X, K, Distance_Functions.single_link_distance)
    return clusters, self.map_data_to_clusters(X, clusters)
    
  def hclus_average_link(self, X: List[List[float]], K: int) -> List[int]:
    """Average link hierarchical clustering"""
    clusters = self.clustering(X, K, Distance_Functions.average_link_distance)
    return clusters, self.map_data_to_clusters(X, clusters)

  def hclus_complete_link(self, X: List[List[float]], K: int) -> List[int]:
    """Complete link hierarchical clustering"""
    clusters = self.clustering(X, K, Distance_Functions.complete_link_distance)
    return clusters, self.map_data_to_clusters(X, clusters)