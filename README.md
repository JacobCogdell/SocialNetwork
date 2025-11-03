# Social Network Graph

This project implements a social networking platform using a graph data structure in Python. People are represented as nodes and friendships as bidirectional edges, allowing you to model real-world social connections where relationships are mutual and dynamic.

The system uses two custom classes to manage user relationships: a Person class to represent individual users and a SocialNetwork class to manage the collection of people and their connections.

## Features

- Add new people to the network
- Create bidirectional friendships between users
- Handle errors when connecting non-existent users
- Print the entire network structure
- Prevent duplicate users

## Classes

### `Person` Class

Represents an individual user in the social network.

**Constructor**
- `Person(name: str)`

**Attributes**
- `name` (str): The person's name
- `friends` (list): List of Person objects this person is connected to

**Methods**
- `add_friend(friend: Person) -> None`: Adds another Person to the friends list

**Example Usage**

```python
alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends) # []
alex.add_friend(jordan)
print(alex.friends[0].name)  # Jordan
```

### `SocialNetwork` Class

Manages the entire social network and all user relationships.

**Constructor**
- `SocialNetwork()`

**Attributes**
- `people` (dict): Dictionary where keys are names and values are Person instances

**Methods**
- `add_person(name: str) -> None`: Creates a new Person and adds them to the network
- `add_friendship(person1_name: str, person2_name: str) -> None`: Establishes bidirectional friendship between two people
- `print_network() -> None`: Prints all people and their friends

**Example Usage**

```python
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
network.add_person("Morgan")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")  # Error: Taylor doesn't exist

network.print_network()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111 
Index 6: Empty
Index 7: - Rebecca: 999-444-9999 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris")) # None
```