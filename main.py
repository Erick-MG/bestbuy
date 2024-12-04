from product import Product
from store import Store

def main():
    # Create initial Product instances
    macbook = Product("MacBook Air M2", 1450.0, 100)
    iphone = Product("iPhone 14", 999.0, 50)

    # Create a Store instance
    store = Store()

    # Add products to the store
    store.add_product(macbook)
    store.add_product(iphone)

    # Display all products
    print("Active Products in Store:")
    for product in store.get_all_products():
        print(product.show())

    # Try buying a product
    print("\nBuying 2 MacBook Air M2s...")
    total_cost = store.buy_product("MacBook Air M2", 2)
    print(f"Total cost: ${total_cost:.2f}")

    # Display products after purchase
    print("\nProducts after purchase:")
    for product in store.get_all_products():
        print(product.show())

    # Remove a product
    print("\nRemoving iPhone 14 from store...")
    store.remove_product(iphone)

    # Display products after removal
    print("\nProducts after removal:")
    for product in store.get_all_products():
        print(product.show())

    # Additional functionality for Bose and Mac products
    print("\n--- Additional Product Testing ---")
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # Test buying products
    print(f"Buying 50 Bose Earbuds: ${bose.buy(50):.2f}")  # Purchase 50 Bose Earbuds
    print(f"Buying 100 MacBooks: ${mac.buy(100):.2f}")     # Purchase all MacBooks
    print(f"Is MacBook active? {mac.is_active()}")        # Check if MacBook is still active after purchase

    # Display product details
    print("\nProduct Details:")
    print(bose.show())  # Display Bose details
    print(mac.show())   # Display MacBook details

    # Update quantity and display again
    print("\nRestocking Bose Earbuds...")
    bose.set_quantity(1000)  # Restock Bose Earbuds
    print(bose.show())       # Display updated details

if __name__ == "__main__":
    main()