#!/bin/sh

data='data/fish.data'
model='Model/PRB_B0.cfg'
weight='backup/fish/PRB_B0_final.weights'
test_image='fish_final_test.txt'
threshold='0.3'

python writeTxt_fish.py

./darknet detector test $data $model $weight -dont_show -save_labels < $test_image -thresh $threshold

python classifier_fish.py