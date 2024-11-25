import { Component } from '@angular/core';
import { RecipeService } from '../service/recipe.service';

@Component({
  selector: 'app-recpies',
  templateUrl: './recpies.component.html',
  styleUrl: './recpies.component.scss'
})
export class RecpiesComponent {
  ingredients: string = ''; 
  recipes: any[] = [];  
  showPreparationSteps: { [key: number]: boolean } = {};

  constructor(private recipeService: RecipeService) {}
  searchRecipes() {
    if (!this.ingredients) {
      console.log('Please enter some ingredients');
      return;  
    }
    const ingredientsArray = this.ingredients.split(',').map(ingredient => ingredient.trim());
    console.log('Searching recipes for:', ingredientsArray);
    this.recipeService.getRecipes(ingredientsArray).subscribe(
      (data: any) => {
        console.log('Recipes received:', data);  
        this.recipes = data;
      },
      (error: any) => {
        console.error('Error fetching recipes:', error);
      }
      
    );
  }
  togglePreparationSteps(index: number) {
    this.showPreparationSteps[index] = !this.showPreparationSteps[index];
  }
}  