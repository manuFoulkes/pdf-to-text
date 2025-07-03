import os
from datetime import datetime

class FileManager:
    def __init__(self):
        self.output_folder = "output"
        self._create_output_folder()
        
    def _create_output_folder(self):
        """Crea la carpeta output si la misma no existe"""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            
    def save_text_to_file(self, text, original_pdf_name):
        """
        Guarda el texto extraído en un archivo .txt
        
        Args:
            text (str): Texto a guardar
            original_pdf_name (str): Nombre del PDF original
            
            
        Returns:
            str: Ruta del archivo creado
        """
        try:
            # Generar nombre único
            base_name = os.path.splitext(original_pdf_name)[0] # Sin extensión
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{base_name}_{timestamp}.txt"
            filepath = os.path.join(self.output_folder, filename)
            
            # Escribir archivo
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
                
            return filepath
        
        except Exception as e:
            raise Exception(f"Error guardando archivo: {str(e)}")
        
    def validate_pdf_file(self, filepath):
        """
        Valida que el archivo sea PDF y exista
        
        Args: 
            filepath (str): Ruta al archivo
            
        Returns:
            bool: True si es válido
        """
        if not os.path.exists(filepath):
            raise Exception(f"El archivo no existe: {filepath}")
        
        if not filepath.lower().endswith('.pdf'):
            raise Exception("El archivo debe ser un PDF")
        
        return True