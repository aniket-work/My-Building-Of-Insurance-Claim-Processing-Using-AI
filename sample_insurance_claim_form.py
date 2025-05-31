import fitz
import os

def create_sample_insurance_claim_pdf(output_path):
    """Create a sample insurance claim form as a PDF using PyMuPDF (fitz), with sample values."""
    doc = fitz.open()
    page = doc.new_page(width=595, height=842)  # A4 size in points
    page.insert_text((150, 50), "Sample Insurance Claim Form", fontsize=20, fontname="helv", color=(0, 0, 0))

    # Labels, Y positions, and sample values
    fields = [
        ("Policy Number:", 50, "PN123456789"),
        ("Claimant Name:", 90, "John Doe"),
        ("Date of Birth:", 130, "1990-01-01"),
        ("Contact Number:", 170, "+1 555-123-4567"),
        ("Email Address:", 210, "john.doe@email.com"),
        ("Incident Date:", 250, "2025-05-01"),
        ("Incident Description:", 290, "Car accident at Main St. No injuries. Minor damage to bumper."),
        ("Claim Amount:", 370, "$2,500.00"),
        ("Signature:", 410, "John Doe"),
        ("Date:", 450, "2025-05-30"),
    ]
    for label, y, value in fields:
        page.insert_text((50, y), label, fontsize=12, fontname="helv", color=(0, 0, 0))
        if label != "Incident Description:":
            page.draw_line((200, y + 10), (500, y + 10), color=(0, 0, 0), width=1)
            page.insert_text((210, y), value, fontsize=12, fontname="helv", color=(0.2, 0.2, 0.2))
        else:
            page.draw_rect(fitz.Rect(200, y, 500, y + 60), color=(0, 0, 0), width=1)
            # Wrap description text if needed
            page.insert_textbox(fitz.Rect(210, y + 5, 495, y + 55), value, fontsize=12, fontname="helv", color=(0.2, 0.2, 0.2))

    # Save PDF (remove if exists)
    if os.path.exists(output_path):
        os.remove(output_path)
    doc.save(output_path)
    doc.close()

if __name__ == "__main__":
    create_sample_insurance_claim_pdf("sample_insurance_claim_form.pdf")
    print("PDF created: sample_insurance_claim_form.pdf")
