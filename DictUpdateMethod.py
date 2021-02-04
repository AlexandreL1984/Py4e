#DictionaryUpdateMethod
model1 = {
  "first": "Kenzia",
  "last": "Fourati",
  "hair": "brown",
  "eyes": "blue"}

model2 = {
  "first": "Kendall",
  "last": "Jenner",
  "hair": "brown",
  "eyes": "brown"}

model3 = {
    "first": "Hayley",
    "last": "Atwell",
    "hair": "blonde",
    "eyes": "blue"}

model4 = {
    "first": "Samantha",
    "last": "Hoopes",
    "hair": "blonde",
    "eyes": "brown"}

model5 = {
    "first": "Sara",
    "last": "Sampaio",
    "hair": "brown",
    "eyes": "green"}

model6 = {
    "first": "Nina",
    "last": "Agdal",
    "hair": "light brown",
    "eyes": "brown"}


model1.update({"age": "33"})
model2.update({"age": "25"})
model3.update({"age": "38"})
model4.update({"age": "29"})
model5.update({"age": "29"})
model6.update({"age": "28"})

print(model1)
print(model2)
print(model3)
print(model4)
print(model5)
print(model6)
