import pytesseract
from PIL import Image
import os

class OCRService:
    def __init__(self):
        tesseract_path = os.path.join(os.path.dirname(__file__), '..', 'external', 'tesseract', 'tesseract.exe')
        pytesseract.pytesseract.tesseract_cmd = os.path.abspath(tesseract_path)
        
        self.lang = 'spa+eng'
        
    def extract_text_from_image(self, image_path):
        '''
        Extrae texto de una imagen usando OCR
        
        Args: 
            image_path (str): Ruta a la imagen
            
        Returns:
            str: Texto extraído
        '''
        try:
            # Abrir imagen
            image = Image.open(image_path)
            
            # Aplicar OCR
            text = pytesseract.image_to_string(image, lang=self.lang)
            
            return text.strip()
        
        except Exception as e:
            raise Exception(f"Error en OCR: {str(e)}")
        
    def extract_text_from_pil_image(self, pil_image):
        '''
        Extrae texto de una imagen PIL directamente
        
        Args: 
            pil_image (PIL.Image): Imagen PIL
            
        Returns:
            str: Texto extraído
        '''
        try:
            text = pytesseract.image_to_string(pil_image, lang=self.lang)
            return text.strip()
        except Exception as e:
            raise Exception(f"Error en OCR: {str(e)}")
