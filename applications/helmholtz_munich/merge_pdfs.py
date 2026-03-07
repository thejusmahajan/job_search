from PyPDF2 import PdfMerger
import os

# Set working directory
os.chdir(r'c:\Users\Admin\Documents\application\helmholtz_munich')

# Create merger
merger = PdfMerger()

# Order: Cover Letter, CV, PhD English Certificate, Original Certificates
pdfs = [
    'cover_letter_helmholtz.pdf',
    'cv_helmholtz.pdf',
    'thejus_phd_certificate_english.pdf',
    'thejus_mahajan_cert_phd_master_bachelor.pdf'
]

# Merge PDFs
for pdf in pdfs:
    print(f"Adding: {pdf}")
    merger.append(pdf)

# Output file
output_file = 'Thejus_Mahajan_Application_Helmholtz_Munich.pdf'
merger.write(output_file)
merger.close()

print(f"\nSuccessfully created: {output_file}")
