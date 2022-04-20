#!/bin/bash

if (( $# < 1 )); then
 echo "At least 1 parameter (input data strint) is required"
 exit 1
fi
READER_OPT=
ARGS_ALL=" --session default --severity info --shm-segment-size 12000000000 --infologger-severity warning --no-cleanup "
CONFIG_ALL="NameConf.mDirGRP=./files;NameConf.mDirGeom=./files;NameConf.mDirCollContext=./files;NameConf.mDirMatLUT=./files;keyval.input_dir=./files;keyval.output_dir=/dev/null;"
o2-ctf-reader-workflow $ARGS_ALL --delay 1  --ctf-input $1 --onlyDet MFT $READER_OPT |
o2-mft-reco-workflow $ARGS_ALL --configKeyValues "${CONFIG_ALL};MFTTracking.FullClusterScan=true;" --clusters-from-upstream --disable-mc --disable-root-output --pipeline mft-tracker:1 |
./o22-eve-display $ARGS_ALL --configKeyValues "${CONFIG_ALL}" --display-tracks MFT --display-clusters MFT --jsons-folder $2 --disable-mc --no-empty-output |
o2-dpl-run $ARGS_ALL --run -b
