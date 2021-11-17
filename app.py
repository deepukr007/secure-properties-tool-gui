from flask import Flask , request , render_template
import os
app = Flask(__name__)

APP_PATH = os.path.dirname(os.path.abspath(__file__))
JAR_PATH  = os.path.join(APP_PATH,'JAR','secure-properties-tool.jar')

@app.route("/")
def home():
   return render_template('index.html')


@app.route("/encrypt" , methods=['POST'] )
def encrypt():
    command_init = "java -cp " + JAR_PATH +   " com.mulesoft.tools.SecurePropertiesTool"     
    algorithm = request.form.get('algorithm')
    mode = request.form.get('mode')
    key = request.form.get('key')
    value = request.form.get('value')
    command = command_init+ " " + "string " + "encrypt" + " " + algorithm + " " + mode +" " + key + " " + str(value)
    print(command)
    a = os.popen(command)
    a= a.read()
    encrypted = a.strip('\n')                                                                                                                                     
                              
    return(encrypted)
  

@app.route("/decrypt" , methods=['POST'])
def decrypt():
    command_init = "java -cp " + JAR_PATH +   " com.mulesoft.tools.SecurePropertiesTool"                                                  
    algorithm = request.form.get('algorithm')
    mode = request.form.get('mode')
    key = request.form.get('key')
    value = request.form.get('value')
    command = command_init + " " + "string " + "decrypt" + " " + algorithm + " " + mode +" " + key + " " + str(value)
    a = os.popen(command)
    a= a.read()
    decrypted = a.strip('\n')
    return(decrypted)


if __name__ == "__main__":
        app.run()