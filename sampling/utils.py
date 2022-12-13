from sklearn.model_selection import train_test_split
import os

class Utils:

    @staticmethod
    def check_embedding_constraints(kg1, ents1, ents2):

        seed_pairs = kg1.get_seed_pairs()
        not_included_in_both = 0
        counterparts = set()
        for e in ents1:
            if seed_pairs[e] not in ents2:
                not_included_in_both += 1
                counterparts.add(seed_pairs[e])
        
        assert not_included_in_both == 0

        print(not_included_in_both)

        print(len(ents1))
        print(len(ents2))
        print()

    @staticmethod
    def generate_seeds_and_splittings(dataset, prefix, ents1, ents2, dest_seed_path):

        splittings = {
            "test_pairs": { "src_path": "../datasets/original/" + dataset + prefix + "_RREA/721_5fold/2/test_links", "pairs": dict(), "dest_path": "sampled/" + dataset + "_sampled/721_5fold/2/test_links"},
            "train_pairs": { "src_path": "../datasets/original/" + dataset + prefix + "_RREA/721_5fold/2/train_links", "pairs": dict(), "dest_path": "sampled/" + dataset + "_sampled/721_5fold/2/train_links"},
            "valid_pairs": { "src_path": "../datasets/original/" + dataset + prefix + "_RREA/721_5fold/2/valid_links", "pairs": dict(), "dest_path": "sampled/" + dataset + "_sampled/721_5fold/2/valid_links"}
        }

        seed_alignment = {}
        train_ratio = 0.20
        validation_ratio = 0.10
        test_ratio = 0.70
        X = []
        for s in splittings:
            with open(splittings[s]["src_path"]) as fp:
                for line in fp:
                    if int(line.split("\t")[0]) in ents1 and int(line.split("\t")[1].rstrip()) in ents2:
                        seed_alignment[int(line.split("\t")[0])] = int(line.split("\t")[1].rstrip())
                        X.append(line.rstrip("\n"))
        
        x_train, x_test = train_test_split(X, test_size=1 - train_ratio)
        x_val, x_test = train_test_split(x_test, test_size=test_ratio / (test_ratio + validation_ratio))

        isExist = os.path.exists(dest_seed_path)
        if not isExist:
            os.makedirs(dest_seed_path)

        with open(dest_seed_path + "ent_links", "w") as fp:
            for s in seed_alignment:
                fp.write(str(s))
                fp.write("\t")
                fp.write(str(seed_alignment[s]))
                fp.write("\n")

        with open(dest_seed_path + "train_links", "w") as fp:
            for x in x_train:
                fp.write(x)
                fp.write("\n")

        with open(dest_seed_path + "valid_links", "w") as fp:
                for x in x_val:
                    fp.write(x)
                    fp.write("\n")

        with open(dest_seed_path + "test_links", "w") as fp:
            for x in x_test:
                fp.write(x)
                fp.write("\n")