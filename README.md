# LaclauGPT demo dashboard with dummy data

This is a demo dashboard with dummy data for LaclauGPT data collection and analysis pipeline.

## LaclauGPT

LaclauGPT is a data collection and analysis pipeline. Developed for a political science project analyzing European parliament elections. It is called LaclauGPT as a tribute to [Ernesto Laclau](https://en.wikipedia.org/wiki/Ernesto_Laclau).

Developed by [Tomi Toivio](mailto:tomi.toivio@helsinki.fi) in the [Helsinki Institute for Social Sciences and Humanities](https://www.helsinki.fi/en/helsinki-institute-social-sciences-and-humanities).

## Pipeline Components

### Core Components

Core components are required for every data collection and analysis project.

#### Data Collection

Data collection tools such as a JavaScript TikTok scraper with a Node.js REST API backend. TikTok scraper will be published as open source.

#### Data Storage

Data storage using [CSC Allas](https://docs.csc.fi/data/Allas/) and [CSC Kaivos](https://docs.csc.fi/data/kaivos/overview/).

#### Data Analysis

Multimodal data analysis pipeline. Uses [Ollama](https://ollama.com/) to run [Llama3.2-vision](https://ollama.com/library/llama3.2-vision) on the [CSC Puhti](https://docs.csc.fi/computing/systems-puhti/) supercomputer. Jupyter Notepad version of the pipeline will be published as open source with dummy data.

#### Data Visualization

Data visualization with Streamlit. Actual data cannot be published due to GDPR. Only development dashboard with dummy data is public: [LaclauGPT Dummy Data](https://laclaugpt-dashboard-development.streamlit.app/).

### Experimental Components

Experimental components are still being developed and tested.

#### LaclauGPT 

LaclauGPT is an [Ollama](https://ollama.com) chatbot which uses vector and graph databases to answer questions about the dataset. Also functions as an agent and has data collection tools for collection of additional data. Pure Python without Langchain.

