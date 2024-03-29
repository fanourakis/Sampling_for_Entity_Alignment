import os
from datetime import datetime

class Configuration:

    c = None


    def __init__(self, dataset, prefix, measure, sampling_size, p, c, conf_id, export_sampled=False):
        self.id = conf_id
        self.dataset = dataset
        self.prefix = prefix
        self.measure = measure
        self.sampling_size = sampling_size
        self.p = p
        self.c = c
        self.export_sampled = export_sampled

    def __init__(self, dataset, prefix, measure, sampling_size, p, conf_id, export_sampled=False):
        self.id = conf_id
        self.dataset = dataset
        self.prefix = prefix
        self.measure = measure
        self.sampling_size = sampling_size
        self.p = p
        self.export_sampled = export_sampled
    
    def export(self, path):
        with open(path, "w") as fp:
            fp.write("timestamp: " + str(datetime.now()))
            fp.write("\n")
            fp.write("conf_id: " + str(self.id))
            fp.write("\n")
            fp.write("dataset: " + str(self.dataset))
            fp.write("\n")
            fp.write("prefix: " + str(self.prefix))
            fp.write("\n")
            fp.write("measure: " + str(self.measure))
            fp.write("\n")
            fp.write("sampling_size: " + str(self.sampling_size))
            fp.write("\n")
            fp.write("p: " + str(self.p))
            fp.write("\n")
            fp.write("c: " + str(self.c))
            fp.write("\n")
            fp.write("export_sampled: " + str(self.export_sampled))