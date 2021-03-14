from flask import Flask, render_template,request        # Import libraries

app = Flask(__name__)                                   # Creating Server
app.config["DEBUG"] = True                              # Developer Mode ON


@app.route("/" ,methods = ["GET","POST"])               # Mapping & Allow to take data in get/post form.
def home():                                             # Defining Action
    a = request.args.get("q")                           # Catching data send by user in variable "q" & store it in "a"
                                                        #store this "q" from index.html file

    if a != None:                                       # Check data is provided by user or not, if not return index.html
        iseven = "ODD"                                  # Assign number as odd so that if it is even we dont need else statement and complexity reduces
        a = int(a)                                      # Input is in String format cast it to integer
        if a % 2 == 0:                                  # Condition For ODD EVEN
            iseven = "EVEN"                             # If even then overwrite iseven value to EVEN
        
        return render_template("response.html", falsenum = iseven)   # If the value is provided the generate response from response.html

    return render_template("index.html")                # Load index.html if data not provided and also when page load.

app.run()                                               # Run Server 