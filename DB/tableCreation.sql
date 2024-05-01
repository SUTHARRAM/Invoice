-- Create UserDetail Table
CREATE TABLE UserDetail (
    UserID SERIAL PRIMARY KEY,
    UserName VARCHAR(100),
    Email VARCHAR(255),
    CityName VARCHAR(255),
    MobileNumber VARCHAR(20),
    PinCode VARCHAR(255),
    CreationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedBy VARCHAR(100)
);

-- Create ClientDetail Table
CREATE TABLE ClientDetail (
    ClientID SERIAL PRIMARY KEY,
    ClientName VARCHAR(100),
    CityName VARCHAR(255),
    MobileNumber VARCHAR(500),
    PinCode VARCHAR(255),
    CreationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedBy VARCHAR(100)
);

-- Create table for Bill Detail

CREATE TABLE BillDetail (
    BillID SERIAL PRIMARY KEY,
    FkUserID INT    REFERENCES UserDetail(UserID),
    FkClientID INT  REFERENCES ClientDetail(ClientID),
    CreationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedBy VARCHAR(100)
);

-- Create ProductDetail Table
CREATE TABLE ProductDetail (
    ProductID SERIAL PRIMARY KEY,
    FkBillID INT REFERENCES BillDetail(BillID),
    Description TEXT,
    Rate VARCHAR(255),
    Price NUMERIC(10,2),
    Quantity INT,
    CreationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedBy VARCHAR(100)
);

CREATE TABLE PaymentDetail(
    PaymentID SERIAL PRIMARY KEY, 
    FkBillID INT REFERENCES BillDetail(BillID),
    TotalAmount NUMERIC(10,2),
    TotalPaid NUMERIC(10,2),
    CreationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LastModifiedBy VARCHAR(100)
);
