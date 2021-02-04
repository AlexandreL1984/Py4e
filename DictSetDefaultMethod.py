#DictionarySetDefaultMethod
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
    "last": "Agdal",
    "hair": "light brown",
    "eyes": "brown"}


x = model1.setdefault("first", "unknown")
x1 = model2.setdefault("first", "unknown")
x2 = model3.setdefault("first", "unknown")
x3 = model4.setdefault("first", "unknown")
x4 = model5.setdefault("first", "unknown")
x5 = model6.setdefault("first", "unknown")

#I added a new line on the print fuction to make it neater

print(x,'\n')
print(x1,'\n')
print(x2,'\n')
print(x3,'\n')
print(x4,'\n')
print(x5,'\n')
