import sys
import os

from numpy import array
from Configuration import Configuration
from start_sampling import *
from start_analysis import *

if __name__ == '__main__':

    args = sys.argv[1:]

    if args[0] == "start_sampling":
        conf_array = {
            "conf_0_only_p": {
                "p": 0,
            },
            "conf_1_only_p": {
                "p": 0.15,
            },
            "conf_2_only_p": {
                "p": 0.50,
            },
            "conf_3_only_p": {
                "p": 0.85,
            },
            "conf_4_only_p": {
                "p": 1.0,
            },
        }
        conf_id = args[1]
        conf = Configuration("D_Y_15K_V1", "", "", 1000, conf_array[conf_id]["p"], conf_id, export_sampled=True)
        start_sampling(conf)

    if args[0] == "start_analysis":
        if args[1] == "original":
            sample = "original"
            conf_id = "original"
        elif args[1] == "sampled":
            sample = "sampled"
            conf_id = args[2]
        start_analysis("D_Y_15K_V1", "", "degree", sample, conf_id)