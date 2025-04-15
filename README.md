## Skills Match App for Data Roles

### About the Project

This project is a Skills Match App designed to analyze how well a candidate’s skills align with the requirements of a data-related job. By comparing the job description with the candidate’s skills, it provides:

1. Matched Skills: Skills the candidate has that match the job requirements.
2. Missing Skills: Skills required by the job but missing from the candidate’s profile.
3. Match Percentage: A calculated percentage showing overall alignment.

This app is especially useful for job seekers in data-related fields like Data Scientist, ML Engineer, Data Analyst, and so on, who want to evaluate their skills against job postings.

### Features

1. Predefined Skills List:
- Includes tools and technologies commonly used in data-related fields (e.g., Python, SQL, Tableau).

2. Interactive Analysis:
-Users can paste job descriptions and their profiles to get an instant breakdown.

3. Insights:
- Identifies areas of strength (matched skills) and areas for improvement (missing skills).
- Displays a color-coded match percentage for easy interpretation.

## How to Access the App
You can use the app online by clicking the link below:
https://huggingface.co/spaces/VickieAbdul/skills-match-app

### How to Run
You can run the app either locally or deploy it online.
1. Running Locally
- Clone or download this repository.

2. Install the required dependencies:
   pip install streamlit
   
3. Run the app:
   streamlit run app.py

4. Open your browser to http://localhost:8501 to view the app.

File Structure
- app.py: The main script that runs the app.
- requirements.txt: A file specifying the required libraries (streamlit).

### How It Works
1. Input Data:
- Paste the job requirements into one text area.
- Paste the candidate’s skills into another text area.

2. Processing:
- The app uses a predefined list of data-related skills/tools to extract matches from the input texts.
- Skills are matched based on whether they appear in both the job requirements and the candidate’s skills.

3. Output:
- A Match Percentage calculated from matched and missing skills.
- A list of Matched Skills and Missing Skills.
- Color-coded results for easy understanding:
  - Green: High match (80% or above).
  - Orange: Moderate match (50–79%).
  - Red: Low match (below 50%).

### Skills/Tools Included
The predefined list covers widely-used technologies and tools in data-related roles, including:
- Programming Languages: Python, R, Java, SQL, Scala
- Data Visualization: Tableau, Power BI, Excel, Matplotlib, Seaborn
- Machine Learning: TensorFlow, PyTorch, Deep Learning, NLP
- Big Data: Apache Spark, Snowflake, MongoDB, PostgreSQL
- Cloud Platforms: AWS, Azure, Google Cloud
- Soft Skills: Teamwork, Communication, Problem-Solving
- Business Tools: HubSpot, Salesforce, CRM Platforms

### Example Use Case
Job Description: Requires skills in "Python," "SQL," "Data Analysis," "Power BI," and "Deep Learning."
Candidate skills: Lists skills in "Python," "R," "SQL," "Tableau," and "Excel."

### Result:
Match Percentage: 60%.
Matched Skills: Python, SQL.
Missing Skills: Data Analysis, Power BI, Deep Learning.

### Future Improvements
Here are some ideas to enhance the app:
1. Add the ability for users to input their own list of skills/tools.
2. Integrate data visualization (e.g., bar charts or pie charts for matched vs. missing skills).
3. Use NLP libraries (like spaCy or NLTK) to extract meaningful phrases from unstructured job descriptions.

### Technology Used
Python: The programming language for building the app.
Streamlit: Framework for creating interactive web applications.

### Contributing
Feel free to contribute by:
- Suggesting new features or improvements.
- Expanding the predefined skills list.
- Reporting bugs or issues.

### License
This project is licensed under the MIT License.
