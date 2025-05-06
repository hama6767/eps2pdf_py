# convert_eps_crop.py  --- EPS → PDF
import subprocess, pathlib

FIG_DIR = pathlib.Path("figures")    
for eps in FIG_DIR.glob("*.eps"):
    pdf = eps.with_suffix(".pdf")
    subprocess.run([
        "gs",
        "-dSAFER", "-dNOPAUSE", "-dBATCH",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",   # arXiv format
        "-dEPSCrop",                  
        f"-sOutputFile={pdf}",
        str(eps)
    ], check=True)
print("Converted all eps file to pdf")
