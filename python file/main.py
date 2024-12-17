#sales data (assignment)
import streamlit as st

def read_sales_data(file_path):
    with open(file_path, 'r') as file:
        return [eval(line.strip()) for line in file.readlines() if line.strip()]

def calculate_sale_details(sale):
    gross_amount = sale['quantity'] * sale['price_per_unit']
    discount_amount = gross_amount * sale['discount']
    net_amount = gross_amount - discount_amount
    tax_amount = net_amount * sale['tax_rate']
    final_amount = net_amount + tax_amount

    return {
        'item': sale['item'],
        'quantity': sale['quantity'],
        'gross_amount': gross_amount,
        'discount_amount': discount_amount,
        'net_amount': net_amount,
        'tax_amount': tax_amount,
        'final_amount': final_amount
    }

def generate_report(sales_data):
    sale_details = [calculate_sale_details(sale) for sale in sales_data]
    total_items_sold = sum(sale['quantity'] for sale in sales_data)
    total_discounts = sum(sale['discount_amount'] for sale in sale_details)
    total_taxes = sum(sale['tax_amount'] for sale in sale_details)
    total_sales_amount = sum(sale['final_amount'] for sale in sale_details)

    return sale_details, total_items_sold, total_discounts, total_taxes, total_sales_amount

def main():
    st.title("Sales Data Report")
    uploaded_file = st.file_uploader("Upload sales_data.txt file", type=["txt"])

    if uploaded_file:
        try:
            sales_data = [eval(line.strip()) for line in uploaded_file if line.strip()]
            sale_details, total_items_sold, total_discounts, total_taxes, total_sales_amount = generate_report(sales_data)

            st.subheader("Sales Report")
            for sale in sale_details:
                st.write(f"**Item:** {sale['item']}")
                st.write(f"Quantity Sold: {sale['quantity']}")
                st.write(f"Gross Amount: {sale['gross_amount']:.2f}")
                st.write(f"Discount Amount: {sale['discount_amount']:.2f}")
                st.write(f"Net Amount (After Discount): {sale['net_amount']:.2f}")
                st.write(f"Tax Amount: {sale['tax_amount']:.2f}")
                st.write(f"Final Amount (After Tax): {sale['final_amount']:.2f}")
                st.write("---")

            st.subheader("Summary Report")
            st.write(f"**Total Number of Items Sold:** {total_items_sold}")
            st.write(f"**Total Discounts Given:** {total_discounts:.2f}")
            st.write(f"**Total Taxes Collected:** {total_taxes:.2f}")
            st.write(f"**Total Sales Amount:** {total_sales_amount:.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
