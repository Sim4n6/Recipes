from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe, Ingredient, Direction

def index(request):
    return redirect("home")

def home(request):
    latest_recipes = Recipe.objects.order_by('-pub_date')[:4]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'recipe_app/home.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = Ingredient.objects.filter(recipe__id=recipe_id)
    directions = Direction.objects.filter(recipe__id=recipe_id)
    latest_recipes = Recipe.objects.order_by('-pub_date')[:4]
    context = {"recipe": recipe, "ingredients": ingredients, "directions": directions, "latest_recipes": latest_recipes}
    return render(request, "recipe_app/detail.html", context)