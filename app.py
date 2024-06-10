from collabinnovate import create_app

app = create_app()

@app.route('/')
def hello_world():
  return 'Good JOB'

if __name__ == '__main__':
  
  app.run(debug=True)