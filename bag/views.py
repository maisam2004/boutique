from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View


# Create your views here.

class ViewBagTemplateView(TemplateView):
    """ a View to return the index page """
    template_name = 'bag/bag.html'


class AddToBagView(View):
    def post(self, request, item_id):
        """ Add a quantity of the specified product to the shopping bag """
        
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        
        bag = request.session.get('bag', {})

       

        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']


        request.session['bag'] = bag

        if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] += quantity
                else:
                    bag[item_id]['items_by_size'][size] = quantity
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
        else:
             if item_id in list(bag.keys()):
                bag[item_id] += quantity
             else:
                bag[item_id] = quantity





        # Print bag contents to console
        print("Current shopping bag contents:", request.session['bag'])
        return redirect(redirect_url)