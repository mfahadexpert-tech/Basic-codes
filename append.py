items=["pen","pencil","eraser","sharpener"]
items.remove("pencil")
print(items)
#Lists aur Mutability (Intermediate)
#Grocery List: Aik list banayein jis mein 3 items hon. User se chotha (4th) item
#input lein aur use .append() ke zariye add karein
items.append("marker")
print(items)
items.pop()
print(items)
print(len(items))