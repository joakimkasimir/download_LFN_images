#!/usr/bin/env bash
set -e
#set -u

org_dir=$(pwd)

# activate python virtuale environment
. env/bin/activate

# remove all current images in output directory
rm -rf outputdir

# Download images from URL
./get_LFN_images.py ${1}

# 
cd ../collage_maker

# activate python virtuale environment
. env/bin/activate

# Create a collage of images. You find the result as png files in this directory.
python collage_maker.py -f ${org_dir}/outputdir -w 400 -i 400 -o ${org_dir}/lfn_400.png -s
python collage_maker.py -f ${org_dir}/outputdir -w 800 -i 400 -o ${org_dir}/lfn_800.png -s
python collage_maker.py -f ${org_dir}/outputdir -w 1200 -i 400 -o ${org_dir}/lfn_1200.png -s
python collage_maker.py -f ${org_dir}/outputdir -w 1600 -i 400 -o ${org_dir}/lfn_1600.png -s
python collage_maker.py -f ${org_dir}/outputdir -w 1800 -i 400 -o ${org_dir}/lfn_1800.png -s
python collage_maker.py -f ${org_dir}/outputdir -w 2200 -i 400 -o ${org_dir}/lfn_2200.png -s
