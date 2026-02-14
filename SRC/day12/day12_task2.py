# Task 2: Create a bar chart and a line plot using Matplotlib
import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
plt.subplot(1, 2, 1)
plt.bar(categories, sales, color=['blue', 'orange', 'green'])
plt.xlabel('Product Categories')
plt.ylabel('Sales')
plt.title('Sales by Product Category')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales_trend = [200, 250, 300, 350, 400]
plt.subplot(1, 2, 2)
plt.plot(months, sales_trend, marker='o', color='red')
plt.xlabel('Months')
plt.ylabel('Sales Trend')
plt.title('Monthly Sales Trend')
plt.tight_layout()
plt.show()
