git clone https://github.com/flori92/chatbot.git



1. Install the required packages:
    
```bash
    pip install -r requirements.txt
```

1. Create a `.env` file in the root directory of the project and add your OpenAI API key:

```
OPENAI_API_KEY=This is my api for chatgpt plateform  
```

1. Run migration and start the server:

```bash
    cd llm_api
    python manage.py migrate
    python manage.py runserver
```

1. Run the frontend:

```bash
    cd frontend
    python -m http.server 8080
