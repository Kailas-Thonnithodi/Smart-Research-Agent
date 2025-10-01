---
title: Smart-Research-Agent
app_file: app.py
sdk: gradio
sdk_version: 5.47.2
---
# 🔬 Smart-Research-Agent

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Gradio](https://img.shields.io/badge/Gradio-5.47.2-orange)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-yellow)

The **Smart Research Agent** is an intelligent system that takes any user query, applies advanced research methods, and generates a structured report. The report is then emailed to a specified recipient in a polished HTML format.

This project can be highly useful in scenarios where quick, thorough, and well-presented research is needed.

---

## 🧩 Components

### 🔎 Searcher Agent
- Performs **Google searches** on the specified topic.
- Uses the **WebSearchTool (OpenAI)** for queries.  
- **Cost note**: Each search may use up to **$0.015** → optimisation and resourcefulness are key.  
- Returns a concise **summary of a single page result** based on the search click-through.

---

### 🎯 Search Optimiser Agent
- Proposes **related questions/concepts** surrounding the topic.  
- Helps guide the Searcher Agent to build **diverse, meaningful insights**.  
- Returns a list of short, focused questions rooted in the original concept.

---

### ✍️ Writer Agent
- Compiles the findings from the Searcher Agent into a **formal research report**.  
- Supports predefined **word/page limits** for flexibility.  
- Builds reports entirely from the **data collected by child agents**.

---

### 📧 Emailer Agent
- Packages the Writer Agent’s report into a **structured HTML email**.  
- Ensures the recipient receives an **interactive email** with clickable links.  
- Aims for a professional and reader-friendly presentation.

---