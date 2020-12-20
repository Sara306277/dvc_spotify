# DVC Spotify

DVC is a command-line tool written in Python and it mimics Git commands and workflows. In particular, it is commonly used for AI/ML experiment management but it can also be useful to build pipelines, consisting in different stages.

In this work, "DVC Spotify" allows to build a simple pipeline where each stage represents a block of code extracted from the Colab Notebook "Spotify SNA". Since there are many blocks and some of them require a lot of time to be executed, the pipeline has been created by considering few pieces of the notebook.

## Setup

These instructions allow to configure everything in order to run the existing code and create the pipeline.

### Download

The first step consists in installing DVC locally.

```sh
pip install dvc
```

There is the need to use a remote storage; in this case, Google drive was considered: this requires to install the following package.

```sh
pip install dvc[gdrive]
```

### Configuration

The directory "src" contains four Python files that represents the stages of the pipeline; each of these .py files takes in input the initial dataset or the output obtained from another stage. The outputs of the different stages are contained in the directory "data".
You need to have the Python files on your machine in order to create the pipeline and they can be also modified, by inserting other lines of code.

To save the entire work on a Github repository, run the following code;

```sh
git init
dvc init -q
git commit -m "Initialize DVC Project"
```

## Run

The starting point of the pipeline is the dataset of related artists obtained through the Spotify API. After adding the dataset, it is possible to commit changes on Github repository.

```sh
dvc add data/related_artists.json
git add data/.gitignore data/related_artists.json.dv
git commit -m "Add row data"
dvc push -q
```

To run the first stage, named "prep_graph":

```sh
dvc run -n prep_graph -d src/prepare.py -d data/related_artists.json -o data/prepared python src/prepare.py data/related_artists.json
```

By executing the following command, it is possible to obtain and observe a graphical representation of the created pipeline.

```sh
dvc dag
```

The same steps must be repeated for the other stages.
After pushing all the changes on the Github repository, a remote storage has been added.

```sh
dvc remote add --default drive gdrive://'Id'
dvc push
```

## Authors

* Sara Mosca