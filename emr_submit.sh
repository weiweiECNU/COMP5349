#!/bin/bash

spark-submit \
    --master local[4] \
    AverageRatingPerGenre.py \
    --input file:///home/hadoop/COMP5349_a1_b/ \
    --output file:///home/hadoop/dislike_out/
	 

    
