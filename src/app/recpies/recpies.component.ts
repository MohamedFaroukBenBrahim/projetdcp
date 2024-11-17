import { Component } from '@angular/core';
import { RecipeService } from '../service/recipe.service';

@Component({
  selector: 'app-recpies',
  templateUrl: './recpies.component.html',
  styleUrl: './recpies.component.scss'
})
export class RecpiesComponent {
  ingredients: string = '';  // Store the user input
  recipes: any[] = [];  // Store the fetched recipes

  constructor(private recipeService: RecipeService) {}

  searchRecipes() {
    if (!this.ingredients) {
      console.log('Please enter some ingredients');
      return;  // Don't proceed if no ingredients are entered
    }
    // Convert ingredients string into an array of individual ingredients
    const ingredientsArray = this.ingredients.split(',').map(ingredient => ingredient.trim());

    console.log('Searching recipes for:', ingredientsArray);
    // Make the API call to get recipes
    this.recipeService.getRecipes(ingredientsArray).subscribe(
      (data: any) => {
        console.log('Recipes received:', data);  // Log data
        this.recipes = data;  // Store the recipes in the component
      },
      (error: any) => {
        console.error('Error fetching recipes:', error);
      }
    );
  }
 
  }  