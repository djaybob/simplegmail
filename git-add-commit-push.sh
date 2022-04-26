#!/bin/bash

for dir in /home/ubuntu/projects-gitlab/*/     # list directories in the form "/tmp/dirname/"
do
    dir=${dir%*/}      # remove the trailing "/"
    cd "/home/ubuntu/projects-gitlab/${dir##*/}"    # print everything after the final "/"
    git add .
    git status
    git commit -m "Bulk Commit"
    git push
done