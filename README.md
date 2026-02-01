# Digital-Transformer-Inspection-Tool
Digital Transformer Inspection & Maintenance Tool

Overview
This project is a Python-based digital inspection tool designed to simulate real-world transformer inspection procedures. It captures inspection inputs and automatically determines equipment condition and maintenance requirements using rule-based logic.

Inspection Parameters
 - Oil level condition
 - Oil temperature
 - Breather condition
 - Transformer cleanliness and oil leaks

Decision Logic
 - FAIL detected → Immediate maintenance required
 - No FAIL but WARNING detected → Maintenance scheduling required
 - No FAIL or WARNING → Transformer safe for continued operation

Purpose
 - Practice electrical engineering inspection logic
 - Apply Python programming to real engineering problems
 - Demonstrate condition-based maintenance concepts

Future Improvements
 - GUI interface (Tkinter)
 - Exportable inspection reports
 - Configurable temperature thresholds
 - Support for additional inspection parameters
