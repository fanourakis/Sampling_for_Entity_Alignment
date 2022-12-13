from lib2to3.pytree import Node
from KG.KnowledgeGraph import *
import numpy as np
import networkx as nx
import pandas as pd
import pickle
import statistics as st
from scipy.stats import skew
from itertools import combinations

class Statistics:

    def weakly_conn_comps( measure, sample, dataset, prefix, num_kg, mode):
        print("wcc_" + "KG" + num_kg)
        wcc_dict = dict()
        kg_mdi = KnowledgeGraph(num_kg, dataset, prefix, "multi_directed", "original", "")
        wcc_dict["original"] = nx.number_weakly_connected_components(kg_mdi.graph)/kg_mdi.graph.number_of_nodes()

        for i in range(0,5):
            conf_id = "conf_" + str(i) + "_only_p"
            kg_mdi = KnowledgeGraph(num_kg, dataset, prefix, "multi_directed", sample, conf_id)
            wcc_dict[conf_id] = nx.number_weakly_connected_components(kg_mdi.graph)/kg_mdi.graph.number_of_nodes()
        
        wcc_df = pd.DataFrame.from_dict(wcc_dict, orient='index').T

        wcc_df = wcc_df.rename(columns={
            'conf_0_only_p': '0 ',
            'conf_1_only_p': '0.15 ',
            'conf_2_only_p': '0.50 ',
            'conf_3_only_p': '0.85 ',
            'conf_4_only_p': '1 '
        })

        print(wcc_df.T)
        print("---------------------------------")


    def avg_rels_per_entity(num_kg, dataset, prefix, type, sample):
        print("deg_" + "KG" + num_kg)
        kg = KnowledgeGraph(num_kg, dataset, prefix, type, "original", "").graph
        nodes_deg = kg.degree()

        counter = 0
        for pair in nodes_deg:
            counter += pair[1]
        avg_node_deg = counter / kg.number_of_nodes()

        b_dict = dict()
        b_dict["original"] = avg_node_deg

        for i in range(5):
            conf_id = "conf_" + str(i) + "_only_p"
            
            kg = KnowledgeGraph(num_kg, dataset, prefix, type, sample, conf_id).graph
            nodes_deg = kg.degree()

            counter = 0
            for pair in nodes_deg:
                counter += pair[1]
            avg_node_deg = counter / kg.number_of_nodes()
            b_dict[conf_id] = avg_node_deg
        
        df = pd.DataFrame.from_dict(b_dict, orient='index').T

        df = df.rename(columns={
            'conf_0_only_p': '0 ',
            'conf_1_only_p': '0.15 ',
            'conf_2_only_p': '0.50 ',
            'conf_3_only_p': '0.85 ',
            'conf_4_only_p': '1 '
        })

        df = df.T
        print(df)
        print("---------------------------------")

    def max_comp(num_kg, dataset, prefix, type, sample):
        print("maxCS_" + "KG" + num_kg)
        kg = KnowledgeGraph(num_kg, dataset, prefix, type, "original", "")
        comps = sorted(nx.weakly_connected_components(kg.graph), key=len)
        max_len = len(comps[-1])/kg.graph.number_of_nodes()

        b_dict = dict()
        b_dict["original"] = max_len

        for i in range(5):
            conf_id = "conf_" + str(i) + "_only_p"
            
            kg = KnowledgeGraph(num_kg, dataset, prefix, type, sample, conf_id)
            comps = sorted(nx.weakly_connected_components(kg.graph), key=len)
            max_len = len(comps[-1])/kg.graph.number_of_nodes()
            b_dict[conf_id] = max_len
        
        df = pd.DataFrame.from_dict(b_dict, orient='index').T

        df = df.rename(columns={
            'conf_0_only_p': '0 ',
            'conf_1_only_p': '0.15 ',
            'conf_2_only_p': '0.50 ',
            'conf_3_only_p': '0.85 ',
            'conf_4_only_p': '1 '
        })

        df = df.T
        print(df)
        print("---------------------------------")