#!/usr/bin/env python3
# -*- coding: utf-8
"""
Created on 2018/12/24
@author yrh

"""

import os
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix
from sklearn.preprocessing import normalize
from logzero import logger

from deepxml.data_utils import get_sparse_feature


__all__ = ['build_tree_by_level']


def build_tree_by_level(sparse_data_x, sparse_data_y, mlb, eps: float, max_leaf: int, levels: list, groups_path):
    os.makedirs(os.path.split(groups_path)[0], exist_ok=True)
    logger.info('Clustering')
    sparse_x, sparse_labels = get_sparse_feature(sparse_data_x, sparse_data_y)
    sparse_y = mlb.transform(sparse_labels)
    logger.info('Getting Labels Feature')
    labels_f = normalize(csr_matrix(sparse_y.T) @ csc_matrix(sparse_x))
    logger.info('Start Clustering {}'.format(levels))
    levels, q = [2**x for x in levels], None
    logger.info("levels")
#    logger.info("levels {}".format(levels))
    for i in range(len(levels)-1, -1, -1):
        if os.path.exists('{}-Level-{}.npy'.format(groups_path,i)):
 #           print("path exists {}-Level-{}.npy".format(groups_path,i))
            labels_list = np.load('{}-Level-{}.npy'.format(groups_path,i))
            q = [(labels_i, labels_f[labels_i]) for labels_i in labels_list]
            break
    if q is None:
  #      logger.info("q is none")
        q = [(np.arange(labels_f.shape[0]), labels_f)]
    while q:
   #     logger.info("q values")
#        for i in q:
#            print(i)
        labels_list = np.asarray([x[0] for x in q])
    #    logger.info("labels_list: ")
#        for i in labels_list:
#            print(i)

        assert sum(len(labels) for labels in labels_list) == labels_f.shape[0]

     #   logger.info("len(labels_list): {}".format(len(labels_list)))

        if len(labels_list) in levels:
      #      logger.info("inside if {}".format(len(labels_list)))
            level = levels.index(len(labels_list))
       #     logger.info('Finish Clustering Level-{}'.format(level))
            np.save('{}-Level-{}.npy'.format(groups_path,level), np.asarray(labels_list))
        else:
        #    logger.info("here")
            logger.info('Finish Clustering {}'.format(len(labels_list)))
        next_q = []
        for node_i, node_f in q:
         #   logger.info("last loop")
            if len(node_i) > max_leaf:
          #      logger.info("last loop if")
                t = split_node(node_i, node_f, eps)
           #     logger.info("split_node returns")      
                next_q += list(t)
            #    logger.info("next_q")
        q = next_q
    #    logger.info("next iteration")
    logger.info('Finish Clustering')


def split_node(labels_i: np.ndarray, labels_f: csr_matrix, eps: float):
    #print("inside split node")
    n = len(labels_i)
    c1, c2 = np.random.choice(np.arange(n), 2, replace=False)
    centers, old_dis, new_dis = labels_f[[c1, c2]].toarray(), -10000.0, -1.0
    l_labels_i, r_labels_i = None, None
    #logger.info("new_dis {}".format(new_dis))
    #logger.info("old_dis {}".format(old_dis))
    #logger.info("eps {}".format(eps))
    while new_dis - old_dis >= eps:
     #   logger.info("new_dis {}".format(new_dis))
     #   logger.info("old_dis {}".format(old_dis))
     #   logger.info("eps {}".format(eps))
        dis = labels_f @ centers.T  # N, 2
        #print("1")
        partition = np.argsort(dis[:, 1] - dis[:, 0])
        #print("2")
        l_labels_i, r_labels_i = partition[:n//2], partition[n//2:]
       # print("3")
        old_dis, new_dis = new_dis, (dis[l_labels_i, 0].sum() + dis[r_labels_i, 1].sum()) / n
      #  print("4")
        centers = normalize(np.asarray([np.squeeze(np.asarray(labels_f[l_labels_i].sum(axis=0))),
                                        np.squeeze(np.asarray(labels_f[r_labels_i].sum(axis=0)))]))
     #   print("5")
    #logger.info("split_node done")
    #logger.info("new_dis {}".format(new_dis))
    #logger.info("old_dis {}".format(old_dis))
    #logger.info("eps {}".format(eps))
    #logger.info("diff {}".format(new_dis-old_dis))
    return (labels_i[l_labels_i], labels_f[l_labels_i]), (labels_i[r_labels_i], labels_f[r_labels_i])
