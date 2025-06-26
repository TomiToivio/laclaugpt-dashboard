# LaclauGPT demo dashboard with dummy data

This is a demo dashboard with dummy data. This is a visualization tool for the LaclauGPT data collection and analysis pipeline.

## LaclauGPT

LaclauGPT is a political science multimodal data collection and analysis pipeline. It is called LaclauGPT as a tribute to [Ernesto Laclau](https://en.wikipedia.org/wiki/Ernesto_Laclau).

LaclauGPT is developed by [Tomi Toivio](mailto:tomi.toivio@helsinki.fi) in the [Helsinki Institute for Social Sciences and Humanities](https://www.helsinki.fi/en/helsinki-institute-social-sciences-and-humanities).

The pipeline was developed for three research projects funded by the European Union:
* [CO3](https://www.co3socialcontract.eu/) researches the social contract. 
* [ENDURE](https://www.endure-project.org/​) researches the world after the pandemic. 
* [PLEDGE](https://www.pledgeproject.eu/​) researches grievance politics.

The pipeline was used to collect and analyze multimodal social media data related to the [2024 European parliament elections](https://en.wikipedia.org/wiki/2024_European_Parliament_election). Data was collected from TikTok and Instagram. Data collection started in 1st of May 2024 and continued until the election day in 9th of June 2024. Collection was based on usernames of official election candidates as well as hashtags and search queries related to the elections. Election data was collected for Bulgaria, Croatia, Finland, France, Germany, Hungary, Portugal, Spain and Sweden. Collected and analyzed data cannot be released yet due to GDPR. This open source version uses dummy data. 

## Pipeline Components

### Core Components

These are the components which can be customized for other research projects.

#### Data Collection

Data collection tools such as a JavaScript TikTok scraper with a Node.js REST API backend. TikTok scraper will be published as open source.

#### Data Analysis

Multimodal data analysis pipeline. Uses [Ollama](https://ollama.com/) to run [Llama3.2-vision](https://ollama.com/library/llama3.2-vision) on the [CSC Puhti](https://docs.csc.fi/computing/systems-puhti/) supercomputer. Jupyter Notepad version of the pipeline will be published as open source with dummy data.

#### Data Visualization

Data visualization with Streamlit. Actual data cannot be published due to GDPR. Only development dashboard with dummy data is public: [LaclauGPT Dummy Data](https://laclaugpt-dashboard-development.streamlit.app/).

### Experimental Components

These components are experimental and mostly developed for research purposes. No really required for similar projects.

#### LaclauGPT Chatbot

LaclauGPT is an [Ollama](https://ollama.com) chatbot which uses vector and graph databases to answer questions about the dataset. Also functions as an agent and has data collection tools for collection of additional data. Pure Python without Langchain. This is currently purely experimental.

