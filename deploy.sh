#!/bin/sh

git checkout master
git add resenbrock.png 
git remote add origin2 https://${GITHUB_TOKEN}@github.com/NiMlr/optimization-benchmark.git
git commit -m "update leaderboard"
git push origin2
