-- Insert dummy data into UserDetail table
INSERT INTO UserDetail (UserName, Email, CityName, MobileNumber, PinCode, LastModifiedBy)
VALUES
    ('John Doe', 'john.doe@example.com', 'New York', '1234567890', '10001', 'Admin'),
    ('Jane Smith', 'jane.smith@example.com', 'Los Angeles', '9876543210', '90001', 'Admin'),
    ('Michael Johnson', 'michael.johnson@example.com', 'Chicago', '5551234567', '60601', 'Admin'),
    ('Emily Davis', 'emily.davis@example.com', 'Houston', '7779876543', '77001', 'Admin'),
    ('William Brown', 'william.brown@example.com', 'San Francisco', '9995551234', '94101', 'Admin');

-- Insert dummy data into ClientDetail table
INSERT INTO ClientDetail (ClientName, CityName, MobileNumber, PinCode, LastModifiedBy)
VALUES
    ('ACME Corporation', 'New York', '1234567890', '10001', 'Admin'),
    ('XYZ Enterprises', 'Los Angeles', '9876543210', '90001', 'Admin'),
    ('ABC Industries', 'Chicago', '5551234567', '60601', 'Admin'),
    ('LMN Corporation', 'Houston', '7779876543', '77001', 'Admin'),
    ('PQR Limited', 'San Francisco', '9995551234', '94101', 'Admin');

-- Insert dummy data into BillDetail table
INSERT INTO BillDetail (FkUserID, FkClientID, LastModifiedBy)
VALUES
    (1, 1, 'Admin'),
    (2, 2, 'Admin'),
    (3, 3, 'Admin'),
    (4, 4, 'Admin'),
    (5, 5, 'Admin');

-- Insert dummy data into ProductDetail table
INSERT INTO ProductDetail (FkBillID, Description, Rate, Price, Quantity, LastModifiedBy)
VALUES
    (1, 'Product 1', '10.00', 10.00, 2, 'Admin'),
    (1, 'Product 2', '15.00', 15.00, 3, 'Admin'),
    (2, 'Product 3', '20.00', 20.00, 1, 'Admin'),
    (3, 'Product 4', '25.00', 25.00, 4, 'Admin'),
    (4, 'Product 5', '30.00', 30.00, 5, 'Admin');

-- Insert dummy data into PaymentDetail table
INSERT INTO PaymentDetail (FkBillID, TotalAmount, TotalPaid, LastModifiedBy)
VALUES
    (1, 50.00, 50.00, 'Admin'),
    (2, 40.00, 40.00, 'Admin'),
    (3, 60.00, 60.00, 'Admin'),
    (4, 70.00, 70.00, 'Admin'),
    (5, 80.00, 80.00, 'Admin');
