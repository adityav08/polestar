from polestar import app, initialize_db
import os

if __name__ == '__main__':
    postgres_user = os.getenv('POSTGRES_USER', 'postgres')
    postgres_password = os.getenv('POSTGRES_PASSWORD', 'password')
    postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
    postgres_port = os.getenv('POSTGRES_PORT', '5433')
    postgres_db = os.getenv('POSTGRES_DB', 'polestar')
    try:
        initialize_db(postgres_user, postgres_password, postgres_host, postgres_port, postgres_db)
    except Exception as e:
        print(f"Error initializing the database: {e}")

    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true',
            port=os.getenv('APP_PORT', '5001'),
            host=os.getenv('APP_HOST', '127.0.0.1'))