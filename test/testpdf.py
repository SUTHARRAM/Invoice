from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Invoice', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_invoice_pdf(invoice_by, invoice_to, items, total_amount, total_paid, total_due):
    pdf = PDF()
    pdf.add_page()
    
    # Header
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Invoice By', 0, 1)
    pdf.cell(0, 10, f"Name: {invoice_by['name']}", 0, 1)
    pdf.cell(0, 10, f"Email: {invoice_by['email']}", 0, 1)
    pdf.cell(0, 10, f"Mobile: {invoice_by['mobile']}", 0, 1)
    pdf.cell(0, 10, f"Pin Code: {invoice_by['pin_code']}", 0, 1)

    pdf.cell(0, 10, 'Invoice To', 0, 1)
    pdf.cell(0, 10, f"Name: {invoice_to['name']}", 0, 1)
    pdf.cell(0, 10, f"Email: {invoice_to['email']}", 0, 1)
    pdf.cell(0, 10, f"Mobile: {invoice_to['mobile']}", 0, 1)
    pdf.cell(0, 10, f"Pin Code: {invoice_to['pin_code']}", 0, 1)

    pdf.cell(0, 10, 'Item Descriptions', 0, 1)

    # Items
    for item in items:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(90, 10, item['item_description'], 1, 0)
        pdf.cell(30, 10, f"Rate: {item['rate']}", 1, 0)
        pdf.cell(30, 10, f"Quantity: {item['quantity']}", 1, 0)
        pdf.cell(30, 10, f"Amount: {item['amount']}", 1, 1)

    # Total
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Total Amount: {total_amount}", 0, 1)
    pdf.cell(0, 10, f"Total Paid: {total_paid}", 0, 1)
    pdf.cell(0, 10, f"Total Due: {total_due}", 0, 1)

    pdf.output("invoice.pdf")

# Example data
invoice_by = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'mobile': '1234567890',
    'pin_code': '12345'
}

invoice_to = {
    'name': 'Jane Smith',
    'email': 'jane@example.com',
    'mobile': '9876543210',
    'pin_code': '54321'
}

items = [
    {'item_description': 'Item 1', 'rate': 10, 'quantity': 2, 'amount': 20},
    {'item_description': 'Item 2', 'rate': 20, 'quantity': 1, 'amount': 20}
]

total_amount = 40
total_paid = 20
total_due = 20

# Create the invoice PDF
create_invoice_pdf(invoice_by, invoice_to, items, total_amount, total_paid, total_due)
