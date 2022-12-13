import networkx as nx
import pandas as pd

class KnowledgeGraph:

    graph = None
    dataset = ""
    prefix = ""
    df = None
    id = 0

    def __init__(self, id, dataset, prefix, kg_type, sample, conf_id):

      self.id = id
      self.dataset = dataset
      self.prefix = prefix
      self.sample = sample
      if sample == "original":
        path =  "../datasets/" + sample + "/" + dataset + prefix + "_RREA/rel_triples_" + id
      elif sample == "sampled":
        path =  "../datasets/sampled/" + dataset + "_sampled/" + conf_id + "/rel_triples_" + id
      kg = pd.read_csv(path,  sep='\t', names=["e1", "r", "e2"])

      # countig relation types
      # print(len(set(kg["r"])))
      
      self.df = kg
      self.df["(e1,e2)"] = list(zip(self.df.e1, self.df.e2))
      if kg_type == "directed":
        self.graph = nx.from_pandas_edgelist(kg, "e1", "e2", ["r"], create_using=nx.DiGraph())
      elif kg_type == "multi_directed":
        self.graph = nx.from_pandas_edgelist(kg, "e1", "e2", ["r"], create_using=nx.MultiDiGraph())
      elif kg_type == "multi_undirected":
        self.graph = nx.from_pandas_edgelist(kg, "e1", "e2", ["r"], create_using=nx.MultiGraph())
      elif kg_type == "undirected":
        # default nx.Graph
        self.graph = nx.from_pandas_edgelist(kg, "e1", "e2", ["r"])


    def get_seed_pairs(self, reverse=False):

      path = "../datasets/" + self.sample + "/"

      if reverse == False:
        pairs = {}
        path_test = path + self.dataset + self.prefix + "_RREA/721_5fold/2/test_links"
        with open(path_test) as fp:
          for line in fp:
            pairs[int(line.split("\t")[0])] = int(line.split("\t")[1].rstrip())

        path_train = path + self.dataset + self.prefix + "_RREA/721_5fold/2/train_links"
        with open(path_train) as fp:
          for line in fp:
            pairs[int(line.split("\t")[0])] = int(line.split("\t")[1].rstrip())

        path_valid = path + self.dataset + self.prefix + "_RREA/721_5fold/2/valid_links"
        with open(path_valid) as fp:
          for line in fp:
            pairs[int(line.split("\t")[0])] = int(line.split("\t")[1].rstrip())
      elif reverse == True:
          pairs = {}
          path_test = path + self.dataset + self.prefix + "_RREA/721_5fold/2/test_links"
          with open(path_test) as fp:
            for line in fp:
              pairs[int(line.split("\t")[1].rstrip())] = int(int(line.split("\t")[0]))

          path_train = path + self.dataset + self.prefix + "_RREA/721_5fold/2/train_links"
          with open(path_train) as fp:
            for line in fp:
              pairs[int(line.split("\t")[1].rstrip())] = int(line.split("\t")[0])

          path_valid = path + self.dataset + self.prefix + "_RREA/721_5fold/2/valid_links"
          with open(path_valid) as fp:
            for line in fp:
              pairs[int(line.split("\t")[1].rstrip())] = int(line.split("\t")[0])

      return pairs

    def create_sampled_graph(self, node_pairs):
      npairs = set()
      for pair in node_pairs:
          npairs.add((pair[0], pair[1]))
          npairs.add((pair[1], pair[0]))
      self.df["(e1,e2)"] = list(zip(self.df.e1, self.df.e2))
      self.df = self.df[self.df["(e1,e2)"].apply(lambda pair: pair in npairs)]
      return nx.from_pandas_edgelist(self.df, "e1", "e2", ["r"]), self.df, nx.from_pandas_edgelist(self.df, "e1", "e2", ["r"], create_using=nx.DiGraph())
