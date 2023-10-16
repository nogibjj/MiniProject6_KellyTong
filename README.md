# IDS 706 Mini Project 6

This repository is for IDS706 mini project week 6. 

## Purpose 
    This repository is for building an ETL-Query pipeline to perform Github actions 
    such as extract, transform and load, and query. 
    A Cloud Database (MySQL) is hosted in Azure and connected to this Github repository 
    through secret variables access_tokens, host_name and HTTP_path. 
    Two csv files are extracted from two source url. 
    Then they are cleaned, transformed and loaded into 2 .db files. 
    Complex Query is performed to join the two datasets based on the desired order and
    their common variables. Joined table will be generated automatically. 
    In these case, the two datasets (csv files) are extracted into women_stem.db and 
    all_ages.db which store the information about major and employment. 
    This Github action allows extract, transform and load. and query to be performed 
    seperately in codespace. It also enables flexibility in performing these in single command.
    
## Important Things included are:
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes CI.yml, which contain configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file. This specific main.py gets the python versions and operation system names. 

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py

- ``mylib`` includes ``_init_.py````extract.py`` ``transform_load.py`` and ``query.py`` which are used to extract
  a csv from an url, clean it and return a db file, and perform complex query.

## Github actions
Status badges for CI.yml
`CI.yml`
[![CI](https://github.com/nogibjj/MiniProject6_KellyTong/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/MiniProject6_KellyTong/actions/workflows/CI.yml)

## Result Query

Query is run with the following commands. 

<img width="583" alt="Query" src="https://github.com/nogibjj/MiniProject6_KellyTong/assets/142815940/5ad28a32-e702-4e70-b427-6e2b4f00b67a">

Results can be found in the [query_log.md](https://github.com/nogibjj/MiniProject6_KellyTong/blob/main/query_log.md)


## Building Process

The building process starts with installing the packages. 


`make install`

**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

<img width="820" alt="截屏2023-10-02 23 40 02" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/ba733b30-5da5-4f44-b2c1-237813b0597c">

`make extract` `make transform_load` `make query`

**make extract, make transform_load, make query**


<img width="1195" alt="extract, transform_load and query" src="https://github.com/nogibjj/MiniProject6_KellyTong/assets/142815940/b117da7a-29ab-4251-b8cf-9a0294128cff">


`make lint`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`

**Make test** calls the command python -m pytest -vv --cov=main test_*.py

<img width="1128" alt="make test" src="https://github.com/nogibjj/MiniProject6_KellyTong/assets/142815940/fc23924e-98d7-4aec-a629-338f9e45dc26">


`make format`

**Make format** calls the command black *.py

<img width="236" alt="make format" src="https://github.com/nogibjj/MiniProject6_KellyTong/assets/142815940/00967237-209c-4f89-96e1-cedc49c276c4">


`make generate_and_push` `make deploy`

**Make generate_and push, make deploy** 

<img width="744" alt="generate_and _push and deploy" src="https://github.com/nogibjj/MiniProject6_KellyTong/assets/142815940/2fa8b869-5cdf-4727-b486-8dc1a430bed1">


## Visualization for how the process work

![1_xHSzARQPes6JhHe_jNGRdg](https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/57a7ce64-dab8-40c3-a066-87fe9862dd41)

p.s. For specific query log please see query_log.md in the repository. 
