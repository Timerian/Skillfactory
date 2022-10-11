CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATETIME NOT NULL,
    time_out DATETIME NOT NULL,
    cost FLOAT NOT NULL,
    pickup INT NOT NULL,

    PRIMARY KEY (order_id),
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
);

CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL,

    PRIMARY KEY (product_id)
);

CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position_ CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,

    PRIMARY KEY (staff_id)
);

CREATE TABLE PRODUCTS_ORDERS (
    product_order_id INT AUTO_INCREMENT NOT NULL,
    amount INT NOT NULL,
    product INT NOT NULL,
    in_order INT NOT NULL,

    PRIMARY KEY (product_order_id),
    FOREIGN KEY (product) REFERENCES PRODUCTS (product_id),
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id)
);