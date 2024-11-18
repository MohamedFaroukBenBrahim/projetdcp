import streamlit as st
import pandas as pd

st.title("INGrecipe")
st.write("Enter ingredients you have, and we’ll suggest recipes just for you")

# Sample recipe data
data = {
    'recipe_id': [1, 2, 3, 4],
    'recipe_name': ["Spaghetti Bolognese", "Chocolate Chip Cookies", "Caesar Salad", "Spaghetti Tounsia"],
    'ingredients': [
        "spaghetti, ground beef, tomato sauce, onions, garlic",
        "flour, sugar, butter, chocolate chips",
        "romaine lettuce, croutons, parmesan cheese, Caesar dressing",
        "spaghetti, potato"
    ]
}
df = pd.DataFrame(data)

def find_recipes(ingredients_list):
    ingredients_set = set(ingredient.strip().lower() for ingredient in ingredients_list.split(","))
    filtered_recipes = df[df['ingredients'].apply(
        lambda x: ingredients_set.issubset(set(x.lower().split(",")))
    )]
    return filtered_recipes

ingredients = st.text_input("Enter ingredients (comma-separated):")

if st.button("Find Recipes"):
    recipes = find_recipes(ingredients)
    if not recipes.empty:
        for idx, row in recipes.iterrows():
            st.subheader(row['recipe_name'])
            st.write("Ingredients:", row['ingredients'])
            st.write("----")
    else:
        st.write("No recipes found with the given ingredients.")
