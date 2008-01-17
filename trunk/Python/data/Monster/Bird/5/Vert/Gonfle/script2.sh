mkdir 4
for i in *.bmp
do
	convert $i -colors 256 -support 0 -resize 85% 4/$i
done
mkdir 3
for i in *.bmp
do
	convert $i -colors 256 -support 0 -resize 70% 3/$i
done
mkdir 2
for i in *.bmp
do
	convert $i -colors 256 -support 0 -resize 50% 2/$i
done
mkdir 1
for i in *.bmp
do
	convert $i -colors 256 -support 0 -resize 38% 1/$i
done