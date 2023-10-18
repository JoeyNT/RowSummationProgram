<body>
    <h1>Row Summation Program</h1>
    <p>This Python program reads a file named <code>numbers.txt</code>, processes each line, calculates the sum of the three integers in each row, and writes the results to <code>output.txt</code>.</p>
    
  <h2>Input File (numbers.txt):</h2>
    <pre>
10 20 23
-7 8 15
0 12 -51
17 -12 -1
    </pre>
<br> You can access the <code>output.txt</code> by clicking the link below:</p>
<a href="https://github.com/JoeyNT/RowSummationProgram/blob/main/numbers.txt" target="input">Download input.txt File</a> 
  <h2>Output File (output.txt):</h2>
    <pre>
63
16
-39
4
    </pre>   
  <h2>Usage:</h2>
    <p>1. Create a file named <code>numbers.txt</code> and populate it with lines, each containing three integers separated by spaces (as shown above).</p>
    <p>2. Run the program.</p>
    <p>3. The program will process the file, calculate the sum of each row, and write the results to <code>output.txt</code>.</p>
    
  <h2>Sample Code:</h2>
    <pre>
import pickle

numbersfile = open('numbers.txt', 'r')
sumfile = open('output.txt', 'w')
for line in numbersfile:
  numberSum = 0
  number = line.split()
  for n in number:
    numberSum += int(n)
  sumfile.write(str(numberSum) + "\n")

numbersfile.close()
sumfile.close()
    </pre>
<br> You can access the <code>rowsummationprogram.py</code> by clicking the link below:</p>
<a href="https://github.com/JoeyNT/RowSummationProgram/blob/main/rowsummationprogram.py" target="sourcecode">Download rowsummationprogram.py File</a>  
    
  <h2>Author:</h2>
    <p>Joey Cuomo (GitHub Username: https://github.com/JoeyNT)</p>

  <h2>License:</h2>
    <p>This program is open-source and available under the MIT License. Feel free to use and modify it as needed.</p>
    
  <h2>Repository:</h2>
    <p>Find the source code and contribute to the project on GitHub: <a href="https://github.com/JoeyNT/RowSummationProgram">GitHub Repository</a></p>
</body>
