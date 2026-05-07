import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# BUSINESS SALES ANALYTICS
# -----------------------------

months = ['2023-01','2023-02','2023-03','2023-04',
          '2023-05','2023-06','2023-07','2023-08',
          '2023-09','2023-10','2023-11','2023-12',
          '2024-01','2024-02','2024-03','2024-04',
          '2024-05','2024-06','2024-07','2024-08',
          '2024-09','2024-10','2024-11','2024-12']

revenue = [135000,125000,155000,122000,
           145000,120000,123000,151000,
           150000,120000,161000,130000,
           121000,124000,113000,154000,
           126000,125000,173000,138000,
           126000,135000,115000,140000]

products = ['Laptop Pro','4K Monitor','Tablet X',
            'Smart Watch','Wireless Earbuds',
            'Coffee Table','Ergonomic Chair',
            'Sofa Set','Bookshelf','Standing Desk']

product_revenue = [439000,421000,397000,
                   381000,374000,185000,
                   183000,175000,167000,128000]

regions = ['East','North','South','West']
region_share = [27,29.1,24,19.9]

categories = ['Electronics','Furniture',
              'Clothing','Sports',
              'Food & Beverage']

category_revenue = [2000000,850000,
                    180000,170000,70000]

profit_margin = [22,35,42,38,55]

sales_2023 = [80000,1020000,30000,430000,85000]
sales_2024 = [90000,980000,40000,410000,80000]

quarters = ['2023-Q1','2023-Q2','2023-Q3','2023-Q4',
            '2024-Q1','2024-Q2','2024-Q3','2024-Q4']

electronics = [270000,220000,260000,270000,
               215000,255000,270000,250000]

furniture = [100000,120000,130000,100000,
             90000,105000,120000,95000]

clothing = [20000,25000,22000,23000,
            18000,24000,26000,22000]

sports = [15000,16000,17000,18000,
          20000,19000,21000,17000]

food = [8000,9000,10000,9500,
        8500,9000,10000,9500]

# -----------------------------
# CREATE DASHBOARD
# -----------------------------

fig = plt.figure(figsize=(16,20))
fig.suptitle("Business Sales Performance Analytics\n2023-2024",
             fontsize=28,
             fontweight='bold')

# -----------------------------
# MONTHLY REVENUE TREND
# -----------------------------

ax1 = plt.subplot(4,2,1)

ax1.plot(months, revenue,
         marker='o',
         linewidth=3)

ax1.fill_between(months, revenue, alpha=0.3)

ax1.set_title("Monthly Revenue Trend",
              fontsize=16,
              fontweight='bold')

ax1.set_xticks(months[::2])
ax1.tick_params(axis='x', rotation=45)

ax1.set_ylabel("Revenue")

# -----------------------------
# TOP PRODUCTS
# -----------------------------

ax2 = plt.subplot(4,2,2)

ax2.barh(products, product_revenue)

ax2.set_title("Top 10 Products by Revenue",
              fontsize=16,
              fontweight='bold')

ax2.set_xlabel("Revenue")

# -----------------------------
# REGIONAL SHARE
# -----------------------------

ax3 = plt.subplot(4,2,3)

ax3.pie(region_share,
        labels=regions,
        autopct='%1.1f%%')

ax3.set_title("Regional Revenue Share",
              fontsize=16,
              fontweight='bold')

# -----------------------------
# CATEGORY REVENUE
# -----------------------------

ax4 = plt.subplot(4,2,4)

ax4.bar(categories, category_revenue)

ax4.set_title("Revenue by Category",
              fontsize=16,
              fontweight='bold')

ax4.tick_params(axis='x', rotation=25)

# -----------------------------
# PROFIT MARGIN
# -----------------------------

ax5 = plt.subplot(4,2,5)

ax5.bar(categories, profit_margin)

ax5.set_title("Profit Margin % by Category",
              fontsize=16,
              fontweight='bold')

ax5.set_ylabel("Margin %")

ax5.tick_params(axis='x', rotation=25)

# -----------------------------
# YOY COMPARISON
# -----------------------------

ax6 = plt.subplot(4,2,6)

x = np.arange(len(categories))
width = 0.35

ax6.bar(x - width/2,
        sales_2023,
        width,
        label='2023')

ax6.bar(x + width/2,
        sales_2024,
        width,
        label='2024')

ax6.set_xticks(x)
ax6.set_xticklabels(categories,
                    rotation=20)

ax6.legend()

ax6.set_title("YoY Category Comparison",
              fontsize=16,
              fontweight='bold')

# -----------------------------
# STACKED BAR CHART
# -----------------------------

ax7 = plt.subplot(4,1,4)

ax7.bar(quarters, electronics, label='Electronics')
ax7.bar(quarters, furniture,
        bottom=electronics,
        label='Furniture')

bottom2 = np.array(electronics) + np.array(furniture)

ax7.bar(quarters, clothing,
        bottom=bottom2,
        label='Clothing')

bottom3 = bottom2 + np.array(clothing)

ax7.bar(quarters, sports,
        bottom=bottom3,
        label='Sports')

bottom4 = bottom3 + np.array(sports)

ax7.bar(quarters, food,
        bottom=bottom4,
        label='Food & Beverage')

ax7.set_title("Quarterly Sales by Category (Stacked)",
              fontsize=16,
              fontweight='bold')

ax7.set_xlabel("Quarter")
ax7.set_ylabel("Revenue")

ax7.legend()

# -----------------------------
# LAYOUT
# -----------------------------

plt.tight_layout(rect=[0,0,1,0.97])

# SAVE IMAGE
plt.savefig("business_sales_dashboard.png")

# SHOW OUTPUT
plt.show()