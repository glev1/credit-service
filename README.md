# Credit Service

## Description

This is a Flask App that performs credit scoring.

Banks play a crucial role in market economies. They decide who can get finance and on what terms and can make or break investment decisions. For markets and society to function, individuals and companies need access to credit. 

Here, you can predict the probability that somebody will experience financial disstress in the next two years.

The application is Continuos Deployed via AWS App Runner. [Acess it here.](https://d5vebxns3y.us-east-2.awsapprunner.com/)

## Dataset

You can access the dataset at [Kaggle - Give me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit/data)

## Application Structure

```
credit-service
├── app.py                      # Flask App
├── cli.py                      # CLI main code
├── utilscli.py                 # CLI helper commands
├── Makefile                  
├── predict.sh                  # Bash commands to perform Flask App prediction
├── profile.json                # Example of profile file
├── README.md                  
├── requirements.txt           
├── src                         # Source code
│   ├── conf                        # Configuration Files
│   │   ├── design.json
│   │   ├── __init__.py
│   │   ├── model.json
│   │   └── preprocess.json
│   ├── __init__.py
│   ├── main                        # MLOps Library
│   │   ├── __init__.py
│   │   └── mlib.py
│   ├── resources                   # Operational resources
│   │   └── models                      # Trained models
│   │       └── model.joblib
│   └── utils                       # Helper functions
│       ├── config.py
│       ├── data_utils.py
│       ├── __init__.py
│       └── model_util.py
├── datasets                        # Kaggle data
│   ├── cs-training.csv                 # Training dataset
│   └── Data Dictionary.xls             # Features description
└── notebooks                       # Data Science
    ├── EDA.ipynb
    ├── Modeling.ipynb
    └── README.md
```
