# OA Metadata Standards Mapping

A tool for visualising mappings between UK repository-related metadata schemas.

The schemas and mappings are described using a series of CSV files (see `data` directory):

* `schemas.csv` - defines the schemas to be visualised (title, version, URL etc.)
* `fields.csv`- lists the fields defined by each schema
* `mappings.csv`- describes the mappings between schema fields, optionally with suggestions and examples

The CSV data is used to generate an interactive HTML-based visualisation of the mappings.

## Initial setup

After cloning the repository:

    mkdir build
    git clone git@github.com:sherpaservices/OA-Metadata-Standards-Mapping.git build
    cd build
    git checkout gh-pages
    cd ..

### Prerequisites

For convenience a self-contained development environment can be used to generate the visualisation.

Install the following:

* Vagrant https://www.vagrantup.com/
* Virtualbox (or similar) https://www.virtualbox.org/

## Generating visualisation

From the repository root directory;

    vagrant up
    vagrant ssh
    cd /vagrant
    ./build.sh
    logout

Open `/path/to/OA-Metadata-Standards-Mapping/build/index.html` in a browser to view result.

## Deployment

### GitHub Pages (Linux only)

A script is included to deploy the output to GitHub Pages:

From the repository root directory:

    ./deploy.sh

Open `https://jisc-services.github.io/OA-Metadata-Standards-Mapping in a browser to view result.
