from pdf2image import convert_from_path
import os

class PDFProcessor:
    def __init__(self):
        self.poppler_path = r'C:\poppler-windows\poppler-24.08.0\Library\bin'
        pass
    
    def pdf_to_images(self, pdf_path):
        '''
        Convierte PDF en lista de imágenes PIL
        
        Args:
            pdf_path (str): Ruta al archivo PDF
            
        Returns:
            list: Lista de imágenes PIL
        '''
        
        try:
            images = convert_from_path(
                pdf_path,
                dpi = 300,
                poppler_path = self.poppler_path
            )
            
            return images
        
        except Exception as e:
            raise Exception(f"Error procesando el PDF: {str(e)}")