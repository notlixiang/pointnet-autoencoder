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

class JsonGenerate():
    def __init__(self, root):
        self.root = root
        self.catfile = os.path.join(self.root, 'synsetoffset2category.txt')
        self.cat = {}  # 类别名称和对应文件夹
        self.basenames = []
        self.meta = {}
        self.jsonall = []

    def get_file_basename(self):
        with open(self.catfile, 'r') as f:  # 读入类别名称和对应文件夹
            for line in f:
                ls = line.strip().split()
                self.cat[ls[0]] = ls[1]

        for item in self.cat:
            self.meta[item] = []
            dir_point = os.path.join(self.root, self.cat[item], 'points')
            fns = sorted(os.listdir(dir_point))  # 点云文件名称


            for fn in fns:  # fns: 文件名.pts
                token = (os.path.splitext(os.path.basename(fn))[0])
                # self.meta[item].append((os.path.join(dir_point, token + '.pts'), os.path.join(dir_seg, token + '.seg')))
                self.meta[item].append((os.path.join(dir_point, token + '.pts'), 'seg'))
                self.jsonall.append(os.path.join('shape_data',self.cat[item], token))
    def write_json(self):


if __name__ == '__main__':
    g=JsonGenerate(root = os.path.join(BASE_DIR, 'data/plan_data'))
    g.get_file_basename()

