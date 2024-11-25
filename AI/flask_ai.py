from flask import Flask, request, jsonify, render_template_string
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload
from flask_cors import CORS

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)

# Configuration de la connexion à la base Oracle
DATABASE_URI = 'oracle+cx_oracle://system:system@localhost:1521/xe'  # Modifie avec tes informations
engine = create_engine(DATABASE_URI, echo=True)  # 'echo=True' pour les logs SQL

# Configuration de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()

# Modèle de la table 'recipes'
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column('RECIPE_ID', Integer, primary_key=True)
    name = Column('RECIPE_NAME', String(100), nullable=False)
    ingredients = Column('INGREDIENTS', String, nullable=False)
    description = Column('DESCRIPTION', String, nullable=True)

    preparations = relationship("Preparation", back_populates="recipe", order_by="Preparation.step_number")

# Modèle de la table 'preparations'
class Preparation(Base):
    __tablename__ = 'preparations'

    id = Column('STEP_ID', Integer, primary_key=True)
    recipe_id = Column('RECIPE_ID', Integer, ForeignKey('recipes.RECIPE_ID'), nullable=False)
    step_number = Column('STEP_NUMBER', Integer, nullable=False)
    description = Column('INSTRUCTION', String, nullable=False)

    recipe = relationship("Recipe", back_populates="preparations")

# Création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Fonction pour obtenir une session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour afficher les recettes avec leurs étapes de préparation
@app.route('/')
def index():
    try:
        with SessionLocal() as db:
            # Récupérer toutes les recettes de la base de données, y compris les étapes de préparation
            all_recipes = db.query(Recipe).options(joinedload(Recipe.preparations)).all()

        # Vérifier s'il y a des recettes
        if not all_recipes:
            return jsonify({'message': 'Aucune recette trouvée'}), 404

        # Affichage des recettes dans un format HTML simple
        recipes_html = "<h1>Recettes</h1><ul>"
        for recipe in all_recipes:
            recipes_html += f"<li><strong>{recipe.name}</strong><br>Ingrédients: {recipe.ingredients}<br>Description: {recipe.description if recipe.description else 'N/A'}<br>"

            # Affichage des étapes de préparation
            recipes_html += "<h3>Étapes de préparation:</h3><ul>"
            for step in recipe.preparations:
                recipes_html += f"<li>Étape {step.step_number}: {step.description}</li>"
            recipes_html += "</ul></li>"
        
        recipes_html += "</ul>"
        return render_template_string(recipes_html)

    except Exception as e:
        print(f"Erreur : {e}")
        return jsonify({'error': str(e)}), 500

# Endpoint POST pour récupérer des recettes en fonction des ingrédients
@app.route('/recipes', methods=['POST'])
def get_recipes():
    try:
        # Récupérer les données du client
        data = request.get_json()
        print("Données reçues :", data)

        ingredients = data.get('ingredients', [])
        if not ingredients:
            return jsonify({'message': 'Aucun ingrédient fourni'}), 400

        # Normalisation des ingrédients
        ingredients_set = [ingredient.strip().lower() for ingredient in ingredients]
        if any(len(ingredient) == 0 for ingredient in ingredients_set):
            return jsonify({'message': 'Un ingrédient vide a été trouvé'}), 400

        # Construction de la condition SQL pour filtrer les recettes
        from sqlalchemy import or_
        filter_conditions = or_(
            *[Recipe.ingredients.like(f"%{ingredient}%") for ingredient in ingredients_set]
        )

        # Exécuter la requête pour obtenir les recettes filtrées, avec les étapes de préparation
        with SessionLocal() as db:
            filtered_recipes = db.query(Recipe).filter(filter_conditions).options(joinedload(Recipe.preparations)).all()

        # Vérifier les résultats
        if not filtered_recipes:
            return jsonify({'message': 'Aucune recette trouvée'}), 404

        # Préparer la réponse sous forme de liste JSON
        recipes_list = []
        for recipe in filtered_recipes:
            preparations_list = [
                {'step_number': step.step_number, 'description': step.description}
                for step in recipe.preparations
            ]
            recipes_list.append({
                'id': recipe.id,
                'name': recipe.name,
                'ingredients': recipe.ingredients,
                'description': recipe.description,
                'preparations': preparations_list
            })

        return jsonify(recipes_list)

    except Exception as e:
        print(f"Erreur : {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
