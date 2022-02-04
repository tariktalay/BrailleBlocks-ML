# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:49:24 2022

@author: emrey
"""
#!python OneDrive/Masaüstü/yolact-Block/eval.py  --trained_model=OneDrive/Masaüstü/yolact-master/weights/yolact_plus_resnet101_block_215_23289_interrupt.pth --config=yolact_resnet101_blocks_config --score_threshold=0.15 --top_k=15 --video_multiframe=4 --video=-1 --cuda==False
import torch 
print(torch.__version__)
print(torch.cuda.is_available())
