from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for local development

# Sample recipe data
data = {
    'recipe_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'recipe_name': [
        "Spaghetti Bolognese", 
        "Chocolate Chip Cookies", 
        "Caesar Salad", 
        "Spaghetti Tounsia",
        "Vegetable Stir Fry", 
        "Chicken Alfredo", 
        "Grilled Cheese Sandwich", 
        "Pancakes", 
        "Beef Tacos", 
        "Tomato Soup", 
        "Veggie Burger", 
        "Lemon Meringue Pie",
        "Chicken Caesar Wrap", 
        "Mushroom Risotto", 
        "Pulled Pork Sandwich", 
        "Apple Pie",
        "Chicken Stir Fry", 
        "Tuna Salad", 
        "Fried Rice", 
        "Beef Stew", 
        "Chicken Wings", 
        "Salmon Fillet", 
        "Lasagna", 
        "Vegetarian Chili", 
        "Meatball Sub", 
        "Chicken Tikka Masala", 
        "Shrimp Scampi", 
        "Pork Schnitzel", 
        "BBQ Ribs", 
        "Chicken Pot Pie", 
        "Beef Burritos"
    ],
    'ingredients': [
        "spaghetti, ground beef, tomato sauce, onions, garlic", 
        "flour, sugar, butter, chocolate chips", 
        "romaine lettuce, croutons, parmesan cheese, Caesar dressing", 
        "spaghetti, potato",
        "carrot, bell pepper, broccoli, soy sauce, garlic, ginger", 
        "chicken breast, heavy cream, garlic, parmesan cheese, fettuccine", 
        "bread, cheese, butter", 
        "flour, sugar, eggs, milk, baking powder", 
        "ground beef, taco shells, lettuce, tomato, cheese, sour cream", 
        "tomatoes, onions, garlic, vegetable broth, basil", 
        "black beans, lentils, breadcrumbs, lettuce, tomato, onion", 
        "lemon, sugar, eggs, meringue, pie crust",
        "chicken breast, romaine lettuce, Caesar dressing, flour tortilla", 
        "mushrooms, rice, vegetable broth, parmesan cheese, garlic", 
        "pork shoulder, barbecue sauce, hamburger buns, pickles", 
        "apples, sugar, flour, cinnamon, pie crust",
        "chicken breast, soy sauce, broccoli, bell pepper, garlic", 
        "canned tuna, lettuce, mayo, pickles, onion", 
        "rice, vegetables, soy sauce, garlic, egg", 
        "beef, potatoes, carrots, onions, beef broth", 
        "chicken wings, garlic, soy sauce, honey, chili flakes", 
        "salmon fillet, lemon, garlic, olive oil", 
        "ground beef, tomato sauce, lasagna noodles, mozzarella cheese", 
        "beans, tomatoes, onion, garlic, chili powder", 
        "ground beef, sub rolls, marinara sauce, mozzarella cheese", 
        "chicken, yogurt, spices, tomato, rice", 
        "shrimp, garlic, butter, lemon, pasta", 
        "pork, breadcrumbs, eggs, lemon, flour", 
        "pork ribs, barbecue sauce, garlic, brown sugar", 
        "chicken, vegetables, pie crust, heavy cream", 
        "ground beef, tortillas, beans, cheese, salsa"
    ],
    'description': [
        "A classic Italian pasta dish with a rich meat sauce.",
        "Delicious cookies with melted chocolate chips.",
        "A fresh salad with crunchy croutons and creamy dressing.",
        "A Tunisian twist on the traditional spaghetti.",
        "A quick and healthy stir fry with colorful vegetables.",
        "Creamy pasta with tender chicken and parmesan.",
        "A warm and comforting sandwich with melted cheese.",
        "Fluffy, golden pancakes perfect for breakfast.",
        "Tasty tacos with seasoned beef and fresh toppings.",
        "A hearty, comforting soup made with fresh tomatoes.",
        "A savory vegetarian burger with black beans and lentils.",
        "A tangy and sweet lemon pie with a fluffy meringue.",
        "A wrap with chicken, Caesar dressing, and crisp lettuce.",
        "A creamy rice dish with earthy mushrooms and parmesan.",
        "Slow-cooked pulled pork served on soft buns with pickles.",
        "A sweet, spiced pie made with fresh apples.",
        "A stir fry with tender chicken and colorful vegetables.",
        "A refreshing salad with tuna, lettuce, and mayo.",
        "A flavorful fried rice dish with veggies and egg.",
        "A rich beef stew with potatoes and carrots.",
        "Crispy chicken wings with a sweet and spicy glaze.",
        "A simple and delicious salmon fillet with garlic and lemon.",
        "A comforting lasagna with layers of beef and cheese.",
        "A hearty chili with beans and a spicy kick.",
        "A sub sandwich with meatballs, marinara, and melted cheese.",
        "A flavorful Indian chicken dish with yogurt and spices.",
        "Shrimp cooked with garlic, butter, and lemon served over pasta.",
        "Crispy breaded pork cutlets served with lemon.",
        "Tender pork ribs coated in a smoky barbecue sauce.",
        "A creamy chicken pie filled with vegetables.",
        "Spicy and savory beef burritos with cheese and salsa."
    ]
}


df = pd.DataFrame(data)
@app.route('/recipes', methods=['POST'])
@app.route('/recipes', methods=['POST'])
@app.route('/recipes', methods=['POST'])
def get_recipes():
    data = request.get_json()
    ingredients = data.get('ingredients', [])

    if not ingredients:
        return jsonify([])  # Return an empty list if no ingredients are provided

    # Convert the ingredients input to lowercase and ensure it’s a set
    ingredients_set = set(ingredient.strip().lower() for ingredient in ingredients)

    # Ensure all specified ingredients are present in the recipe's ingredients
    filtered_recipes = df[df['ingredients'].apply(
        lambda x: all(ingredient in x.lower() for ingredient in ingredients_set)
    )]

    # If no recipes match, return an empty list
    if filtered_recipes.empty:
        return jsonify([])

    # Return the filtered recipes
    return jsonify(filtered_recipes.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

