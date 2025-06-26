# LaclauGPT demo dashboard with dummy data

This is a demo dashboard with dummy data. This is a visualization tool for the LaclauGPT data collection and analysis pipeline.

# LaclauGPT 

LaclauGPT is a political science multimodal data collection and analysis pipeline. It is called LaclauGPT as a tribute to [Ernesto Laclau](https://en.wikipedia.org/wiki/Ernesto_Laclau).

LaclauGPT is developed by [Tomi Toivio](https://github.com/TomiToivio) for three [Helsinki Hub on Emotions, Populism and Polarisation](https://www.helsinki.fi/en/researchgroups/emotions-populism-and-polarisation) research projects funded by the European Union:
* [CO3](https://www.co3socialcontract.eu/) researches the social contract. 
* [ENDURE](https://www.endure-project.org/) researches the world after the pandemic. 
* [PLEDGE](https://www.pledgeproject.eu/) researches grievance politics.

The pipeline was used to collect and analyze multimodal social media data related to the 2024 European parliament elections. Data was collected from TikTok and Instagram. Data collection started in 1st of May 2024 and continued until the election day in 9th of June 2024. Collection was based on usernames of official election candidates as well as hashtags and search queries related to the elections. Election data was collected for Bulgaria, Croatia, Finland, France, Germany, Hungary, Portugal, Spain and Sweden. Collected and analyzed data cannot be released yet due to GDPR. This open source version uses dummy data. 

## LaclauGPT Data Collection and Analysis Pipeline Components

#### Data Collection

[LaclauGPT TikTok Scraper](https://github.com/TomiToivio/LaclauGPT-TikTok-Scraper) for EP2024. Not maintained currently.

#### Data Analysis

[LaclauGPT Multimodal Data Analysis](https://github.com/TomiToivio/LaclauGPT-Multimodal-Analysis) for Ollama and CSC Puhti.

#### Data Visualization

[LaclauGPT Dashboard](https://github.com/TomiToivio/laclaugpt-dashboard-development) for data visualization. Actual data cannot be published due to GDPR. Only this development dashboard with dummy data is public: [LaclauGPT Dummy Data](https://laclaugpt-dashboard-development.streamlit.app/).

#### LaclauGPT Chatbot

[LaclauGPT](https://github.com/TomiToivio/LaclauGPT) is an [Ollama](https://ollama.com) chatbot which uses vector and graph databases to answer questions about the dataset. Also functions as an agent and has data collection tools for collection of additional data. Pure Python without Langchain. This is currently purely experimental. 

# CO3

This project has been developed for the [CO3](https://www.co3socialcontract.eu/) project. This project has received funding from the EU's Horizon Europe research and innovation programme under Grant Agreement 101132631. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the Agency. Neither the European Union nor the granting authority can be held responsible for them.