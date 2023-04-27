python -m venv venv # create envcd my-  
Set-ExecutionPolicy Bypass -Scope Process #if cannot start venv
.\venv\Scripts\activate # activate venv
uvicorn main:app --reload 


deactivate # to deactivate venv
