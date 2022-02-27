import json
import random


def handler(event, context):

    friends = [
        "Pei Pacetti", "Sung Spears", "Ashlee Alderson", "Aimee Acker",
        "Keneth Koehler", "Joseph Julio", "Vida Vickrey", "Isaac Iannuzzi",
        "Janey Jeske", "Oralia Ostendorf"
    ]

    print("start")
    first = choose(Friends=friends, Chosen=None)
    second = choose(Friends=friends, Chosen=first)

    return {"statusCode": 200, "body": {"first": first, "second": second}}


def choose(**kwargs):
    friends = kwargs.get('Friends', None)
    chosen = kwargs.get('Chosen', None)

    # Select a random number from 0 to size of list

    random.seed()
    while True:
        number = random.randint(0, len(friends))
        print(f"number = {number}/{len(friends)} friend = {friends[number]}")

        if chosen != friends[number]:
            return friends[number]


if __name__ == "__main__":
    response = handler({}, "")
    print(response)
    