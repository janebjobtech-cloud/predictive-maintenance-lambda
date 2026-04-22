# Predictive Maintenance Lambda Function

This repository contains the AWS Lambda function and supporting files used for the CLCS 660 predictive maintenance lab. The function processes S3 events, invokes a SageMaker endpoint for inference, writes alerts to DynamoDB, and publishes notifications through SNS.

## Repository Contents
- `lambda_function.py` — Main Lambda function code.
- `test_data.json` — Sample input file used to trigger the Lambda function.
- `README.md` — Documentation for the repository.

## Notes About the Student AWS Environment
This project was completed in a restricted student AWS environment provided by UMGC.  
Some Lambda runtime behaviors, debugging steps, and code deployment actions were limited by the environment’s permissions.  
As a result, certain initialization errors (e.g., module import failures) could not be fully resolved within the constraints of the lab environment.

## Purpose
This repository is provided to satisfy the lab requirement:
**“Include a link to your code repository (GitHub, GitLab, etc.)”**

## Repository Link
https://github.com/janebjobtech-cloud/predictive-maintenance-lambda
