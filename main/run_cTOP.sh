sample=$1
python scr/CSI.py $sample
python scr/GE.py $sample
for i in `seq 2 8`
do
echo -e "python scr/cTOP.py $sample $i; python scr/TFModule.py $sample $i;python scr/SubNetwork.py $sample $i;python scr/get_cell_annotation.py $sample $i"
done | parallel 
