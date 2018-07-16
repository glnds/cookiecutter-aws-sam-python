# Cookiecutter SAM for Python Lambda functions with CodePipeline integration

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless App based on Serverless Application Model (SAM) and Python 3.6.

It is important to note that you should not try to `git clone` this project but use `cookiecutter` CLI instead as ``{{cookiecutter.project_slug}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## TODO (prioritised)
1. Fix API GW logs
1. Add a name prefix so multiple stacks can be deployed in the same account
1. Test behaviour when API GW role is already present
1. Extend X-Ray functionality
1. Add persistency (DynamoDB) in a separate pipeline
1. Add BitBucket support
1. Create an application bucket to hold all artefacts and documentation
	Set correct CORS for swagger....
1. Add a custom domain name 
1. Add DLQ
1. Add a post hook example
1. Add a custom metric
1. teardown. delete stack then pipeline. Describe + add make target
1. Add a Build badge to the Readme
1. Add Support for Golang and NodeJS
1. Describe project layout: Pipeline.yml, output.yml, buildspec, ...
1. Describe features: CodePipeline, doint the Heavy lifting, Gitops
1. Add option for ELK stack


Blog post:  CN V1&2, Paved road, GitOps, Heavy lifting....

## Requirements

Install `cookiecutter` command line: 

**Pip users**:

* `pip install cookiecutter`

**Homebrew users**:

* `brew install cookiecutter`

**Windows or Pipenv users**:

* `pipenv install cookiecutter`

**NOTE**: [`Pipenv`](https://github.com/pypa/pipenv) is the new and recommended Python packaging tool that works across multiple platforms and makes Windows a first-class citizen.

## Usage

Generate a new SAM based Serverless App: `cookiecutter gh:glnds/cookiecutter-aws-sam-python`. 

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

**NOTE**: After you understand how cookiecutter works (cookiecutter.json, mainly), you can fork this repo and apply your own mechanisms to accelerate your development process and this can be followed for any programming language and OS.


# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [Forked from aws-samples](https://github.com/aws-samples/cookiecutter-aws-sam-python)


License
-------

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
