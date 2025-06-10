from typing import List
from fastapi import UploadFile, File
import os
from openai import OpenAI
import json
from dotenv import load_dotenv
import PyPDF2
import io

load_dotenv()

class DoctorServices:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.system_prompt = """
        You are playing two roles: an experienced physician and the physician's assistant. Your task is to analyze medical documents and/or images, provide relevant clinical insights, technical observations, diagnostic hypotheses, and possible recommendations. Base your analysis on medical knowledge and clinical best practices.

Context:

If there is a single document (.txt, .docx, .xlsx, .pdf):
Summarize the main points from the document.
Highlight important clinical information.
Present hypotheses or suspicions with proper reasoning.
Suggest any useful follow-up actions, tests, or treatments for the physician or patient.

If there is a single image:
Identify what the image represents (e.g., X-ray, lab result scan, dermatological photo).
Analyze it visually for abnormalities or key features.
Comment on potential conditions, suggest possible diagnoses, or additional exams if necessary.

If there are multiple documents:
Cross-reference the data across all documents.
Look for correlations, inconsistencies, or relevant trends.
Form hypotheses based on the combined information.
Provide clinical insights and suggest any relevant charts, graphs, or data visualizations.

If there are multiple images:
Compare the images to each other.
Look for patterns, progression, or repeated findings.
Provide your interpretation based on comparative analysis and suggest further diagnostic steps if needed.

Important Notes:
Your responses should be technically sound but clearly written so that any healthcare team member can understand.
Use a professional and objective tone.
When appropriate, categorize your recommendations (e.g., "Suggested Exams," "Possible Diagnoses," "Points of Concern," "Refer to Specialist").

If you need to generate any files (like reports, summaries, or visualizations), please format them as JSON with the following structure:
{
    "analysis": "Your text analysis here",
    "generated_files": [
        {
            "filename": "filename.ext",
            "content": "file content",
            "content_type": "text/plain"
        }
    ]
}

Now, analyze the input data as if you were advising a colleague or recording notes in a medical report.
        """

    async def analyzePatientData(self, files: List[UploadFile] = File(...)):
        try:
            # Lista para armazenar o conteúdo dos arquivos
            file_contents = []
            
            # Lê o conteúdo de cada arquivo
            for file in files:
                content = await file.read()
                
                # Trata diferentes tipos de arquivo
                if file.content_type == "application/pdf":
                    # Processa arquivo PDF
                    pdf_content = ""
                    try:
                        pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
                        for page in pdf_reader.pages:
                            pdf_content += page.extract_text() + "\n"
                        decoded_content = pdf_content
                    except Exception as e:
                        decoded_content = f"[Erro ao processar PDF {file.filename}: {str(e)}]"
                else:
                    # Tenta decodificar como texto
                    try:
                        decoded_content = content.decode('utf-8')
                    except UnicodeDecodeError:
                        decoded_content = f"[Conteúdo binário do arquivo: {file.filename}]"
                
                file_contents.append({
                    "filename": file.filename,
                    "content": decoded_content,
                    "content_type": file.content_type
                })
            
            # Prepara o prompt com o conteúdo dos arquivos
            user_prompt = "Analise os seguintes documentos médicos:\n\n"
            for file in file_contents:
                user_prompt += f"Arquivo: {file['filename']}\nTipo: {file['content_type']}\nConteúdo:\n{file['content']}\n\n"
            
            # Faz a chamada para a OpenAI
            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            
            # Extrai a análise da resposta
            analysis = response.choices[0].message.content
            
            # Tenta parsear a resposta como JSON para verificar se há arquivos gerados
            try:
                response_data = json.loads(analysis)
                if isinstance(response_data, dict):
                    return {
                        "message": "Análise realizada com sucesso",
                        "analysis": response_data.get("analysis", analysis),
                        "files_processed": [{"filename": f["filename"], "content_type": f["content_type"]} for f in file_contents],
                        "generated_files": response_data.get("generated_files", [])
                    }
            except json.JSONDecodeError:
                return {
                    "message": "Análise realizada com sucesso",
                    "analysis": analysis,
                    "files_processed": [{"filename": f["filename"], "content_type": f["content_type"]} for f in file_contents],
                    "generated_files": []
                }
            
        except Exception as e:
            raise Exception(f"Erro ao analisar documentos: {str(e)}")
        