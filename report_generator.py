
from fpdf import FPDF

class DietPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'MyDiet_AI: Personalized Nutrition Plan', 0, 1, 'C')
        self.ln(5)

def create_pdf_report(diet_data, macros, output_path='/content/diet_plan.pdf'):
    pdf = DietPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    
    pdf.set_text_color(200, 0, 0)
    pdf.cell(200, 10, txt=f"Condition: {diet_data['condition']}", ln=1)
    
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Daily Nutrient Targets:", ln=1)
    pdf.cell(200, 10, txt=f"- Calories: {macros['calories']} kcal", ln=2)
    pdf.cell(200, 10, txt=f"- Protein: {macros['protein_g']}g | Carbs: {macros['carbs_g']}g | Fats: {macros['fat_g']}g", ln=2)
    
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Diet Plan: {diet_data.get('diet_plan', 'Maintain a balanced diet.')}")
    
    pdf.output(output_path)
    return output_path
