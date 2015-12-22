# knowledge

Key/value store for topic -> information about the topic. To communicate from other applications this project uses RPCs and protobufs.

To build project run `make`.

### Problems that this project attempts to solve

1. Given a paragraph or a sentence what "topics" or "entities" there are.
    - Basically an entity extraction problem
2. Given a topic or an entity what entities are related to it.

### Running a test

To run a test you can execute: `python -m tests.external.test_google`, which will run the python file `tests/external/test_google.py`. This is a way around relative imports and adding to a PYTHONPATH, which is also possible.
