from config import *

for category in CATEGORIES:
    print(category)
    for subCategory in CATEGORIES[category]:
        print(subCategory)
