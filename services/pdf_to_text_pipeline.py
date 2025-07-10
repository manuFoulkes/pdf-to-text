import os
import sys
from services.pdf_processor import PDFProcessor
from services.ocr_service import OCRService
from services.file_manager import FileManager
from services.spellchecker_service import SpellCheckerService

def process_pdf_to_text(pdf_path):
    '''
    Función principal que orquesta todo el proceso de:
    PDF → imágenes → OCR → corrección → archivo de texto
    
    Args: 
        pdf_path (str): Ruta al PDF
        
    Returns: 
        str: Ruta del archivo de texto generado
    '''
    try:
        print(f"Procesando: {pdf_path}")
        
        # Inicializar servicios
        pdf_processor = PDFProcessor()
        ocr_service = OCRService()
        file_manager = FileManager()
        spellchecker_service = SpellCheckerService()
        
        # Validar el archivo
        print("Validando archivo...")
        file_manager.validate_pdf_file(pdf_path)
        
        # Convertir PDF a imágenes
        print("Convirtiendo PDF a imágenes...")
        images = pdf_processor.pdf_to_images(pdf_path)
        print(f"  -> {len(images)} páginas encontradas")
        
        # Procesar cada página
        print("Extrayendo texto...")
        full_text = ""
        
        for i, image in enumerate(images, 1):
            print(f"  -> Procesando página {i}/{len(images)}")
            page_text = ocr_service.extract_text_from_pil_image(image)
            
            print("Corrigiendo errores de OCR con SpellChecker...")
            corrected_text = spellchecker_service.correct_text(page_text)
            
            full_text += f"\n--- PÁGINA {i} ---\n"
            full_text += corrected_text + "\n"
            
        # Guardar resultado
        original_name = os.path.basename(pdf_path)
        output_file = file_manager.save_text_to_file(full_text, original_name)
        
        print(f"Proceso completo. Archivo guardado en: {output_file}")
        return output_file
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None