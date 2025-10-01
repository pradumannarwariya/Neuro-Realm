from flask import Flask

# Initialize the Flask application instance
app = Flask(__name__)

# --- The text content you provided, stored as a multi-line Python string ---
# We use triple quotes (""") to easily define strings that span multiple lines.
JAVASCRIPT_ROADMAP_TEXT = """
<!DOCTYPE html>
<html>
<head>
    <title>The JavaScript Mastery Roadmap</title>
</head>
<body>
    <h1>The JavaScript Mastery Roadmap: A Structured Curriculum for the Absolute Non-Coder</h1>
    
    <pre>
I. Module 1: Laying the Groundwork (Zero-Barrier Setup and Context)
 1.1. Decoding the Web: The Triad of HTML, CSS, and JavaScript
 Understanding JavaScript begins with defining its role within the ecosystem of the World Wide Web. A modern webpage is constructed using three distinct but interconnected languages: HTML, CSS, and JavaScript.
 HTML (HyperText Markup Language) serves as the foundation, providing the essential structure and meaning to the web content. It functions as the blueprint or skeleton of the page, defining elements such as paragraphs, headings, data tables, or embedded media. Without HTML, the content would be formless. 
 CSS (Cascading Style Sheets) is the language of presentation and design. If HTML dictates what the content is, CSS dictates how it looks. CSS applies style rules, controlling attributes like background colors, fonts, margins, and the layout of elements into columns. 
 JavaScript (JS) is the scripting language that introduces action and interactivity. It is the dynamic layer, responsible for enabling content that updates dynamically, controlling multimedia elements, animating images, and responding to user actions. JavaScript allows the webpage to transition from a static document to a fully interactive application. Establishing this clear conceptual separation—HTML is structure, CSS is style, and JS is action—is critical for the non-coder. It allows the learner to understand JavaScript as the dynamic "action layer" that explicitly operates on the static HTML and CSS elements, thereby defining the crucial concept of separation of concerns required in professional development. 
 1.2. The Zero-Barrier Development Environment
 The first major barrier for new programmers is often the complex setup process. To mitigate this, the initial learning phase should focus entirely on environments that provide immediate feedback with zero installation requirements.
 1.2.1. The Instant Sandbox: Using the Browser Console
 The simplest and quickest way for a non-coder to begin writing and executing JavaScript is directly within their web browser’s developer console. Modern browsers include powerful developer tools that feature a dedicated Console tab, which acts as a text-based interface where commands can be typed and run instantly. This immediate execution and feedback loop are paramount for retaining the beginner’s focus on programming logic rather than tooling complexity. 
 Accessing the Console is uniform across major browsers:
 Google Chrome: Use Ctrl + Shift + J (Windows) or Cmd + Opt + J (Mac).
 Mozilla Firefox: Use Ctrl + Shift + K (Windows) or Cmd + Opt + K (Mac).
 Apple Safari: Use Cmd + Opt + C (Mac). 
 This sandbox allows for instant experimentation with variables, data types, and functions before the learner needs to worry about file systems or embedding code within HTML. 
 1.2.2. Establishing the Professional Environment
 While the console is excellent for isolated exercises, real-world JavaScript is written in dedicated files that interact with HTML. The professional environment requires a code editor, with Visual Studio Code (VSCode) being the widely accepted standard. 
 To transition efficiently, the learner should be guided to create a simple HTML file (index.html) and link a JavaScript file (index.js). A significant point of friction for beginners is the continuous manual process of saving a change and refreshing the browser to see the effect. This repetitive task increases cognitive load and causes frustration, diverting mental energy away from mastering programming concepts.
 To combat this, the inclusion of the Live Server VSCode extension is essential. This extension automatically launches the HTML file on a local server and automatically reloads the browser whenever file changes are detected. By automating this crucial process, the non-coder is allowed to focus their entire mental capacity on understanding JavaScript logic, minimizing early burnout and fostering a more efficient learning trajectory. 
 1.3. Structure and Execution
 JavaScript code is composed of statements, which are individual commands that perform actions. Statements are typically terminated by semicolons, although modern JS often relies on automatic semicolon insertion. Furthermore, documentation is crucial. Comments, ignored by the JavaScript interpreter, allow the programmer to annotate the code using plain language, explaining why and how a section of code works. This practice, using // for single-line comments or /* */ for multi-line comments, reinforces comprehension and communication skills from the start. 
 
II. Module 2: Programming Fundamentals (Conceptual Core)
 2.1. Variables: Containers for Data and References
 The concept of a variable is foundational to programming. For a non-coder, variables are best introduced using the "lunchbox" analogy—a labeled container used to store a specific piece of data. 
 2.1.1. Modern Declarations (let and const)
 Modern JavaScript primarily utilizes two keywords for declaring variables, intentionally sidelining the legacy var keyword. 
 let: Declares a variable whose stored value can be reassigned later. This is used for data that is expected to change, such as a counter or user input.
 const: Declares a constant variable, meaning its reference cannot be reassigned after initialization. This is the default choice for data that should remain consistent throughout the program.
 2.1.2. The Nuance of References and Immutability
 While the lunchbox analogy is helpful for initial comprehension, it must be refined to prevent significant errors later, particularly when dealing with complex data. If a non-coder assumes a variable is a physical box, they may fail to understand why complex data structures declared with const can still be modified, which can lead to bugs. 
 Variables are more accurately conceptualized as references or arrows that point to a location in the computer's memory. 
 If a variable uses const, the arrow itself cannot be reassigned to point to a different location in memory.
 However, if the data block pointed to by the arrow is a complex structure (like an object or array), the contents of that block can still be changed or mutated. The core concept is that immutability relates to the ability to reassign the reference, not necessarily the data within the memory location. Providing this precision early on, rather than letting the simpler "box" model break down later, ensures the learner develops a correct mental model for future object-oriented programming. 
 2.2. Data Types: Recognizing the Building Blocks
 JavaScript programs manipulate values, and every value belongs to a specific data type. JavaScript categorizes types into primitives (simple, singular values) and Objects (complex, structured values). 
 2.2.1. Primitive Data Types
 JavaScript includes seven primitive types, essential for handling basic operations : 
 Number: Used for all numeric values, covering both integers and floating-point decimals. Arithmetic operations are central to this type. 
 String: Used to store textual data, enclosed in quotes. Basic string operations include concatenation and determining length. 
 Boolean: Represents logical states, possessing only two values: true or false. These are fundamental for conditional logic. 
 Undefined: Indicates that a variable has been declared but has not yet been assigned a value. 
 Null: Represents a deliberate non-value or absence of any object value, explicitly set by the programmer. 
 Table 1: JavaScript Primitive Data Types
    </pre>
</body>
</html>
"""

# Define the route for the home page ("/")
@app.route("/")
def home():
  """
  This function serves the entire JavaScript roadmap text as the HTML content 
  for the application's root URL.
  """
  return JAVASCRIPT_ROADMAP_TEXT

# Run the development server
if __name__ == "__main__":
  app.run(debug=True)
