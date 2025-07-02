import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def test_tesseract():
    try:
        # If Tesseract isn't in the PATH, use the follow line:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        version = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract is working - Version: {version}")
        return True
    except Exception as e:
        print(f"❌ Error - Tesseract is not working: {e}")
        return False
    
def test_poppler():
    try:
        # Basic test - This test will fail without a PDF file
        convert_from_path("dummy_pdf")
    except Exception as e:
        if "cannot indentify image file" in str(e).lower() or "no such file" in str(e).lower() or " couldn't open file 'dummy_pdf': no error" in str(e).lower():
            print("✅ Poppler is working (expected error without PDF)")
            return True
        else:
            print(f"❌ Error with Poppler: {e}")
            return False
        
if __name__ == "__main__":
    print("Verifying configuration...")
    test_tesseract()
    test_poppler()
    print("Setup completed!")