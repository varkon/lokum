from django.utils.decorators import method_decorator
from liqpay import LiqPay
from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class PayView(TemplateView):
    template_name = 'payment/pay.html'


    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': '100',
            'currency': 'UAH',
            'description': 'Payment for food',
            'order_id': 'order_id_1',
            'version': '3',
            'sandbox': 0,  # sandbox mode, set to 1 to enable it
            'server_url': 'https://lockum.dp.ua/payment/pay-callback/',  # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(TemplateView):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()
