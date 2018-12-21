# -*- coding: utf-8 -*-
'''
    Dataset for shapenet part segmentaion.
'''

import os
import os.path
import json
import numpy as np
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_file_basename(path):






def write_json(main_names):

if __name__ == '__main__':
    d = PartDataset(root=os.path.join(BASE_DIR, 'data/shapenetcore_partanno_segmentation_benchmark_v0'),
                    class_choice=None, split='trainval')
    print(len(d))
    import time

    tic = time.time()
    i = 100
    ps, seg = d[i]
    print np.max(seg), np.min(seg)
    print(time.time() - tic)
    print(ps.shape, type(ps), seg.shape, type(seg))
    sys.path.append('utils')
    import show3d_balls

    print(len(d))
    ps, cls = d[0]
    print(ps.shape, type(ps), cls.shape, type(cls))

