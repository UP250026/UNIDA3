it_companies = {"Google", "Apple", "Microsoft"}

length = len(it_companies)
print("Length of it_companies array:", length)

it_companies.add("Twitter")
print("it_companies after adding Twitter:", it_companies)

it_companies.update({"Amazon", "Facebook", "Tesla"})
print("it_companies after adding multiple companies:", it_companies)

it_companies.remove("Facebook")
print("it_companies after removing Facebook:", it_companies)

# 5. What is the difference between remove and discard?
# - .remove() removes an item and throws an error if it is not found.
# - .discard() removes an item but does not throw an error if the item does not exist.

it_companies.discard('Twitter')

#exercises 2

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B
print("Union of A and B:", union)

intersection = A & B
print("Intersection of A and B:", intersection)

difference = A - B
print("Difference A - B:", difference)

symmetric_difference = A ^ B
print("Symmetric difference between A and B:", symmetric_difference)

is_subset = A <= B
print("Is A a subset of B?", is_subset)
#exercises 3

ages = [25, 30, 25, 20, 30, 30]

ages_set = set(ages)
print("Length of list of ages:", len(ages))
print("Length of set of ages:", len(ages_set))

sentence = "I am a teacher and I love inspiring and teaching people. people"
words = sentence.split()
unique_words = set(words)
print("Unique words in sentence:", unique_words)
print("Number of unique words:", len(unique_words))