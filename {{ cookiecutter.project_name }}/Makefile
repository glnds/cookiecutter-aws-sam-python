#################################################
# Please use mmake: https://github.com/tj/mmake #
#################################################

SHELL=bash

APP_NAME={{ cookiecutter.project_name.lower().replace(' ', '-') }}

# In order to use moto in AWS CodeBuild the following to environment varibales need to be unset.
# https://forums.aws.amazon.com/thread.jspa?messageID=785174
unexport AWS_DEFAULT_REGION
unexport AWS_CONTAINER_CREDENTIALS_RELATIVE_URI

check_defined = \
		$(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))

# Remove all python artifacts.
clean-pyc:
	@echo "Removing python artifacts..."
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
.PHONY: clean-pyc

# Run the unit tests.
unittest:
	@echo "Running unittests..."
	AWS_XRAY_CONTEXT_MISSING=LOG_ERROR pytest -s -v .
.PHONY: unittest

# Lint python code.
lint:
	@echo "Running Python Codestyle check..."
	pycodestyle --max-line-length 100 --ignore E402,W503,E704 --statistics --exclude=src/lib/* .
.PHONY: lint

# Run test coverage.
coverage:
	@echo "Run unittests and report on coverage..."
	pytest -s -v --cov-report html --cov-report term --no-cov-on-fail --cov-fail-under=35 --cov-branch --cov-config .coveragerc --cov src/
.PHONY: coverage

# Run clean-pyc, lint and unittest targets.
test: clean-pyc lint unittest
.PHONY: test

# Run clean-pyc, lint and coverage targets.
fulltest: clean-pyc lint coverage
.PHONY: fulltest

# Create the CloudFormation stack.
create-pipeline:
	@:$(call check_defined, OAUTH_TOKEN)
	@echo "Creating Cloudformation Stack ${APP_NAME}-pipeline."
	@aws cloudformation create-stack --stack-name ${APP_NAME}-pipeline --template-body file://pipeline.yaml --parameters \
		ParameterKey=ApplicationName,ParameterValue=${APP_NAME} \
		ParameterKey=ArtifactBucket,ParameterValue=dpp-artifacts-400007416746-eu-west-1-cfn \
		ParameterKey=GitHubOAuthToken,ParameterValue=${OAUTH_TOKEN} \
		ParameterKey=GitHubUser,ParameterValue=glnds \
		ParameterKey=GitHubRepository,ParameterValue=sam-by-example \
		ParameterKey=GitHubBranch,ParameterValue=master \
		--region eu-west-1 --capabilities CAPABILITY_NAMED_IAM --output text
	@echo "Waiting for Cloudformation stack to complete..."
	@aws cloudformation wait stack-create-complete --region eu-west-1 --stack-name ${APP_NAME}-pipeline
	@echo "Deployment complete!"
.PHONY: create-pipeline

# Update the CloudFormation stack.
update-pipeline:
	@:$(call check_defined, OAUTH_TOKEN)
	@echo "updating Cloudformation Stack ${APP_NAME}-pipeline."
	@aws cloudformation update-stack --stack-name ${APP_NAME}-pipeline --template-body file://pipeline.yaml --parameters \
		ParameterKey=ApplicationName,ParameterValue=${APP_NAME} \
		ParameterKey=ArtifactBucket,ParameterValue=dpp-artifacts-400007416746-eu-west-1-cfn \
		ParameterKey=GitHubOAuthToken,ParameterValue=${OAUTH_TOKEN} \
		ParameterKey=GitHubUser,ParameterValue=glnds \
		ParameterKey=GitHubRepository,ParameterValue=sam-by-example \
		ParameterKey=GitHubBranch,ParameterValue=master \
		--region eu-west-1 --capabilities CAPABILITY_NAMED_IAM --output text
	@echo "Waiting for Cloudformation update stack to complete..."
	@aws cloudformation wait stack-update-complete --region eu-west-1 --stack-name ${APP_NAME}-pipeline
	@echo "Stack update complete!"
.PHONY: update-pipeline

# Delete the CloudFormation stack.
delete-pipeline:
	@echo "Delete Cloudformation Stack ${APP_NAME}-pipeline."
	@aws cloudformation delete-stack --region eu-west-1 --stack-name ${APP_NAME}-pipeline
	@echo "Waiting for Cloudformation delete stack to complete..."
	@aws cloudformation wait stack-delete-complete --region eu-west-1 --stack-name ${APP_NAME}-pipeline
	@echo "Stack removed!"
.PHONY: delete-pipeline
