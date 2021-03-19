# Test_stage_ftn

## functionality

fetch open issue on "https://github.com/PyGithub/PyGithub/issues" > export data in .json format, then print result on a website which is running with python script.

## Requierement

Python3 PyGithub (Python library to use the Github API v3)

   > pip install PyGithub

## How to use ?

We have to fill the .json file with the followed command:

   > python ./API/export_data.py

Next, run the HTTPS server (for some ports we need to use "sudo" before the command):

  >  python3 myserver.py -p "port"

PEM Pass phrase is asked for SSL, "test" is the answer:

  >  Enter PEM pass phrase: test
