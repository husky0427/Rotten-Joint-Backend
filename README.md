# Rotten-Joint-Backend
Backend of the Rotten Joint hiking team app

## Environment setup

1. Download [Python 3.10.13](https://www.python.org/downloads/release/python-3913/)
2. Open a new terminal and clone this repo to a folder
3. Create a new virtual python environment for the project. <br/>
The folder name **virtualenv** is added to the `.gitignore` file, so we can just use **virtualenv** as the virtualenv name <br/>
The following command is written for Windows Command Prompt. There might be some differences between Mac OS terminal and Windows CMD. <br/>
    - Step 1: `cd` to your project folder <br/>
    - Step 2: Create a new virtual environment by `python -m venv virtualenv`. Make sure your are using python3.10.3 if you have multiple python versions installed on your machine. <br/>
    - Step 3: Activate the virtualenv. `cd <path to your project folder..>/virtualenv/Scripts` and then execute `activate`. After you activate the virtual environment, you should see `(virtualenv)` appears at the left of your command line. This indicates the virtualenv is activated. <br/>
    - Step 4: Install python packages. Run `python -m pip install -r requirements.txt`. This command will install all packages in `requirements.txt` for you.<br/>


## Start the backend on localhost

Execute `uvicorn app.main:app --reload`. By default, your backend will use port 8000. You may check `http://localhost:8000` to see if the server is up.

## OpenApi documentation on localhost
1. Start backend Server
2. `http//localhost:8000/redoc`


## Backend unittest 

Backend unittest is written in **pytest**.

To execute the unittest, execute `pytest tests` at the root folder.

Backend unittest related files locate at `/tests/`.
