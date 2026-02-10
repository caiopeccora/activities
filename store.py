store = []
total_price = 0

quantity_products = int(input("How many products do you want to register? "))

for _ in range(quantity_products):
    product = {}
    product["id"] = int(input("Enter the product ID: "))
    product["name"] = input("Enter the product name: ")
    product["price"] = float(input("Enter the product price: "))
    product["stock"] = int(input("Enter the product stock: "))
    
   
    store.append(product)
   
answer = input("Do you want to remove a product? (yes/no): ")

if answer.lower() == "yes":
    id = int(input("Enter the id of the product to remove: "))

    for product in store:
        if product["id"] == id:
            store.remove(product)
            print("Product removed!")
            break
        else:
            print("No product removed.")
     
for product in store:
     total_price += product["price"] * product["stock"]

     print("\nRegistered product data:")
     print(
        f"\nName: {product['name']}, "
        f"\nPrice: ${product['price']:.2f}, "
        f"\nStock: {product['stock']}"
    )
print("\nProducts in the store:", [product["name"] for product in store])
print(f"Total price of all products: ${total_price:.2f}")