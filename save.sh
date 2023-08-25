#!/bin/bash
git add .
read commit_name
echo "Nombre del Commit: "$commit_name
git commit -m "$commit_name"
git push -u origin main
