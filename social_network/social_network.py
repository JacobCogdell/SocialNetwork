class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend: 'Person'):
        if friend not in self.friends:
            self.friends.append(friend)

    def __repr__(self):
        return f"Person(name='{self.name}')"
    



class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}    

    def add_person(self, name: str):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"Person '{name}' already exists in the network.")

    def add_friendship(self, person1_name: str, person2_name: str):

        if person1_name not in self.people:
            print(f"Person '{person1_name}' not found in the network.")     
            return
        if person2_name not in self.people:
            print(f"Person '{person2_name}' not found in the network.")     
            return
        
        self.people[person1_name].add_friend(self.people[person2_name])
        self.people[person2_name].add_friend(self.people[person1_name])
    
    def print_network(self):
        # This syntax loops over the both keys and values of the dictionary
        for name, person in self.people.items():
            if person.friends:
                friend_list = ", ".join(friend.name for friend in person.friends)
                print(f"{name} is friends with {friend_list}")
            else:
                print(f"{name} has no friends defined.")


# Test your code here
network = SocialNetwork()
network.add_person("Alex")
network.add_person("Jordan")
print(network.people)
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
network.add_person("Cruella")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network() 
