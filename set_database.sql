--cream inventory table
CREATE TABLE IF NOT EXISTS inventory_table (
    product_id VARCHAR(64) PRIMARY KEY,
    product_code VARCHAR(64),
    product_brand VARCHAR(64),
    product_price FLOAT,
    product_name VARCHAR(100),
    product_quantity INTEGER,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);