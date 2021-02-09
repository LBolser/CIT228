def order_sandwich(*ingredients):
    print("\nYour sandwich contains: ")

    for item in ingredients:
        print(item.title())

order_sandwich("manwich")
order_sandwich("cheese", "hamburger")
order_sandwich("bacon","lettuce","tomato")
order_sandwich("salami", "provolone","lettuce", "olives","pickles","ranch dressing")