#!/usr/bin/env bash

echo 'changing directories to api directory'
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
pushd $SCRIPT_DIR

echo 'removing existing "build" directory'
rm -rf build || echo '"build" directory does not exist'
rm -rf build.zip || echo '"build.zip" file does not exist'
mkdir -p build

echo 'creating virtual environment'
python3 -m venv venv
source venv/bin/activate

echo 'adding artifacts to build directory'
cp api.py build
pip3 install -t build -r requirements.txt

echo 'zipping artifact'
pushd build
zip -r ../build.zip .
popd build

popd $SCRIPT_DIR