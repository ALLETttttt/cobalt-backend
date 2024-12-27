# Views
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from app.models import Product, Category, Offer

from django.middleware.csrf import get_token
from django.http import HttpRequest

request = HttpRequest()
csrf_token = get_token(request)


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        data = [{
            'id': product.id,
            'name': product.product_name,
            'price': product.product_price,
            'old_price': product.product_old_price,
            'image': product.product_image,
            'discount': product.product_discount,
            'rating': product.product_rating,
            'description': product.product_description,
            'is_liked': product.product_is_liked,
            'category': product.category.name
        } for product in products]
        return JsonResponse(data, safe=False)


class LikedProductListView(View):
    def get(self, request):
        products = Product.objects.filter(product_is_liked=True)
        data = [{
            'id': product.id,
            'name': product.product_name,
            'price': product.product_price,
            'old_price': product.product_old_price,
            'image': product.product_image,
            'discount': product.product_discount,
            'rating': product.product_rating,
            'description': product.product_description,
            'is_liked': product.product_is_liked,
            'category': product.category.name
        } for product in products]
        return JsonResponse(data, safe=False)


class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        data = {
            'id': product.id,
            'name': product.product_name,
            'price': product.product_price,
            'old_price': product.product_old_price,
            'image': product.product_image,
            'discount': product.product_discount,
            'rating': product.product_rating,
            'description': product.product_description,
            'is_liked': product.product_is_liked,
            'category': product.category.name,
            'csrf': csrf_token
        }
        return JsonResponse(data)


class ToggleLikeView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.product_is_liked = not product.product_is_liked
        product.save()
        return JsonResponse({'is_liked': product.product_is_liked})


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        data = [{'id': category.id, 'name': category.name} for category in categories]
        return JsonResponse(data, safe=False)


class CategoryProductsView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = category.products.all()
        data = [{
            'id': product.id,
            'name': product.product_name,
            'price': product.product_price,
            'old_price': product.product_old_price,
            'image': product.product_image,
            'discount': product.product_discount,
            'rating': product.product_rating,
            'description': product.product_description,
            'is_liked': product.product_is_liked
        } for product in products]
        return JsonResponse(data, safe=False)


class OfferListView(View):
    def get(self, request):
        # Fetch all offers from the database
        offers = Offer.objects.all()

        # Manually format the data into a list of dictionaries
        offers_list = [
            {
                "hours": offer.hours,
                "minutes": offer.minutes,
                "seconds": offer.seconds,
                "description_text": offer.description_text,
                "image_name": offer.image_name,
                "percent": offer.percent,
                "countdown": offer.countdown
            }
            for offer in offers
        ]

        # Return as JSON response
        return JsonResponse(offers_list, safe=False)
