# FILE = dir_list
FILE=$1
COUNT=0
FILE_LENGTH=$(wc -l $FILE | awk '{print $1}')
for line in $(cat $FILE);
do 
    figlet _; 
    echo ==== $COUNT / $FILE_LENGTH ====; 
    # echo $(dirname $line); 
    echo $line; 
    figlet _;
    # python inter_region_noise_corrs_setup.py $(dirname $line);
    # python inter_region_noise_corrs_plot.py $(dirname $line);
    python inter_region_noise_corrs_setup.py $line;
    # python inter_region_noise_corrs_plot.py $line;
    COUNT=$((COUNT+1));
done
