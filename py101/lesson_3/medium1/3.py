def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# The first one adds an element to the end of the list.


def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# This one concatenates a new list to the original list.

# the biggest difference is the first one is adding to the same list. while the 
# second one is reassigning a new list everytime. But the methods are the same