advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
new_advice = []

for word in advice.split():
    if word == "house":
        break
    new_advice.append(word)

print(" ".join(new_advice))


print(advice.split("house")[0])