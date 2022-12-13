from tkinter.font import names
from KG.KnowledgeGraph import *
from samplers.ControlComponentsSizes import *
from Statistics.Statistics import *
from utils import Utils
import sys
import os

def start_sampling(conf):
    conf_id = conf.id
    measure = conf.measure
    dataset = conf.dataset
    prefix = conf.prefix
    sampling_size = conf.sampling_size
    p = conf.p
    export_sampled = conf.export_sampled

    kg1_mdi = KnowledgeGraph("1", dataset, prefix, "multi_directed", "original", "original")
    kg2_mdi = KnowledgeGraph("2", dataset, prefix, "multi_directed", "original", "original")

    kg1_mun = KnowledgeGraph("1", dataset, prefix, "multi_undirected", "original", "original")
    kg2_mun = KnowledgeGraph("2", dataset, prefix, "multi_undirected", "original", "original")

    print("\n-----START SAMPLING WITH ONLY P-----")

    _, _, ents1, ents2, sampled_graph1, sampled_graph2, sampled_df, sampled_df2 = ControlComponentsSizes.RJ_only_p(kg1_mdi, kg2_mdi, kg1_mun, kg2_mun, sampling_size, p)

    print(sampled_graph1.number_of_nodes())
    
    print(sampled_graph2.number_of_nodes())

    Utils.check_embedding_constraints(kg1_mdi, ents1, ents2)
    
    if export_sampled:
        Utils.generate_seeds_and_splittings(dataset, prefix, ents1, ents2, "sampled/" + dataset + "_sampled/" + conf_id + "/721_5fold/2/")
        dest_path = "sampled/" + dataset + "_sampled/" + conf_id + "/"
        isExist = os.path.exists(dest_path)
        if isExist:
            if input("are you sure you want to override " + dest_path + " ? (y/n) ") != "y":
                exit()
        if not isExist:
            os.makedirs(dest_path)
        sampled_df.to_csv("sampled/" + dataset + "_sampled/" + conf_id + "/triples_1", sep="\t", index=False, columns=["e1", "r", "e2"], header=False)  
        sampled_df2.to_csv("sampled/" + dataset + "_sampled/" + conf_id + "/triples_2", sep="\t", index=False, columns=["e1", "r", "e2"], header=False)
        conf.export("sampled/" + dataset + "_sampled/" + conf_id + "/" + "configuration.txt")