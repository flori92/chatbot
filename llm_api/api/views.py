import os
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt, download_loader
from rest_framework.decorators import api_view
from rest_framework.response import Response


class AskView(View):
    def get(self, request, *args, **kwargs):
        query_str = request.GET.get('question', None)
        if not query_str:
            return JsonResponse({"error": "Please provide a question."}, status=400)

        # Load the index from disk
        load_dotenv()
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        #index_file_path = os.path.join(settings.BASE_DIR, '')
        index = GPTSimpleVectorIndex.load_from_disk(index_file_path)
        QA_PROMPT_TMPL = (
            "Hello, I have some context information for you:\n"
            "---------------------\n"
            "{context_str}"
            "\n---------------------\n"
            "Based on this context, could you please help me understand the answer to this question: {query_str}?\n"
        )
        QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)
        answer = index.query(query_str, text_qa_template=QA_PROMPT)
        return JsonResponse({'answer': answer.response})

    def post(self, request, *args, **kwargs):
        query_str = request.POST.get('question', None)
        if not query_str:
            return JsonResponse({"error": "Please provide a question."}, status=400)

        # Load the index from disk
        load_dotenv()
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        #do it if your json file will be loading on your disk otherrwise make sure to connect in the link of your dbs
        index_file_path = os.path.join(settings.BASE_DIR, '', '')
        index = GPTSimpleVectorIndex.load_from_disk(index_file_path)
        QA_PROMPT_TMPL = (
            "Hello, I have some context information for you:\n"
            "---------------------\n"
            "{context_str}"
            "\n---------------------\n"
            "Based on this context, could you please help me understand the answer to this question: {query_str}?\n"
        )
        QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)
        answer = index.query(query_str, text_qa_template=QA_PROMPT)
        return JsonResponse({'answer': answer.response})



