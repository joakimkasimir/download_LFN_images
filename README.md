# Download Local Food Nodes images
This is a simple scraping script. With it you can create collage of images by cloning https://github.com/delimitry/collage_maker 

## Preparations ##
Clone this repository and https://github.com/delimitry/collage_maker as parallel directories.

## How to run it ##
Activate Python virtual Environment and install packages: 
```bash
cd download_LFN_images
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd ../collage_maker
virtualenv env
source env/bin/activate
pip install Pillow
```

Install all needed packagesi and run the code:
```bash
cd download_LFN_images
./generateImage.sh https://localfoodnodes.org/node/kavlinge-matnod?date=2018-10-24
```
Inactivate the virtualenv with command:
```bash
deactivate
```
## Check in the code ##
Remove all security and credentials information from config.yaml
Before you check in your code run:
```bash
pip freeze > requirements.txt
```
