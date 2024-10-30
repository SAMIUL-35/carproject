from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from .models import CarModel
from comments.forms import CommentForm

class detail_View(DetailView):  
    model = CarModel
    template_name = "detail.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.object  
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('detail', id=self.object.id) 
        else:
            messages.error(request, 'Failed to add comment. Please try again.')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

@login_required
def buy_car(request, car_id):
    car = CarModel.objects.get(id=car_id)

    if car.quantity > 0:
        car.quantity -= 1
        car.purchased_by = request.user
        car.save()
        messages.success(request, f"You have successfully bought {car.name}!")
    else:
        messages.error(request, "Sorry, this car is out of stock.")

    return redirect('profile')
