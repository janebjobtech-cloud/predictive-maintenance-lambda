# Architecture Overview

This project implements a serverless predictive maintenance pipeline using:

- **Amazon S3** — Input storage for metric files.
- **AWS Lambda** — Event-driven processing and inference orchestration.
- **Amazon SageMaker** — Real-time model inference endpoint.
- **Amazon DynamoDB** — Storage for prediction results and alerts.
- **Amazon SNS** — Email notifications for high-risk predictions.

The Lambda function is triggered by S3 `ObjectCreated:Put` events and performs inference using the SageMaker endpoint. Results are written to DynamoDB and alerts are published to SNS.

Due to restrictions in the UMGC student AWS environment, certain debugging and runtime behaviors were limited.
