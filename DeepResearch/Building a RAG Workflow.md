# Building a RAG Workflow

Learn how to build a RAG workflow with Together AI embedding and chat endpoints\!

## Introduction

For AI models to be effective in specialized tasks, they often require domain-specific knowledge. For instance, a financial advisory chatbot needs to understand market trends and products offered by a specific bank, while an AI legal assistant must be equipped with knowledge of statutes, regulations, and past case law.

A common solution is Retrieval-Augmented Generation (RAG), which retrieves relevant data from a knowledge base and combines it with the user’s prompt, thereby improving and customizing the model's output to the provided data.

## ![][image1] RAG Explanation

RAG operates by preprocessing a large knowledge base and dynamically retrieving relevant information at runtime.

Here's a breakdown of the process:

1. Indexing the Knowledge Base: The corpus (collection of documents) is divided into smaller, manageable chunks of text. Each chunk is converted into a vector embedding using an embedding model. These embeddings are stored in a vector database optimized for similarity searches.  
2. Query Processing and Retrieval: When a user submits a prompt that would initially go directly to a LLM we process that and extract a query, the system searches the vector database for chunks semantically similar to the query. The most relevant chunks are retrieved and injected into the prompt sent to the generative AI model.  
3. Response Generation: The AI model then uses the retrieved information along with its pre-trained knowledge to generate a response. Not only does this reduce the likelihood of hallucination since relevant context is provided directly in the prompt but it also allows us to cite to source material as well.

## ![][image2] Download and View the Dataset

wget https://raw.githubusercontent.com/togethercomputer/together-cookbook/refs/heads/main/datasets/movies.json

mkdir datasets

mv movies.json datasets/movies.json

import together, os

from together import Together

\# Paste in your Together AI API Key or load it

TOGETHER\_API\_KEY \= os.environ.get("TOGETHER\_API\_KEY")

import json

with open('./datasets/movies.json', 'r') as file:

    movies\_data \= json.load(file)

movies\_data\[:1\]

This dataset consists of movie information as below:

\[{'title': 'Minions',

  'overview': 'Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.',

  'director': 'Kyle Balda',

  'genres': 'Family Animation Adventure Comedy',

  'tagline': 'Before Gru, they had a history of bad bosses'},

 {'title': 'Interstellar',

  'overview': 'Interstellar chronicles the adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.',

  'director': 'Christopher Nolan',

  'genres': 'Adventure Drama Science Fiction',

  'tagline': 'Mankind was born on Earth. It was never meant to die here.'},

 {'title': 'Deadpool',

  'overview': 'Deadpool tells the origin story of former Special Forces operative turned mercenary Wade Wilson, who after being subjected to a rogue experiment that leaves him with accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life.',

  'director': 'Tim Miller',

  'genres': 'Action Adventure Comedy',

  'tagline': 'Witness the beginning of a happy ending'}\]

## Implement Retrieval Pipeline \- "R" part of RAG

Below we implement a simple retrieval pipeline:

1. Embed movie documents and query  
2. Obtain top k movies ranked based on cosine similarities between the query and movie vectors.

\# This function will be used to access the Together API to generate embeddings for the movie plots

from typing import List

import numpy as np

def generate\_embeddings(input\_texts: List\[str\], model\_api\_string: str) \-\> List\[List\[float\]\]:

    """Generate embeddings from Together python library.

    Args:

        input\_texts: a list of string input texts.

        model\_api\_string: str. An API string for a specific embedding model of your choice.

    Returns:

        embeddings\_list: a list of embeddings. Each element corresponds to the each input text.

    """

    together\_client \= together.Together(api\_key \= TOGETHER\_API\_KEY)

    outputs \= together\_client.embeddings.create(

        input=input\_texts,

        model=model\_api\_string,

    )

    return np.array(\[x.embedding for x in outputs.data\])

\# We will concatenate fields in the dataset in prep for embedding

to\_embed \= \[\]

for movie in movies\_data:

    text \= ''

    for field in \['title', 'overview', 'tagline'\]:

        value \= movie.get(field, '')

        text \+= str(value) \+ ' '

    to\_embed.append(text.strip())

\# Use bge-base-en-v1.5 model to generate embeddings

embeddings \= generate\_embeddings(to\_embed, 'BAAI/bge-base-en-v1.5')

This will generate embeddings of the movies which we can use later to retrieve similar movies.

When a use makes a query we can embed the query using the same model and perform a vector similarity search as shown below:

from sklearn.metrics.pairwise import cosine\_similarity

\# Generate the vector embeddings for the query

query \= "super hero action movie with a timeline twist"

query\_embedding \= generate\_embeddings(\[query\], 'BAAI/bge-base-en-v1.5')\[0\]

\# Calculate cosine similarity between the query embedding and each movie embedding

similarity\_scores \= cosine\_similarity(\[query\_embedding\], embeddings)

We get a similarity score for each of our 1000 movies \- the higher the score, the more similar the movie is to the query.

We can sort this similarity score to get the movies most similar to our query \= `super hero action movie with a timeline twist`

\# Get the indices of the highest to lowest values

indices \= np.argsort(-similarity\_scores)

top\_10\_sorted\_titles \= \[movies\_data\[index\]\['title'\] for index in indices\[0\]\]\[:10\]

top\_10\_sorted\_titles

This produces the top ten most similar movie titles below:

\['The Incredibles',

 'Watchmen',

 'Mr. Peabody & Sherman',

 'Due Date',

 'The Next Three Days',

 'Super 8',

 'Iron Man',

 'After Earth',

 'Men in Black 3',

 'Despicable Me 2'\]

## We can encapsulate the above in a function

def retrieve(query: str, top\_k: int \= 5, index: np.ndarray \= None) \-\> List\[int\]:

    """

    Retrieve the top-k most similar items from an index based on a query.

    Args:

        query (str): The query string to search for.

        top\_k (int, optional): The number of top similar items to retrieve. Defaults to 5\.

        index (np.ndarray, optional): The index array containing embeddings to search against. Defaults to None.

    Returns:

        List\[int\]: A list of indices corresponding to the top-k most similar items in the index.

    """

    query\_embedding \= generate\_embeddings(\[query\], 'BAAI/bge-base-en-v1.5')\[0\]

    similarity\_scores \= cosine\_similarity(\[query\_embedding\], index)

    return np.argsort(-similarity\_scores)\[0\]\[:top\_k\]

Which can be used as follows:

retrieve("super hero action movie with a timeline twist", top\_k=5, index \= embeddings)

Which returns an array of indices for movies that best match the query.

array(\[172, 265, 768, 621, 929\])

## Generation Step \- "G" part of RAG

Below we will inject/augment the information the retrieval pipeline extracts into the prompt to the Llama3 8b Model.

This will help guide the generation by grounding it from facts in our knowledge base\!

\# Extract out the titles and overviews of the top 10 most similar movies

titles \= \[movies\_data\[index\]\['title'\] for index in indices\[0\]\]\[:10\]

overviews \= \[movies\_data\[index\]\['overview'\] for index in indices\[0\]\]\[:10\]

client \= Together(api\_key \= TOGETHER\_API\_KEY)

\# Generate a story based on the top 10 most similar movies

response \= client.chat.completions.create(

    model="meta-llama/Llama-3-8b-chat-hf",

    messages=\[

      {

        "role": "system",

        "content": "You are a pulitzer award winning craftful story teller. Given only the overview of different plots you can weave together an interesting storyline."},

      {

        "role": "user",

        "content": f"Tell me a story about {titles}. Here is some information about them {overviews}"},

    \],

)

print(response.choices\[0\].message.content)

Which produces the grounded output below:

What a delightful mix of plots\! Here's a story that weaves them together:

In a world where superheroes are a thing of the past, Bob Parr, aka Mr. Incredible, has given up his life of saving the world to become an insurance adjuster in the suburbs. His wife, Helen, aka Elastigirl, has also hung up her superhero suit to raise their three children. However, when Bob receives a mysterious assignment from a secret organization, he's forced to don his old costume once again.

As Bob delves deeper into the assignment, he discovers that it's connected to a sinister plot to destroy the world. The plot is masterminded by a group of rogue superheroes, who were once part of the Watchmen, a group of vigilantes that were disbanded by the government in the 1980s.

The Watchmen, led by the enigmatic Rorschach, have been secretly rebuilding their team and are now determined to take revenge on the world that wronged them. Bob must team up with his old friends, including the brilliant scientist, Dr. Manhattan, to stop the Watchmen and prevent their destruction.

Meanwhile, in a different part of the world, a young boy named Sherman, who has a genius-level IQ, has built a time-travel machine with his dog, Penny. When the machine is stolen, Sherman and Penny must travel through time to prevent a series of catastrophic events from occurring.

As they travel through time, they encounter a group of friends who are making a zombie movie with a Super-8 camera. The friends, including a young boy named Charles, witness a train derailment and soon discover that it was no accident. They team up with Sherman and Penny to uncover the truth behind the crash and prevent a series of unexplained events and disappearances.

As the story unfolds, Bob and his friends must navigate a complex web of time travel and alternate realities to stop the Watchmen and prevent the destruction of the world. Along the way, they encounter a group of agents from the Men in Black, who are trying to prevent a catastrophic event from occurring.

The agents, led by Agents J and K, are on a mission to stop a powerful new super criminal, who is threatening to destroy the world. They team up with Bob and his friends to prevent the destruction and save the world.

In the end, Bob and his friends succeed in stopping the Watchmen and preventing the destruction of the world. However, the journey is not without its challenges, and Bob must confront his own demons and learn to balance his life as a superhero with his life as a husband and father.

The story concludes with Bob and his family returning to their normal lives, but with a newfound appreciation for the importance of family and the power of teamwork. The movie ends with a shot of the Parr family, including their three children, who are all wearing superhero costumes, ready to take on the next adventure that comes their way.

Here we can see a simple RAG pipeline where we use semantic search to perform retrieval and pass relevant information into the prompt of a LLM to condition its generation.

To learn more about the Together AI API please refer to the [docs here](http:///docs/introduction) \!  


[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>