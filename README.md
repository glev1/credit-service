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
├── datasets                    # Kaggle data
│   ├── cs-training.csv                 # Training dataset
│   └── Data Dictionary.xls             # Features description
└── notebooks                   # Data Science
    ├── EDA.ipynb
    ├── Modeling.ipynb
    └── README.md
```
## CLI Tools

The file `cli.py` is an endpoint that serves out predictions:

![CLI-help](https://raw.githubusercontent.com/glev1/credit-service/main/.github/images/cli_help.png)

 To predict some profile's chance of defaulting, use the following:
 `./cli.py --profile profile.json`

![CLI-profile](https://raw.githubusercontent.com/glev1/credit-service/main/.github/images/cli_profile.png)

The `profile.json` is an example file containing:

```
{
    "inc": 9000,
    "age": 30,
    "rev": 0.7,
    "debt": 0.8,
    "dep": 2,
    "cred": 5,
    "estate": 2,
    "lowdue": 2,
    "middue": 0,
    "highdue": 0
}
```

Further, `utilscli.py` perform some auxiliary functions, as model retrain:

`./utilscli.py retrain`

![CLI-profile](https://raw.githubusercontent.com/glev1/credit-service/main/.github/images/cli_retrain.png)

You can also query the API via `./utilscli.py predict --profile profile.json --host http://localhost:8080/predict`. This allows you to change both host and the profile passed into the API.