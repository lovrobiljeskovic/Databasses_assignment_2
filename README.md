# Databasses_assignment_2
Solution to our second database assignment

This python script connects to a MongoDB and runs the queries on the imported twitter dataset and prints out the results. (I didn't know how to make a query for question number three)
## How to run:

prerequisites:
```
pip3 install pymongo
```
In case you don't have python 3:

```
pip install pymongo
```

This is taking into consideration that you've unzipped the .csv files provided and ran
all the neccessary docker/mongo commands.

Clone the repo and change the line 6 of .py file to be ```db = client.{your_name_of_db}```
and run:
```
python3 assignment_2.py
``` 

or in case you don't have python3:
```
python assignment_2.py
```

This will print out results to all the queries

