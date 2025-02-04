def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# {
    #     'prop1': "hi there",
    # }

# None

# The second function can't reach the dictionary.