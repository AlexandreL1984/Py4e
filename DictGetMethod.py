#DictionaryGetMethod
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

x = model1.get("first")
y = model2.get("first")
z = model3.get("first")
a = model4.get("first")
b = model5.get("first")

print(x, y, z, a, b)
