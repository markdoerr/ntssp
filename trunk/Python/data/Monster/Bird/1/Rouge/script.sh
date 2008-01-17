for i in *.bmp
do
	convert $i -colors 256 $i.bmp
	mv $i $i.old
	mv $i.bmp $i
done