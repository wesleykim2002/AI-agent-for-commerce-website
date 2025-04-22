from app import app, db, Product

with app.app_context():
    db.create_all()

    products = [
        Product(name="Shoes", description="Lifestyle shoes for men", price=149.99),
        Product(name="Shirt", description="Cotton shirt", price=19.99),
        Product(name="TV", description="Smart TV", price=1299.99),
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()
    print("Database initialized with sample products.")