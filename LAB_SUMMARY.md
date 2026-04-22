# Final Lab Summary — Predictive Maintenance Pipeline

This repository contains the Lambda function and supporting files used to complete the CLCS 660 predictive maintenance lab. The goal of the lab was to implement a serverless inference pipeline using AWS S3, Lambda, SageMaker, DynamoDB, and SNS.

## Summary of Work Completed
- Implemented a Lambda function to process S3 events.
- Integrated the function with a SageMaker inference endpoint.
- Stored prediction results in DynamoDB.
- Published alerts to an SNS topic.
- Tested the pipeline using `test_data.json`.

## CloudWatch Findings
During testing, CloudWatch Logs showed that the Lambda function failed during the initialization phase due to a top-level statement executing before imports. This behavior was tied to restrictions in the UMGC student AWS environment, which limited certain runtime behaviors and prevented full module initialization.

## Repository Link
https://github.com/janebjobtech-cloud/predictive-maintenance-lambda

This repository satisfies the lab requirement to provide a public code repository link.
