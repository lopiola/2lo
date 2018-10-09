#!/bin/bash

if [ ! -z "$(git status --porcelain)" ]; then 
	echo "Commit your changes first! Or use -f to force deploy whatever is on origin/master"
	if [[ ${1} == "-f" ]]; then
		echo "Deploying origin/master (will not include your local changes)"
	else
 		exit 1
	fi
fi

echo ""

ssh lopiola@student.agh.edu.pl /bin/bash << EOF
	rm -rf public_html/*
	cd 2lo
	git fetch
	git reset --hard origin/master
	cp -R * ../public_html/
EOF

echo "Done! Visit: http://student.agh.edu.pl/~lopiola/"
open "http://student.agh.edu.pl/~lopiola/"