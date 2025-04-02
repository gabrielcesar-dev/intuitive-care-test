import pandas as pd
import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Operadora

class LoadCSVData(APIView):
    """
    Load data from CSV file into the database
    """
    def post(self, request):
        try:
            csv_path = os.path.join(settings.BASE_DIR, 'operators_data.csv')
            
            if not os.path.exists(csv_path):
                return Response({
                    "error": f"CSV file not found at {csv_path}"
                }, status=status.HTTP_404_NOT_FOUND)
            
            encoding = 'utf-8'
            delimiter = ';'
            
            df = pd.read_csv(csv_path, sep=delimiter, encoding=encoding, quotechar='"')
            
            if df is None:
                return Response({
                    "error": "Could not read CSV file with any of the tried encodings and delimiters"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            
            # Normalize column names
            df.columns = [col.upper().replace('_', '') for col in df.columns]
            
            # Map CSV columns to model fields (case-insensitive without underscores)
            field_mapping = {
                'REGISTROANS': 'registro_ans',
                'CNPJ': 'cnpj',
                'RAZAOSOCIAL': 'razao_social',
                'NOMEFANTASIA': 'nome_fantasia',
                'MODALIDADE': 'modalidade',
                'LOGRADOURO': 'logradouro',
                'NUMERO': 'numero',
                'COMPLEMENTO': 'complemento',
                'BAIRRO': 'bairro',
                'CIDADE': 'cidade',
                'UF': 'uf',
                'CEP': 'cep',
                'DDD': 'ddd',
                'TELEFONE': 'telefone',
                'FAX': 'fax',
                'ENDERECOELETRONICO': 'endereco_eletronico',
                'EMAIL': 'endereco_eletronico',
                'REPRESENTANTE': 'representante',
                'CARGOREPRESENTANTE': 'cargo_representante',
                'REGIAOCOMERCIALIZACAO': 'regiao_de_comercializacao', 
                'REGISTRODECOMERCIALIZACAO': 'regiao_de_comercializacao',
                'DATAREGISTROANS': 'data_registro_ans'
            }
            
            # Create a reverse mapping for checking available columns
            available_cols = {col: col for col in df.columns}
            
            if Operadora.objects.exists():
                print("Clearing existing data...")
                Operadora.objects.all().delete()
            
            success_count = 0
            error_count = 0
            error_messages = []
            
            for idx, row in df.iterrows():
                try:
                    data = {field: None for field in field_mapping.values()}
                    
                    for target_field, model_field in field_mapping.items():
                        if target_field in available_cols:
                            data[model_field] = row.get(target_field)
                    
                    # Date format
                    if data['data_registro_ans'] is not None and pd.notna(data['data_registro_ans']):
                        try:
                            for fmt in ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y']:
                                try:
                                    data['data_registro_ans'] = pd.to_datetime(data['data_registro_ans'], format=fmt).date()
                                    break
                                except:
                                    continue
                        except:
                            data['data_registro_ans'] = None
                    
                    # region_comercializacao as integer
                    if data['regiao_de_comercializacao'] is not None and pd.notna(data['regiao_de_comercializacao']):
                        try:
                            data['regiao_de_comercializacao'] = int(data['regiao_de_comercializacao'])
                        except:
                            data['regiao_de_comercializacao'] = None
                    
                    # Skip rows without registro_ans
                    if not data['registro_ans'] or pd.isna(data['registro_ans']):
                        error_count += 1
                        error_messages.append(f"Row {idx+1}: Missing required REGISTRO_ANS")
                        continue
                    
                    obj, created = Operadora.objects.update_or_create(
                        registro_ans=data['registro_ans'],
                        defaults={k: v for k, v in data.items() if k != 'registro_ans'}
                    )
                    success_count += 1
                    
                except Exception as row_error:
                    error_count += 1
                    error_messages.append(f"Row {idx+1}: {str(row_error)}")
            
            return Response({
                "message": f"Processed {len(df)} rows: {success_count} successful, {error_count} errors",
                "errors": error_messages[:10] if error_messages else []
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            import traceback
            return Response({
                "error": str(e),
                "traceback": traceback.format_exc()
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchOperators(APIView):
    """
    Search for operators based on text input
    """
    def get(self, request):
        search_query = request.query_params.get('q', '')
        
        if not search_query:
            return Response({"error": "Please provide a search query parameter 'q'"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Search in relevant fields
        operators = Operadora.objects.filter(
            Q(registro_ans__icontains=search_query) |
            Q(cnpj__icontains=search_query) |
            Q(razao_social__icontains=search_query) |
            Q(nome_fantasia__icontains=search_query) |
            Q(modalidade__icontains=search_query) |
            Q(cidade__icontains=search_query) |
            Q(uf__icontains=search_query)
        )
        
        # Convert queryset to list of dictionaries
        results = []
        for op in operators:
            results.append({
                'registro_ans': op.registro_ans,
                'cnpj': op.cnpj,
                'razao_social': op.razao_social,
                'nome_fantasia': op.nome_fantasia,
                'modalidade': op.modalidade,
                'cidade': op.cidade,
                'uf': op.uf,
                'endereco_eletronico': op.endereco_eletronico,
                'telefone': op.telefone,
                'regiao_de_comercializacao': op.regiao_de_comercializacao,
            })
        
        return Response({
            "count": len(results),
            "results": results
        }, status=status.HTTP_200_OK)