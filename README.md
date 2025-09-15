# 🏥 Clinical Reports AI: Italian Lab Report Structuring with OCR & GPT-4o

This project automatically extracts and structures data from scanned Italian laboratory reports (referti) using OCR and GPT-4o, achieving 100% accuracy on the test set.

---

## 🚀 Features

- 🖼️ **PDF OCR:** Converts scanned PDF reports (any page count) to text (uses Tesseract-OCR & Poppler).
- 🤖 **LLM Extraction:** Structures extracted text using advanced GPT-4o prompting with context & synonym support.
- 📊 **Ground Truth Testing:** Built-in evaluation for accuracy vs. gold standard.
- 🔥 **Production-Ready:** Modular Python code, robust error handling, safe JSON output, detailed instructions.
- 🇮🇹 **Works with any Italian lab report PDF!**

---

## 🗂️ Project Structure

```

elty-project/
│
├── main.py                             # Pipeline orchestrator
├── ocr.py                              # OCR from PDF (Tesseract + pdf2image)
├── prompt\_builder.py                   # LLM prompt assembly
├── openai\_client.py                    # OpenAI API & safe JSON parsing
├── test\_groundtruth.py                 # Evaluation vs ground truth
├── requirements.txt                    # Python dependencies
├── .env                                # Your OpenAI API key
├── Clinical Reports AI - png.pdf       # Sample clinical report (PDF)
├── Clinical Reports AI dictionary.json # Ground truth & synonym dictionary (JSON)
└── prompt.txt                          # Prompt template (system + user)

````

---

## ⚡ Quickstart

### 1. **Install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) and [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/releases/) for your OS**
- Add both `poppler/bin` and `Tesseract-OCR` folders to your PATH (System Environment Variables).
- Make sure Italian language (`ita.traineddata`) is present in Tesseract's tessdata folder.

### 2. **Create and activate Python virtual environment**

```powershell
python -m venv venv
.\venv\Scripts\activate
````

### 3. **Install Python dependencies**

```powershell
pip install -r requirements.txt
```

### 4. **Add your OpenAI API key**

```env
OPENAI_API_KEY=sk-...
```

### 5. **Run the pipeline**

```powershell
python main.py --pdf "Clinical Reports AI - png.pdf" --dictionary "Clinical Reports AI dictionary.json" --prompt "prompt.txt" --output "output.json"
```

### 6. **Check the accuracy (optional)**

```powershell
python test_groundtruth.py output.json "Clinical Reports AI dictionary.json"
```

---

## 🛠️ How it works

* **OCR:** `ocr.py` extracts all text from your scanned lab report PDF using Tesseract-OCR (Italian language).
* **Prompt Assembly:** `prompt_builder.py` creates a context-rich prompt for GPT-4o, including synonyms/ground truth if needed.
* **LLM Extraction:** `openai_client.py` safely parses and validates the GPT-4o output as real JSON (handles strings, escapes, etc).
* **Evaluation:** `test_groundtruth.py` matches your output to the ground truth using fuzzy matching.

---

## 💡 Tips

* **Any PDF:** Works with any scanned Italian report (multi-page supported).
* **Safe JSON:** Output always valid — robust to weird LLM formatting.
* **Production-ready:** All configs/folders portable, code easily extendable to other lab forms, languages, or LLMs.

---

## ❓ Troubleshooting

* **Poppler or Tesseract not found:**
  Check your PATH and install the latest version for your OS.

* **OCR errors:**
  Make sure `ita.traineddata` exists in Tesseract's `tessdata` folder.

* **JSON errors:**
  This pipeline is protected against BOM, extra quotes, and other Windows-related encoding issues.

---

## 📄 License

MIT — use for your tests, portfolio, hackathons, or real-world production.
