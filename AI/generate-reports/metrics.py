import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
from datetime import datetime
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'DataFrame to PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()


text = "BTC"
x = yf.Ticker(f"{text}")
data = x.get_news()

['title'], ['link']
for item in data:
    item['Date Published'] = datetime.utcfromtimestamp(item['providerPublishTime']).strftime('%Y-%m-%d %H:%M:%S')

# Create DataFrame
df = pd.DataFrame(data)

# Select only the necessary columns
df = df[['Date Published', 'title', 'link', 'publisher']]
df = df.replace('\u2019', "'")
print(df)
# Calculate the maximum width of each column based on the text length
max_width = {
    'Date Published': max([len(str(x)) for x in df['Date Published']]),
    'title': max([len(str(x)) for x in df['title']]),
    'link': max([len(str(x)) for x in df['link']]),
    'publisher': max([len(str(x)) for x in df['publisher']])
}

# Define a scale factor to convert character count to pixel width
scale_factor = 8

fig = go.Figure(data=[
    go.Table(
        header=dict(
            values=list(df.columns),
            align='center',
            fill_color='paleturquoise',
            font=dict(size=12)
        ),
        cells=dict(
            values=[df['Date Published'], df['title'], df['link'], df['publisher']],
            fill_color=[['white', 'lightgrey'] * (df.shape[0] // 2 + 1)],
            align='left',
            height=30,
            font=dict(size=10),  # Adjust font size if needed
            line_color='darkslategray'
        ),
        columnwidth=[
            max_width['Date Published'] * scale_factor,
            max_width['title'] * scale_factor,
            max_width['link'] * scale_factor,
            max_width['publisher'] * scale_factor
        ]  # Set the column widths based on the calculated maximum widths
    )
])

# Adjust layout to ensure columns fit properly
fig.update_layout(
    autosize=False,
    width=sum([max_width[col] * scale_factor for col in df.columns]),  # Total width
    height=400 + 30 * len(df),  # Adjust height dynamically based on the number of rows
    margin=dict(l=0, r=0, t=0, b=0),
)

# Save the figure as an image
fig.write_image(r'C:\\Users\\Utki\Desktop\\code\\blockchain defi project\\AI\\generate-reports\\df_to_pdf.pdf', scale=6)

def add_table_to_pdf(pdf, df):
    pdf.set_font('Arial', '', 10)
    col_widths = [40, 80, 60, 30]  # Column widths
    row_height = 10
    for i, row in df.iterrows():
        if pdf.get_y() + row_height > pdf.h - pdf.b_margin:
            pdf.add_page()
        for idx, text in enumerate(row):
            if idx == 2:  # Handle the 'link' column for wrapping
                pdf.multi_cell(col_widths[idx], row_height, str(text), border=1, ln=3, max_line_height=pdf.font_size)
            else:
                pdf.multi_cell(col_widths[idx], row_height, str(text), border=1, ln=3, max_line_height=pdf.font_size)
        pdf.ln(row_height)

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Add Table
pdf.chapter_title('News Articles')
add_table_to_pdf(pdf, df)