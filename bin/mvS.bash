#!/bin/bash

echo "Move data to a remote compute node"
echo "Usage: $0 <NODE>"

[ $# -eq 1 ] || { echo "One argument required"; exit 1; }

### Variables ###
NODE=$1
DT=`date "+%d-%H%M%S"`
DIR=$PWD
NAME=${PWD##*/}.$DT

### Info ###
hostname > INFO
pwd >> INFO

### Copy data ###
rsync -avz "$DIR/" $NODE:SCRATCH/$NAME

### Create sync script ###
sleep 0.1
###
cat << EOF > "$DIR/sync.bash"
#!/bin/bash

rsync -auvz --exclude='QCSCRATCH' --exclude='*.tmp' --exclude='WORK' $NODE:SCRATCH/$NAME/ . || exit 1

if [ "\$1" = "-d" ]
then
     ssh $NODE "rm -rv SCRATCH/$NAME" || exit 2
     rm sync.bash
fi
EOF
###
chmod +x sync.bash
