#! /bin/bash
for i in $(seq 1 11);
do
	echo "coverting Tranck $i..."
	ffmpeg -i Track\ $i.wav -vn -ar 44100 -ac 2 -ab 192k t$((i+18)).mp3
done
