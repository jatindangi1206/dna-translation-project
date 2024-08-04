## README for DNA Translation Project

### Introduction to DNA Translation
DNA translation is a fundamental process in molecular biology where the genetic code carried by DNA is converted into proteins. The sequence of nucleotides in DNA (adenine [A], thymine [T], guanine [G], and cytosine [C]) is transcribed into RNA (where thymine is replaced by uracil [U]), which is then translated into a sequence of amino acids, the building blocks of proteins. This process is crucial for the synthesis of proteins, which perform a myriad of functions in living organisms.

### How DNA Translation Works
1. **Transcription**: DNA is transcribed into messenger RNA (mRNA) by the enzyme RNA polymerase. In RNA, thymine (T) is replaced by uracil (U).
2. **Translation**: The mRNA is then read by ribosomes in the cell cytoplasm. Transfer RNA (tRNA) molecules bring amino acids to the ribosome in the correct sequence, as dictated by the mRNA codons (a sequence of three nucleotides).
3. **Protein Synthesis**: The ribosome assembles the amino acids into a polypeptide chain, forming a protein.


  
# How to Run the App

#### Prerequisites
- Python 3.x
- Flask
  ```bash - if you do not have these
    pip install python
    pip install flask
    ```
  
- Docker (optional, for containerized setup)



#### Running Locally

1. **Clone the Repository**
    ```bash
    git clone https://github.com/jatindangi1206/dna-translation-project.git
    cd dna-translation
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**
    ```bash
    python app.py
    ```

4. **Access the Application**
    Open your web browser and go to `http://127.0.0.1:5000`.

---
#### Running with Docker

1. **Build the Docker Image**
    ```bash
    docker build -t dna-translation .
    ```

2. **Run the Docker Container**
    ```bash
    docker run -p 5000:5000 dna-translation
    ```

3. **Access the Application**
    Open your web browser and go to `http://127.0.0.1:5000`.

### Usage

1. **Open the Web Application**: Access the application via your web browser at `http://127.0.0.1:5000`.

2. **Enter Your Sequence**:
   - Input the DNA or RNA sequence directly in the text area.
   - Alternatively, upload a FASTA file containing your sequence.

3. **Select the Type**: Choose whether your input sequence is DNA or RNA.

4. **Submit**: Click the "Translate" button to perform the translation.

5. **View Results**: The translated sequence will be displayed on the page.


-------------------------------------------------------------------------

### Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.



### Contact
For any questions or feedback, please contact jatin.dangi_ug24@ashoka.edu.in.

---
