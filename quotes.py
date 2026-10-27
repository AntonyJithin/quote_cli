# Import Libraries
import random
import json

# Variables
count = 1
authors =  []

# quotes list
quotes_list = [
    "\"The secret of getting ahead is getting started.\" — Mark Twain",
    "\"Do what you can, with what you have, where you are.\" — Theodore Roosevelt",
    "\"Start moving before planning perfectly.\" — James Clear",
    "\"Successful people do what unsuccessful people are not willing to do. Don't wish it were easier; wish you were better.\" — Jim Rohn",
    "\"Eighty percent of success is showing up.\" — Woody Allen",
    "\"Courage doesn't always roar. Sometimes courage is the little voice at the end of the day that says I'll try again tomorrow.\" — Mary Anne Radmacher",
    "\"What lies behind you and what lies in front of you pales in comparison to what lies inside you.\" — Ralph Waldo Emerson",
    "\"A river cuts through rock, not because of its power, but because of its persistence.\" — James N. Watkins",
    "\"Action is a great restorer and builder of confidence. Inaction is not only the result, but the cause, of fear.\" — Norman Vincent Peale",
]


# Function to print n number of quotes from the quotes list
def print_n_quotes(count):
    for i in range(count):
        print("» " + random.choice(quotes_list))


# Function to get the authors list
def get_authors_list():
    # Hotfix: Check if the source list is empty before processing
    if not quotes_list:
        print("No quotes available to process.")
        return

    for quote in quotes_list:
        authors.append(quote.strip('"').split(' — ')[-1])
    authors_sorted = sorted(authors)
    [print(" - " + author) for author in authors_sorted]


def get_all_quotes_json():
    data = {
        "quotes": [
            {
                "quote": quote.split(" — ")[0].strip('"'),
                "author": quote.split(" — ")[1]
            }
            for quote in quotes_list
        ]
    }
    return json.dumps(data, indent=4)


# Make function calls
print_n_quotes(3)
get_authors_list()
data = get_all_quotes_json()
print(data)

# wip
# Fix1
# Fix2