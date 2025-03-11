from cluster import Clustering

def read_input_file(file_path): 
  with open(file_path, 'r') as f: 
    raw_data = f.read()
  # Get all but first line
  data = raw_data.split("\n")[1:]
  data = [
    [float(lat), float(lon)]
    for dat in data
    if (split_data := dat.split()) and
      (lat := split_data[0]) and 
      (lon := split_data[1])
  ]
  return data


if __name__ == "__main__": 
  single_link_data = read_input_file("sample_test_cases/input00.txt")
  complete_link_data = read_input_file("sample_test_cases/input01.txt")
  average_link_data = read_input_file("sample_test_cases/input02.txt")
  
  clustering = Clustering()
  single_link_clusters_mapping = clustering.hclus_single_link(X=single_link_data, K=2)
  print(single_link_clusters_mapping)
 
  complete_link_clusters_mapping = clustering.hclus_complete_link(X=complete_link_data, K=2)
  print(complete_link_clusters_mapping)

  average_link_clusters_mapping = clustering.hclus_average_link(X=average_link_data, K=2)
  print(average_link_clusters_mapping)