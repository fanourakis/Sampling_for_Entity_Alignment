import argparse
import sys
import time

from openea.modules.args.args_hander import check_args, load_args
from openea.modules.load.kgs import read_kgs_from_folder
from openea.models.basic_model import BasicModel
from openea.approaches import RDGCN


class ModelFamily(object):
    BasicModel = BasicModel

    
    RDGCN = RDGCN


def get_model(model_name):
    return getattr(ModelFamily, model_name)


if __name__ == '__main__':
    t = time.time()
    args = load_args(sys.argv[1])
    if "conf_" in args.conf_id:
        args.training_data = args.training_data + args.dataset + '/' + args.conf_id + '/'
    else:
        args.training_data = args.training_data + args.dataset + '/'

    # args.dataset_division = sys.argv[2]
    print(args.embedding_module)
    print(args)
    remove_unlinked = False
    if args.embedding_module == "RSN4EA":
        remove_unlinked = True
    kgs = read_kgs_from_folder(args.training_data, args.dataset_division, args.alignment_module, args.ordered,
                               remove_unlinked=remove_unlinked)
    model = get_model(args.embedding_module)()
    model.set_args(args)
    model.set_kgs(kgs)
    model.init()
    model.run()
    model.test()
    model.save()
    print("Total run time = {:.3f} s.".format(time.time() - t))