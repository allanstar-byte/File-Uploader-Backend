from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
import os

# class FileUploadView(APIView):
#     parser_class = (FileUploadParser,)

#     def post(self, request, *args, **kwargs):
#         file_obj = request.data['file']
#         # Handle the file object (e.g., save it to disk or process it)
#         return Response({'message': 'File uploaded successfully.'})


from rest_framework import status
from django.core.exceptions import ValidationError

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')

        # Validate file type
        if not file_obj:
            return Response({'message': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)

        valid_extensions = ['.csv', '.xls', '.xlsx']
        file_extension = os.path.splitext(file_obj.name)[1].lower()
        if file_extension not in valid_extensions:
            return Response({'message': 'Invalid file format. Only CSV and Excel files are allowed.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Handle the file object (e.g., save it to disk or process it)
        return Response({'message': 'File uploaded successfully.'})
