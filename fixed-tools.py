# Fixed tools.py

import os
from dotenv import load_dotenv
load_dotenv()

# Fixed: Removed unused import
from crewai_tools.tools.serper_dev_tool import SerperDevTool
# Fixed: Added missing import for PDF processing
from langchain.document_loaders import PyPDFLoader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool - Fixed: Added self parameters to all methods
class BloodTestReportTool():
    
    def __init__(self):
        """Initialize the BloodTestReportTool"""
        pass
    
    async def read_data_tool(self, path='data/sample.pdf'):  # Fixed: Added self parameter
        """Tool to read data from a pdf file from a path
        
        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.
            
        Returns:
            str: Full Blood Test report file
        """
        try:
            # Fixed: Changed PDFLoader to PyPDFLoader with proper initialization
            docs = PyPDFLoader(file_path=path).load()
            full_report = ""
            
            for data in docs:
                # Clean and format the report data
                content = data.page_content
                # Remove extra whitespaces and format properly
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")
                full_report += content + "\n"
                
            return full_report
        except Exception as e:
            return f"Error reading PDF file: {str(e)}"

## Creating Nutrition Analysis Tool - Fixed: Added self parameters
class NutritionTool:
    
    def __init__(self):
        """Initialize the NutritionTool"""
        pass
    
    async def analyze_nutrition_tool(self, blood_report_data):  # Fixed: Added self parameter
        """Analyze nutrition based on blood report data
        
        Args:
            blood_report_data (str): Blood report data to analyze
            
        Returns:
            str: Nutrition analysis results
        """
        # Process and analyze the blood report data
        processed_data = blood_report_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ": # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
        
        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool - Fixed: Added self parameters
class ExerciseTool:
    
    def __init__(self):
        """Initialize the ExerciseTool"""
        pass
    
    async def create_exercise_plan_tool(self, blood_report_data):  # Fixed: Added self parameter
        """Create exercise plan based on blood report data
        
        Args:
            blood_report_data (str): Blood report data to analyze
            
        Returns:
            str: Exercise plan recommendations
        """
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"