# import weasyprint
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from cart.cart import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm
from django.core.mail import mail_admins
# from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            # set the order in the session
            subject = "Новый заказ #", order.id
            plain_message = "На сайте создан новый заказ под номером #", order.id, " проверьте админку!";
            html_message = "<h3>Новый заказ</h3><p>На сайте создан новый заказ №", order.id, "</p><p>", order.first_name, "</p><p> ",order.last_name, "</p><p>",order.phone,"</p>"
            mail_admins(subject, plain_message, fail_silently=True, html_message=html_message )
            request.session['order_id'] = order.id
            # redirect for payment
            return render(request, 'orders/order/created.html', {'order_id': order.id})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    # weasyprint.HTML(string=html).write_pdf(response,
    #     stylesheets=[weasyprint.CSS(
    #         settings.STATIC_ROOT + 'css/pdf.css')])
    return response