import json

data= [
  {
    "model": "opinion_ate.restaurant",
    "pk": 1,
    "fields": {
      "name": "Sushi Place",
      "address": "123 Main Street"
    }
  },
  {
    "model": "opinion_ate.dish",
    "pk": 1,
    "fields": {
      "name": "Volcano Roll",
      "rating": 3,
      "restaurant_id": 1
    }
  },
  {
    "model": "opinion_ate.dish",
    "pk": 2,
    "fields": {
      "name": "Salmon Nigiri",
      "rating": 4,
      "restaurant_id": 1
    }
  },
  {
    "model": "opinion_ate.restaurant",
    "pk": 2,
    "fields": {
      "name": "Burger Place",
      "address": "456 Other Street"
    }
  },
  {
    "model": "opinion_ate.dish",
    "pk": 3,
    "fields": {
      "name": "Barbecue Burger",
      "rating": 5,
      "restaurant_id": 2
    }
  },
  {
    "model": "opinion_ate.dish",
    "pk": 4,
    "fields": {
      "name": "Slider",
      "rating": 3,
      "restaurant_id": 2
    }
  }
]

json_object= json.dumps(data, indent= 4)

with open("sample.json", "w") as f:
	f.write(json_object)