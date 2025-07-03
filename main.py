import os
import sys
from services.pdf_processor import PDFProcessor
from services.ocr_service import OCRService
from services.file_manager import FileManager

def process_pdf_to_text(pdf_path):
    '''
    Función principal que orquesta todo el proceso
    
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
        
        # Paso 1: Validar el archivo
        print("Validando archivo...")
        file_manager.validate_pdf_file(pdf_path)
        
        # Paso 2: Convertir PDF a imágenes
        print("Convirtiendo PDF a imágenes...")
        images = pdf_processor.pdf_to_images(pdf_path)
        print(f"  -> {len(images)} páginas encontradas")
        
        # Paso 3: Procesar cada página
        print("Extrayendo texto...")
        full_text = ""
        
        for i, image in enumerate(images, 1):
            print(f"  -> Procesando página {i}/{len(images)}")
            page_text = ocr_service.extract_text_from_pil_image(image)
            full_text += f"\n--- PáGINA {i} ---\n"
            full_text += page_text + "\n"
            
        # Paso 4: Guardar resultado
        original_name = os.path.basename(pdf_path)
        output_file = file_manager.save_text_to_file(full_text, original_name)
        
        print(f"Proceso completo. Archivo guardado en: {output_file}")
        return output_file
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
if __name__ == "__main__":
    # Test manual - reemplaza con la ruta de un PDF de prueba
    test_pdf = 'test.pdf' # Cambiar por un PDF real
    
    if os.path.exists(test_pdf):
        process_pdf_to_text(test_pdf)
    else:
        print("Coloca un PDF llamada 'test.pdf' en la carpeta del proyecto para probar la app")