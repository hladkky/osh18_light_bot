#!/bin/bash

# Define the input and output directories
PROTO_DIR="./proto"

# Create the output directory if it doesn't exist
mkdir -p $OUT_DIR

# Find all .proto files in the directory recursively
PROTO_FILES=$(find $PROTO_DIR -name "*.proto")

# Loop through each proto file and generate the corresponding files
for PROTO_FILE in $PROTO_FILES;
do
  echo "Compiling $PROTO_FILE"
  # Generate the Python files
  python -m grpc_tools.protoc -I. \
    --proto_path=$PROTO_DIR \
    --python_out=. \
    --grpc_python_out=. \
    $PROTO_FILE
done
