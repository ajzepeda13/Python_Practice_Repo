""" 3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.

* Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.

- Show that your list is still in its original order by printing it.
- Use sorted() to print your list in reverse alphabetical order without changing
the order of the original list.
- Show that your list is still in its original order by printing it again.
- Use reverse() to change the order of your list. Print the list to show that its
order has changed.
- Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
- Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
- Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.


"""


places = ['Tokyo', 'Paris', 'Berlin', 'New York', 'Mexico City', 'Medellin']

print()
print(f'Sorted List: {sorted(places)}')

print()
print(f'Original List: {places}')
print()


places.reverse()
print(f'Printing Reverse List: {places}')

print()
places.reverse()
print(f'Printing Original List: {places}')
print()

places.sort()
print(f'Sorting List: {places}')
print()


places.sort(reverse=True)
print(f'Sorting List on reverse order: {places}')
print()


"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
"""

# note will use same places list
print()
print(f'The number of places to go in the list are: {len(places)}')
print()