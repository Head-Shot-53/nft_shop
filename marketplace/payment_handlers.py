class PaymentRequest:
    def __init__(self, user, artwork, price):
        self.user = user
        self.artwork = artwork
        self.price = price
        self.is_successful = False
        self.notes = []

# Обробник
class PaymentHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # для зручного ланцюжка

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return request

# Перевірка доступності NFT
class AvailabilityCheckHandler(PaymentHandler):
    def handle(self, request):
        if request.artwork.status == 'sold':
            request.notes.append("NFT вже продано.")
            return request
        return super().handle(request)

# Застосування знижки
class DiscountHandler(PaymentHandler):
    def handle(self, request):
        if request.user.is_authenticated and request.user.username == 'vip_user':
            request.price *= 0.9  # 10% знижка (мб проробити знижки за якісь досягнення)
            request.notes.append("VIP знижка застосована.")
        return super().handle(request)
    
# Логування транзакції
class LoggingHandler(PaymentHandler):
    def handle(self, request):
        print(f"[LOG] Користувач {request.user} оплачує {request.price} за {request.artwork.title}")
        return super().handle(request)

# Завершення оплати
class FinalizePaymentHandler(PaymentHandler):
    def handle(self, request):
        request.artwork.status = 'sold'
        request.artwork.buyer = request.user  
        request.artwork.save()
        request.is_successful = True
        request.notes.append("Оплата успішна.")
        return request
