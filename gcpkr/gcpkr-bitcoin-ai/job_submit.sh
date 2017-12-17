#!/bin/sh

PROJECT_ID=gcpkr-bitcoin
BUCKET_NAME=${PROJECT_ID}-ml
JOB_NAME=model
OUTPUT_PATH=gs://$BUCKET_NAME/$JOB_NAME
REGION=asia-east1
NOW="$(date +'%Y%m%d%H%M')"
ML_JOB=bitcoin_train_$NOW
gcloud ml-engine jobs submit training $ML_JOB \
    --job-dir $OUTPUT_PATH \
    --runtime-version 1.2 \
    --module-name trainer.model \
    --package-path trainer/ \
    --region $REGION
