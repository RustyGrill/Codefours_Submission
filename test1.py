import cv2
import subprocess

image= cv2.imread(r"/Users/sathvik1/projects/Unknown.jpeg")
edges=cv2.Canny(image,threshold1=100,threshold2=250)
cv2.imwrite(r"canny_image.bmp",edges)
print("canny edge generated")
cv2.destroyAllWindows()

input_image_path="/Users/sathvik1/projects/canny_image.bmp"
output_image="final2.eps"
process=subprocess.run(["potrace",input_image_path,"-o",output_image],
               stdout=subprocess.PIPE,
stderr=subprocess.PIPE,universal_newlines=True)
print("eps generated")

def convert_eps_to_pdf(input_eps_file, output_pdf_file):
    try:
        # Run the ps2pdf command to convert EPS to PDF
        subprocess.run(["ps2pdf", input_eps_file, output_pdf_file], check=True)
        print(f"Conversion successful: {input_eps_file} converted to {output_pdf_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Conversion failed: {input_eps_file}")

# Example usage
input_eps_file = "final2.eps"  # Replace with the path to your EPS file
output_pdf_file = "output.pdf"  # Replace with the desired output PDF file path

convert_eps_to_pdf(input_eps_file, output_pdf_file)

def convert_pdf_to_svg(pdf_path, svg_output_path):
    subprocess.run(["pdf2svg", pdf_path, svg_output_path])
# Usage
pdf_path = "output.pdf"
svg_output_path = "output.svg"

# Convert PDF to SVG
convert_pdf_to_svg(pdf_path, svg_output_path)

print("pdf converted to svg")