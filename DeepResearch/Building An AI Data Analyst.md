# Building An AI Data Analyst

Learn how to use code interpreter to build an AI data analyst with E2B and Together AI.

Giving LLMs the ability to execute code is very powerful – it has many advantages such as:

* Better reasoning  
* More complex tasks (e.g., advanced data analysis or mathematics)  
* Producing tangible results such as charts  
* Immediate testing (and correcting) of the produced output.

In this example, we'll show you how to build an AI data analyst that can read in data and make charts. We'll be using [E2B](https://e2b.dev/docs) for the code interpreter and Together AI for the LLM piece.

## 1\. Prerequisites

Create a`main.ipynb` file and save your Together & E2B API keys in there.

Get the E2B API key [here](https://e2b.dev/docs/getting-started/api-key) and the Together AI API key [here](https://api.together.xyz/settings/api-keys). Download the CSV file from [here](https://www.kaggle.com/datasets/nishanthsalian/socioeconomic-country-profiles/code) and upload it to the same directory as your program. Rename it to `data.csv`.

## 2\. Install the SDKs

pip install together==1.2.6 e2b-code-interpreter==0.0.10 dotenv==1.0.0

## 3\. Define your model and system prompt

In the following code snippet, we'll define our API keys, our model of choice, and our system prompt.

You can pick the model of your choice by uncommenting it. There are some recommended models that are great at code generation, but you can add a different one from [here](http:///docs/serverless-models#chat-models).

For the system prompt, we tell the model it's a data scientist and give it some information about the uploaded CSV. You can choose different data but will need to update the instructions accordingly.

from dotenv import load\_dotenv

import os

import json

import re

from together import Together

from e2b\_code\_interpreter import CodeInterpreter

load\_dotenv()

\# TODO: Get your Together AI API key from https://api.together.xyz/settings/api-keys

TOGETHER\_API\_KEY \= os.getenv("TOGETHER\_API\_KEY")

\# TODO: Get your E2B API key from https://e2b.dev/docs

E2B\_API\_KEY \= os.getenv("E2B\_API\_KEY")

\# Choose from the codegen models:

MODEL\_NAME \= "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"

\# MODEL\_NAME \= "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

\# MODEL\_NAME \= "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

\# MODEL\_NAME \= "codellama/CodeLlama-70b-Instruct-hf"

\# MODEL\_NAME \= "deepseek-ai/deepseek-coder-33b-instruct"

\# MODEL\_NAME \= "Qwen/Qwen2-72B-Instruct"

\# See the complete list of Together AI models here: https://api.together.ai/models.

SYSTEM\_PROMPT \= """You're a Python data scientist. You are given tasks to complete and you run Python code to solve them.

Information about the csv dataset:

\- It's in the \`/home/user/data.csv\` file

\- The CSV file is using , as the delimiter

\- It has the following columns (examples included):

    \- country: "Argentina", "Australia"

    \- Region: "SouthAmerica", "Oceania"

    \- Surface area (km2): for example, 2780400

    \- Population in thousands (2017): for example, 44271

    \- Population density (per km2, 2017): for example, 16.2

    \- Sex ratio (m per 100 f, 2017): for example, 95.9

    \- GDP: Gross domestic product (million current US$): for example, 632343

    \- GDP growth rate (annual %, const. 2005 prices): for example, 2.4

    \- GDP per capita (current US$): for example, 14564.5

    \- Economy: Agriculture (% of GVA): for example, 10.0

    \- Economy: Industry (% of GVA): for example, 28.1

    \- Economy: Services and other activity (% of GVA): for example, 61.9

    \- Employment: Agriculture (% of employed): for example, 4.8

    \- Employment: Industry (% of employed): for example, 20.6

    \- Employment: Services (% of employed): for example, 74.7

    \- Unemployment (% of labour force): for example, 8.5

    \- Employment: Female (% of employed): for example, 43.7

    \- Employment: Male (% of employed): for example, 56.3

    \- Labour force participation (female %): for example, 48.5

    \- Labour force participation (male %): for example, 71.1

    \- International trade: Imports (million US$): for example, 59253

    \- International trade: Exports (million US$): for example, 57802

    \- International trade: Balance (million US$): for example, \-1451

    \- Education: Government expenditure (% of GDP): for example, 5.3

    \- Health: Total expenditure (% of GDP): for example, 8.1

    \- Health: Government expenditure (% of total health expenditure): for example, 69.2

    \- Health: Private expenditure (% of total health expenditure): for example, 30.8

    \- Health: Out-of-pocket expenditure (% of total health expenditure): for example, 20.2

    \- Health: External health expenditure (% of total health expenditure): for example, 0.2

    \- Education: Primary gross enrollment ratio (f/m per 100 pop): for example, 111.5/107.6

    \- Education: Secondary gross enrollment ratio (f/m per 100 pop): for example, 104.7/98.9

    \- Education: Tertiary gross enrollment ratio (f/m per 100 pop): for example, 90.5/72.3

    \- Education: Mean years of schooling (female): for example, 10.4

    \- Education: Mean years of schooling (male): for example, 9.7

    \- Urban population (% of total population): for example, 91.7

    \- Population growth rate (annual %): for example, 0.9

    \- Fertility rate (births per woman): for example, 2.3

    \- Infant mortality rate (per 1,000 live births): for example, 8.9

    \- Life expectancy at birth, female (years): for example, 79.7

    \- Life expectancy at birth, male (years): for example, 72.9

    \- Life expectancy at birth, total (years): for example, 76.4

    \- Military expenditure (% of GDP): for example, 0.9

    \- Population, female: for example, 22572521

    \- Population, male: for example, 21472290

    \- Tax revenue (% of GDP): for example, 11.0

    \- Taxes on income, profits and capital gains (% of revenue): for example, 12.9

    \- Urban population (% of total population): for example, 91.7

Generally, you follow these rules:

\- ALWAYS FORMAT YOUR RESPONSE IN MARKDOWN

\- ALWAYS RESPOND ONLY WITH CODE IN CODE BLOCK LIKE THIS:

      \`\`\`python'

      {code}

      \`\`\`'

   \- the Python code runs in jupyter notebook.

   \- every time you generate Python, the code is executed in a separate cell. it's okay to make multiple calls to \`execute\_python\`.

   \- display visualizations using matplotlib or any other visualization library directly in the notebook. don't worry about saving the visualizations to a file.

   \- you have access to the internet and can make api requests.

   \- you also have access to the filesystem and can read/write files.

   \- you can install any pip package (if it exists) if you need to be running \`\!pip install {package}\`. The usual packages for data analysis are already preinstalled though.

   \- you can run any Python code you want, everything is running in a secure sandbox environment

   """

## 4\. Add code interpreting capabilities and initialize the model

Now we define the function that will use the E2B code interpreter. Every time the LLM assistant decides that it needs to execute code, this function will be used. Read more about the Code Interpreter SDK [here](https://e2b.dev/docs/code-interpreter/installation).

We also initialize the Together AI client. The function for matching code blocks is important because we need to pick the right part of the output that contains the code produced by the LLM. The chat function takes care of the interaction with the LLM. It calls the E2B code interpreter anytime there is a code to be run.

def code\_interpret(e2b\_code\_interpreter, code):

    print("Running code interpreter...")

    exec \= e2b\_code\_interpreter.notebook.exec\_cell(

        code,

        on\_stderr=lambda stderr: print("\[Code Interpreter\]", stderr),

        on\_stdout=lambda stdout: print("\[Code Interpreter\]", stdout),

        \# You can also stream code execution results

        \# on\_result=...

    )

    if exec.error:

        print("\[Code Interpreter ERROR\]", exec.error)

    else:

        return exec.results

client \= Together()

pattern \= re.compile(

    r"\`\`\`python\\n(.\*?)\\n\`\`\`", re.DOTALL

)  \# Match everything in between \`\`\`python and \`\`\`

def match\_code\_blocks(llm\_response):

    match \= pattern.search(llm\_response)

    if match:

        code \= match.group(1)

        print(code)

        return code

    return ""

def chat\_with\_llm(e2b\_code\_interpreter, user\_message):

    print(f"\\n{'='\*50}\\nUser message: {user\_message}\\n{'='\*50}")

    messages \= \[

        {"role": "system", "content": SYSTEM\_PROMPT},

        {"role": "user", "content": user\_message},

    \]

    response \= client.chat.completions.create(

        model=MODEL\_NAME,

        messages=messages,

    )

    response\_message \= response.choices\[0\].message

    python\_code \= match\_code\_blocks(response\_message.content)

    if python\_code \!= "":

        code\_interpreter\_results \= code\_interpret(e2b\_code\_interpreter, python\_code)

        return code\_interpreter\_results

    else:

        print(f"Failed to match any Python code in model's response {response\_message}")

        return \[\]

## 5\. Upload the dataset

The CSV data is uploaded programmatically, not via AI-generated code. The code interpreter by E2B runs inside the E2B sandbox. Read more about the file upload [here](https://e2b.dev/docs/sandbox/api/upload).

def upload\_dataset(code\_interpreter):

    print("Uploading dataset to Code Interpreter sandbox...")

    dataset\_path \= "./data.csv"

    if not os.path.exists(dataset\_path):

        raise FileNotFoundError("Dataset file not found")

    try:

        with open(dataset\_path, "rb") as f:

            remote\_path \= code\_interpreter.upload\_file(f)

        if not remote\_path:

            raise ValueError("Failed to upload dataset")

        print("Uploaded at", remote\_path)

        return remote\_path

    except Exception as error:

        print("Error during file upload:", error)

        raise error

## 6\. Put everything together

Finally we put everything together and let the AI assistant upload the data, run an analysis, and generate a PNG file with a chart. You can update the task for the assistant in this step. If you decide to change the CSV file you are using, don't forget to update the prompt too.

with CodeInterpreter(api\_key=E2B\_API\_KEY) as code\_interpreter:

    \# Upload the dataset to the code interpreter sandbox

    upload\_dataset(code\_interpreter)

    code\_results \= chat\_with\_llm(

        code\_interpreter,

        "Make a chart showing linear regression of the relationship between GDP per capita and life expectancy from the data. Filter out any missing values or values in wrong format.",

    )

    if code\_results:

        first\_result \= code\_results\[0\]

    else:

        raise Exception("No code interpreter results")

\# This will render the image if you're running this in a notebook environment.

\# If you're running it as a script, you can save the image to a file using the Pillow library.

first\_result

## 7\. Run the program and see the results

The resulting chart is generated within the notebook. The plot shows the linear regression of the relationship between GDP per capita and life expectancy from the CSV data:

Uploading dataset to Code Interpreter sandbox...

Uploaded at /home/user/data.csv

\==================================================

User message: Make a chart showing linear regression of the relationship between GDP per capita and life expectancy from the data. Filter out any missing values or values in wrong format.

\==================================================

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear\_model import LinearRegression

\# Load the data

data \= pd.read\_csv('/home/user/data.csv', delimiter=',')

\# Clean the data

data \= data.dropna(subset=\['GDP per capita (current US$)', 'Life expectancy at birth, total (years)'\])

data\['GDP per capita (current US$)'\] \= pd.to\_numeric(data\['GDP per capita (current US$)'\], errors='coerce')

data\['Life expectancy at birth, total (years)'\] \= pd.to\_numeric(data\['Life expectancy at birth, total (years)'\], errors='coerce')

\# Fit the linear regression model

X \= data\['GDP per capita (current US$)'\].values.reshape(-1, 1\)

y \= data\['Life expectancy at birth, total (years)'\].values.reshape(-1, 1\)

model \= LinearRegression().fit(X, y)

\# Plot the data and the regression line

plt.scatter(X, y, color='blue')

...

plt.xlabel('GDP per capita (current US$)')

plt.ylabel('Life expectancy at birth, total (years)')

plt.show()

Running code interpreter...

## ![][image1] Resources

* [More guides: Mixture of Agents](http:///docs/mixture-of-agents)  
* [E2B docs](https://e2b.dev/docs)  
* [E2B Cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main)

[image1]: <data:image/png;base64,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>