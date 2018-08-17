from django.http import JsonResponse


FILM_PRICE = 20000
THEATER_PRICE = 32000
CONCERT_PRICE = 26000


# activate just one slide
def slide_active(slides):
    # check if any of the slides is active
    if slides.count() > 0:      
        active = False
        for slide in slides:
            # if found active slide, make other slides inactive
            if active:
                slide.active = False
                slide.save()
            # if found any active slide, save the state
            if slide.active:
                active = True

        # if no slide is active, make the first one active
        if not active:
            slide = slides[0]
            slide.active = True
            slide.save()


# we need to calculate each element's price by row
# we add 20% to ticket's price for the first row
# and add 10% to ticket's price for the second row
# third row 0% (original ticket's price, no changes)
def calculate_price_by_row(price, row):
    # add 20% to ticket price if row is 1
    if row == 1:
        return price + (price / 100) * 20
    
    # add 10% to ticket price if row is 2
    elif row == 2:
        return price + (price / 100) * 10

    # row 3 is already set
    return price


# this function gets a request and figures out the ticket type and the row
# then calculate ticket's price and send its response as json
# this function is called from within the buy ticket page with jquery request
def calculate_price(request):
    item_type = request.GET.get('type')
    row = int(request.GET.get('row'))
    
    if item_type == 'film':
        price = FILM_PRICE
    elif item_type == 'theater':
        price = THEATER_PRICE
    elif item_type == 'concert':
        price = CONCERT_PRICE
    else:
        price = 0

    price = calculate_price_by_row(price, row)
    data = {'price': price}
    return JsonResponse(data)
