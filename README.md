# knowledge

Key/value store for topic -> information about the topic.

To install dependencies `pip install -r requirements.txt`. You also have to add a `api_key.txt` file with the AlchemyAPI key in the base directory (same directory as `knowledge_server.py`).

### Running the application

To run the knowledge server you can do `python knowledge_server.py`.

### Problems that this project attempts to solve

1. Given a paragraph or a sentence what "topics" or "entities" there are.
    - Basically an entity extraction problem.
2. Given a topic or an entity what entities are related to it.

### How to solve problem 1

- Use APIs and Knowledge bases to take sentences and give back the different entities that are in those sentences.
- Store the entities that are returned, and map Word -> Entity data. This way we are taking Taylor Swift -> Singer-Songwriter.
- Next time we're able to determine that Taylor Swift is an entity ourselves rather than using an API. This way we bootstrap our way up.

### Running a test

To run a test you can execute: `python setup.py test`, which will run all the tests in the folder `tests/`.
