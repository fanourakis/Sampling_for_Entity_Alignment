from KG.KnowledgeGraph import *
import os
from Statistics.Statistics import Statistics

def start_analysis(dataset, prefix, measure, sample, conf_id):

    print("-----START ANALYSIS-----")

    print(dataset + " " + sample + " " + conf_id)

    kg1_mdi = KnowledgeGraph("1", dataset, prefix, "multi_directed", sample, conf_id)
    kg2_mdi = KnowledgeGraph("2", dataset, prefix, "multi_directed", sample, conf_id)

    kg1_mun = KnowledgeGraph("1", dataset, prefix, "multi_undirected", sample, conf_id)
    kg2_mun = KnowledgeGraph("2", dataset, prefix, "multi_undirected", sample, conf_id)

    Statistics.weakly_conn_comps("degree", sample, dataset, prefix, "1", "NO_CSLS")
    Statistics.avg_rels_per_entity("1", dataset, prefix, "multi_directed", sample)
    Statistics.max_comp("1", dataset, prefix, "multi_directed", sample)

    Statistics.weakly_conn_comps("degree", sample, dataset, prefix, "2", "NO_CSLS")
    Statistics.avg_rels_per_entity("2", dataset, prefix, "multi_directed", sample)
    Statistics.max_comp("2", dataset, prefix, "multi_directed", sample)