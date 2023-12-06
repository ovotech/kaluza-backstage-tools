# Batch script

We're aware that creating your catalog-info files individually can be tedious, especially when you're starting from scratch and registering everything in one go, so we've developed a simple script to make this easier. Just put together a CSV with some information about each service, run the script, and it will generate your `catalog-info.yaml` files. It may not include _every_ annotation you could ever need, but it does allow you to very quickly go from a spreadsheet of services to yaml files without having to write them by hand (or do too much copy-pasting!)

## Creating your CSV file

We've found it's easiest to create a spreadsheet, compile all of your info, and then export it as a CSV. 

Based on the example in `file.csv` it should look something like this:

|name           |description               |owner       |githubSlug             |circleSlug                    |tags            |system        |type |architectureLinks   |technicalLinks   |supportLinks         |dependsOn |providesApis      |consumesApis      |
|---------------|--------------------------|------------|-----------------------|------------------------------|----------------|--------------|-----|--------------------|-----------------|---------------------|----------|------------------|------------------|
|example-service|This is an example service|example-team|ovotech/example-service|github/ovotech/example-service|test test1 test2|example-system|infra|https://.../some-arch-doc|http://.../some-tech-doc|https://.../some-support-doc|dependency|api:produces|api:consumes|

**Things to note:**

* You can have multiple `tags`, `architectureLinks`, `technicalLinks`, `supportLinks`, `dependsOn`, `providesApis`, and `consumesApis`. Just separate each one with a newline.
* You can also leave `tags`, `architectureLinks`, `technicalLinks`, `supportLinks`, `dependsOn`, `providesApis`, and `consumesApis` blank and they will be omitted from the output.
* You can leave `circleSlug` blank if you don't use CircleCI, it will be omitted from the output.
* You can leave `type` blank and it will default to `service`.

## Prerequisites

The script relies on Jinja2 for templating:
```sh
pip install Jinja2
```

## How to use the script

1. Clone the repo

```sh
git clone https://github.com/ovotech/kaluza-backstage-tools
```

2. Navigate to the `batch-script` folder

```sh
cd batch-script
```

3. Update your local copy of `file.csv` with your service information, making sure to follow the example format. If you follow the steps in [Creating your CSV file](#creating-your-csv-file), this will just be the output of exporting your spreadsheet as a CSV.

4. From the command line, run the following command 

```sh
python3 batch-catalog-file.py
```

This will generate a `catalog-info-{repo-name}.yaml` for every GitHub repository referenced in your CSV. Each of these files will define the components and any systems that are referenced.

5. Commit these files to the appropriate repositories and register them in Backstage, as you normally would!

_Note_: The script assumes you don't have any existing catalog files in your repos, and that any systems referenced don't exist yet. If they _do_ exist, then you can just copy-paste the relevant blocks of yaml in!


