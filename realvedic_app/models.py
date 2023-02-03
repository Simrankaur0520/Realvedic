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
    
    title = models.TextField(blank = True)
    category = models.TextField(blank = True)
    image = models.FileField(blank=True)
    price = models.TextField(blank = True)
    size = models.TextField(blank = True)
    benefits = models.TextField(blank = True)
    ingredients= models.TextField(blank = True)
    how_to_use=models.TextField(blank = True)
    how_we_make_it = models.TextField(blank = True)
    nutrition= models.TextField(blank = True)
    Status = models.TextField(blank = True)
    sibling_product=models.TextField(blank = True)
    HSN=models.TextField(blank = True)
    SKU=models.TextField(blank = True)

class categoryy(models.Model):
    category=models.TextField()
    category_colour=models.TextField()
    category_image=models.ImageField(upload_to='images/')

class order_data(models.Model):
    order_id=models.TextField()
    order_date = models.TextField()
    Customer_id = models.TextField()
    Product_id = models.TextField()
    Total_amount = models.TextField()

class images_and_banners(models.Model):
    title=models.TextField()
    image=models.ImageField()

class blogs(models.Model):
    image=models.ImageField()
    title=models.TextField()
    content=models.TextField()
    Points=models.TextField(blank=True)

#-------------------------------------------------user side models--------------------------------------

class user_cart(models.Model):
    user_id = models.TextField()
    product_id = models.TextField()
    size = models.TextField()
    price_per_unit=models.TextField(blank=True)
    quantity = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

class user_data(models.Model):
    first_name = models.TextField()
    last_name = models.TextField(blank=True)
    email = models.TextField()
    gender = models.TextField()
    dob = models.TextField()
    phone_code = models.TextField()
    phone_no = models.TextField()
    password = models.TextField()
    token = models.TextField()

class user_address(models.Model):
    user_id = models.TextField()
    add_line_1 = models.TextField()
    add_line_2 = models.TextField(null=True,blank=True)
    landmark = models.TextField(null=True,blank=True)
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()
    pincode = models.TextField()
    phone_no = models.TextField()













