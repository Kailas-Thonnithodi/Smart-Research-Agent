---
title: Smart-Research-Agent
app_file: app.py
sdk: gradio
sdk_version: 5.47.2
---
# 🔬 Smart-Research-Agent

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Gradio](https://img.shields.io/badge/Gradio-5.47.2-orange)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Model-Hugging%20Face-yellow)](https://huggingface.co/spaces/GoldenMeta/Smart-Research-Agent)
![Status](https://img.shields.io/badge/status-active-success)

The **Smart Research Agent** automates the process of information discovery and reporting. Given a query, it performs deep research, generates a structured report, and emails it directly to a specified recipient using the **SendGrid API**.

---

## 📖 About

The Smart Research Agent streamlines research into four steps:

1. Accept a research query or question.  
2. Conduct in-depth searches and gather relevant insights.  
3. Generate a comprehensive research report.  
4. Deliver the report via email in an interactive HTML format.  

This pipeline ensures research is **thorough, well-structured, and instantly delivered**.

### 🌐 Live Demo
Try it out on [Hugging Face 🤗](https://huggingface.co/your-username/your-model). If you are interested in local development of the agents, you can follow the instructions folder. 

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