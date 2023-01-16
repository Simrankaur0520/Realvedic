from django.db import models

# Create your models here.
class customer_details(models.Model):
    customer_id = models.TextField()
    customer_name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    Address_line1 = models.TextField()
    Address_line2 = models.TextField()
    city = models.TextField()
    pincode = models.TextField()
    state = models.TextField()
    Country = models.TextField()
    
class Product_data(models.Model):
    Product_id = models.TextField(blank = True)
    Product_name = models.TextField(blank = True)
    category = models.TextField(blank = True)
    image = models.TextField(blank = True)
    prices = models.TextField(blank = True)
    Sizes = models.TextField(blank = True)
    benefits = models.TextField(blank = True)
    ingredients= models.TextField(blank = True)
    how_to_use=models.TextField(blank = True)
    how_we_make_it = models.TextField(blank = True)
    nutrition= models.TextField(blank = True)
    Status = models.TextField(blank = True)
    sibling_product=models.TextField(blank = True)
    HSN=models.TextField(blank = True)
    SKU=models.TextField(blank = True)


class order_data(models.Model):
    order_id=models.TextField()
    order_date = models.TextField()
    Customer_id = models.TextField()
    Product_id = models.TextField()
    Total_amount = models.TextField()
