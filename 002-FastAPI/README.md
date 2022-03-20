#Basic API Development

Initial Steps (Line 1 to 7 in main.py):

- Import FastAPI.
- Create an app instance.
- Write a path operation decorator (like @app.get("/")).
- Write a path operation function (like def root(): ... above).
- Run the development server (like uvicorn main:app --reload).

Path operations are evaluated in order top to bottom.