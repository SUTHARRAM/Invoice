from django.db import models

class UserDetail(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    cityname = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=20)
    pincode = models.CharField(max_length=255)
    creationdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    lastmodifiedby = models.CharField(max_length=100)
    class Meta:
        # Specify the actual table name
        db_table = 'userdetail'
class ClientDetail(models.Model):
    clientid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=100)
    cityname = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=500)
    pincode = models.CharField(max_length=255)
    creationdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    lastmodifiedby = models.CharField(max_length=100)
    class Meta:
        # Specify the actual table name
        db_table = 'clientdetail'

class BillDetail(models.Model):
    billid = models.AutoField(primary_key=True)
    fkuserid = models.ForeignKey(UserDetail, on_delete=models.CASCADE, db_column='fkuserid')
    fkclientid = models.ForeignKey(ClientDetail, on_delete=models.CASCADE, db_column='fkclientid')
    creationdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    lastmodifiedby = models.CharField(max_length=100)
    class Meta:
        # Specify the actual table name
        db_table = 'billdetail'

class ProductDetail(models.Model):
    productid = models.AutoField(primary_key=True)
    fkbillid = models.ForeignKey(BillDetail, on_delete=models.CASCADE, db_column='fkbillid')
    description = models.TextField()
    rate = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    creationdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    lastmodifiedby = models.CharField(max_length=100)
    class Meta:
        # Specify the actual table name
        db_table = 'productdetail'

class PaymentDetail(models.Model):
    paymentid = models.AutoField(primary_key=True)
    fkbillid = models.ForeignKey(BillDetail, on_delete=models.CASCADE, db_column='fkbillid')
    totalamount = models.DecimalField(max_digits=10, decimal_places=2)
    totalpaid = models.DecimalField(max_digits=10, decimal_places=2)
    creationdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    lastmodifiedby = models.CharField(max_length=100)
    class Meta:
        # Specify the actual table name
        db_table = 'paymentdetail'
