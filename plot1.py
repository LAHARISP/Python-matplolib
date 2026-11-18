# Mini Project: Sales Data Visualization
# Create a DataFrame:
# import pandas as pddata = {    "Product": ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"],    "Sales": [50000, 80000, 30000, 10000, 5000],    "Quantity": [5, 10, 6, 20, 25]}df = pd.DataFrame(data)
#Tasks:
# Display the dataset.
# Find the total sales.
# Find the highest-selling product by sales value.
# Create a bar chart for product-wise sales.
# Create a pie chart showing each product's share of total sales.
# Create a horizontal bar chart for quantity sold.
# Add appropriate titles and axis labels.
# Save the final chart using plt.savefig().

import pandas as pd
import matplotlib.pyplot as plt

data = {    
        "Product": ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"],   
        "Sales": [50000, 80000, 30000, 10000, 5000],    
        "Quantity": [5, 10, 6, 20, 25]
        }
df = pd.DataFrame(data)
# Display the dataset.
print(df)

# Find the total sales.
print("Total sales:",df["Sales"].sum())

# Find the highest-selling product by sales value.
high_sale = df.loc[df["Sales"].idxmax()]
print("Highest-selling product:", high_sale["Product"])
print("Sales value:", high_sale["Sales"])

# Create a bar chart for product-wise sales.
plt.bar(df["Product"], df["Sales"])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product-wise Sales Analysis")
plt.show()

# Create a pie chart showing each product's share of total sales.
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Product-wise Sales Distribution")
plt.show()


# Create a horizontal bar chart for quantity sold.
plt.barh(df["Product"], df["Quantity"])
plt.xlabel("Quantity Sold")
plt.ylabel("Products")
plt.title("Product-wise Quantity Sold")
plt.show()

# # Save the final chart using plt.savefig().
plt.barh(df["Product"], df["Quantity"])
plt.xlabel("Quantity Sold")
plt.ylabel("Products")
plt.title("Product-wise Quantity Sold")
plt.savefig("quantity_sales.png", dpi=300, bbox_inches="tight")
plt.show()