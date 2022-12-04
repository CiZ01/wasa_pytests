# WasaPhoto Python Tester
This is a simple Python script for testing the WasaPhoto API and populating the database. \
Currently, it only supports the population of the database. It will be updated to support the testing of the API in the future.

## Populating the database
To populate the database, the first step is to edit the **"config_population.json"** file with your attributes and an example of them. Each key in json file rappresent a table in the database and it attributes. \
The **"config_population.json"** file is structured as follow:
```json
{
    "table_name": {
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example"
    },
    "table_name": {
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example",
        "attribute_name": "attribute_example"
    }
}
```  
The example is for having a valid value. \
The second step is to run the **"populate.py"** script. \
The script have a username list for the users table. \
There are functions that generate random values, and functions that generate values based on the username list. \
\
For example, the **populateUser** function generate a number of user equal to the number of the usernames in the list and set the userID attribute equal to the index of the username in the list. \
```python
def populateUser(conn):
    for i in range(1, len(usernames_list)):
        user['userID'] = i
        user['username'] = usernames_list[i]
        addUser(conn)
```
