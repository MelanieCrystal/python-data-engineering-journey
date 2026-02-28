# --- VARIABLES & DATA TYPES ---

# Text data (called "string")
company_name = "Informatica"
product = "Axon"

# Whole numbers (called "integer")
employee_count = 5000
year_founded = 1993

# Decimal numbers (called "float")
revenue = 1.5  # in billions

# True/False (called "boolean")
is_public_company = True

# Print everything
print("Company:", company_name)
print("Product:", product)
print("Employees:", employee_count)
print("Founded:", year_founded)
print("Revenue (billions):", revenue)
print("Is Public:", is_public_company)

# Check what TYPE a variable is
print(type(company_name))   # <class 'str'>
print(type(employee_count)) # <class 'int'>
print(type(revenue))        # <class 'float'>
print(type(is_public_company)) # <class 'bool'>


# --- STRING OPERATIONS ---

pipeline_name = "  ETL_Pipeline_Sales_2024  "

# Remove extra spaces (very common when cleaning data)
clean_name = pipeline_name.strip()
print(clean_name)  # ETL_Pipeline_Sales_2024

# Convert to lowercase
print(clean_name.lower())  # etl_pipeline_sales_2024

# Convert to uppercase
print(clean_name.upper())  # ETL_PIPELINE_SALES_2024

# Replace a word
print(clean_name.replace("Sales", "Marketing"))

# Split into parts (very useful for parsing file names)
parts = clean_name.split("_")
print(parts)  # ['ETL', 'Pipeline', 'Sales', '2024']

# Check if something is inside a string
print("Sales" in clean_name)  # True
print("HR" in clean_name)     # False

# f-strings — the cleanest way to build strings (you'll use this constantly)
table_name = "orders"
database = "production_db"
message = f"Loading table '{table_name}' from database '{database}'"
print(message)


