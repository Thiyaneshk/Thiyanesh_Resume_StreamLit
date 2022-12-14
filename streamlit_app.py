import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with open('Thiyanesh_PLSQL.pdf', "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#####################

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Thiyanesh"
PAGE_ICON = ":wave:"
NAME  = "Thiyanesh Kamaraj"
TITLE = "PLSQL Developer"
CITY  = "*Halifax*, Nova Scotia"
MOBILE= "`+1 (782) 882 4409`"
DESCRIPTION = """
Oracle PLSQL Developer, Seeking opportunity.
"""
EMAIL = "thiyaneshk@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/thiyaneshk",
    "GitHub": "https://github.com/ThiyaneshK",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

#####################
# Header 
st.write('''
# Thiyanesh Kamaraj
''')

# st.write('''
# # Thiyanesh Kamaraj
# ##### Oracle PL\SQL Developer
# ''')
image = Image.open('dp.jpg')
col1, col2 = st.columns(2)

with col1:
    st.image(image, width=200)

with col2:
    st.write("📫", EMAIL)
    st.write("☎️",MOBILE)
    st.write("⚓", CITY)
    st.write("🔗",'[LinkedIn](https://www.linkedin.com/in/thiyaneshk)')
    # st.write("🔗",'[GitHub](https://github.com/Thiyaneshk)')
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name='Thiyanesh_PLSQL.pdf',
        mime="application/octet-stream",
    )
#
# st.write('''
# # Thiyanesh - PLSQL Developer
# ''')

# st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Highly versatile Oracle application developer with 10 years of
experience in development of Banking applications with prowess in
learning technology, knack to work in team to achieve concrete
goals on a strict deadline. Forte includes Oracle PLSQL, Shell
scripting/automation and Python.
''')
# 
# - Strong skills include Oracle database, Banking application development , Python and shell scripting. 
# - Extensive experience working on Banking applications of Flexcube/B@NCS.
# - Hands on experience on Scripting/automation in Unix/Linux env.
# - Have working experience as Oracle Database Architect, in which have migrated Sybase database to a new Oracle database.
# - Involved in Oracle DB related activities including upgrades and migration.
# - Have good knowledge in Python and AWS.
# - Gappppp
# 
# - 10+ Years of programming experience as an PL/SQL Developer in Analysis, Design and Implementation of Business Applications using Oracle DB.
# 
# - Knowledgeable Oracle Developer skilled in Data collection, analysis and management. Works well under pressure and consistently meets deadline and targets while delivering high quality work.
# 
# - Involved in all phases of SDLC from analysis, design, development, testing, implementation and maintenance with timely delivery against aggressive deadlines.
# 
# - Experience with Data flow diagrams, Data dictionary, Database normalization
# 
# - Effectively made use of Table, Views, Constraints, Indexes, partitioning, collections, Analytic functions, Materialized views, Query re-write, et al.
# 
# - Developed complex database objects like stored procedures, functions, packages, triggers using SQL and PL/SQL.
# 
# - Experiecne in Oracle supplied packages, Dynamic SQL, Records and PL/SQL Tables. Loaded data into Oracle tables using SQL Loader.
# 
# - Created packages and procedures to automatically drop tables indexes and create indexes for tables.
# - Worked extensively on Ref Cursor, External tables and collections.
# 
# - Expertise in Dynamic SQL, Collections and exception handling SQL.
# - Experience om SQL performance tuning using Cost-Based optimization

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/thiyaneshk" target="_blank">Thiyanesh - PLSQL Developer</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact-me">Contact me</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


#####################
st.markdown('''
## Work Experience
''')

#
# txt('**Senior Consultant**, [Virtusa](https://www.virtusa.com/) Chennai, India',
# '10/2018 - 07/2022')
# with st.expander("Tasks" ):
#     st.markdown('''
#     - Developed database architectural strategies at modeling, design and implementation stages for migration of legacy Sybase database to Oracle database.
#     - Migration of MIS application from Sybase to Oracle in view to implement most secure and robust financial reporting application for Citi Bank - Japan.
#     - Gathered, defined and refined requirements, led project design and oversaw implementation.
#     - Determined areas for improvement and implemented processes which leveraged Oracle security features to alleviate problems.
#     - Automated EUC files into automated reports as value-adds to user, which reduced 1hr of human effort per day and reduced cost-to-company of $200,000 per year.
#     - Created common utils package for the application with custom functions and autonomous logging, which improved code reusability and code quality.
#     - Created scripts in shell/Perl and processes for data loading, integration, maintenance, data quality check and other tools used for the implementation.
#     - Agile application development including constant feedback from clients and implementation of robust system.
#     ''')
#
# with st.expander("Achievements" ):
#     st.markdown('''
#     - Developed database architectural strategies at modeling, design and implementation stages for migration of legacy Sybase database to Oracle database.
#     - Migration of MIS application from Sybase to Oracle in view to implement most secure and robust financial reporting application for Citi Bank - Japan.
#     - Gathered, defined and refined requirements, led project design and oversaw implementation.
#     - Determined areas for improvement and implemented processes which leveraged Oracle security features to alleviate problems.
#     - Automated EUC files into automated reports as value-adds to user, which reduced 1hr of human effort per day and reduced cost-to-company of $200,000 per year.
#     - Created common utils package for the application with custom functions and autonomous logging, which improved code reusability and code quality.
#     - Created scripts in shell/Perl and processes for data loading, integration, maintenance, data quality check and other tools used for the implementation.
#     - Agile application development including constant feedback from clients and implementation of robust system.
#     ''')


txt('[Virtusa](https://www.virtusa.com/) , **Senior Consultant**','Chennai, India.')
txt('10/2018 - 07/2022',' ')
st.markdown('''
- Developed database architectural strategies at modeling, design and implementation stages for migration of legacy Sybase database to Oracle database.
- Migration of MIS application from Sybase to Oracle in view to implement most secure and robust financial reporting application for Citi Bank - Japan.
- Gathered, defined and refined requirements, led project design and oversaw implementation.
- Determined areas for improvement and implemented processes which leveraged Oracle security features to alleviate problems.
- Automated EUC files into automated reports as value-adds to user, which reduced 1hr of human effort per day and reduced cost-to-company of $200,000 per year.
- Created common utils package for the application with custom functions and autonomous logging, which improved code reusability and code quality.
- Created scripts in shell/Perl and processes for data loading, integration, maintenance, data quality check and other tools used for the implementation.
- Agile application development including constant feedback from clients and implementation of robust system.
''')

txt('[Oracle Financial Services Software](https://www.oracle.com/) , **Application Developer**','Chennai, India')
txt('08/2016 - 10/2018',' ')
st.markdown('''
- Customization of the application to the needs of the clients, which includes understanding the business requirement, feasibility study, implementation of the same by coding the same which includes creation of database objects like tables, triggers, views and packages, procedures, functions with the highest degree of coding standards. 
- Catering needs of Flexcube universal banking applications to a range of clients in development and maintenance of clients in the Middle East and Asia Pacific.
- Reduction of EoD/EoM runtime over 20-30% by performance tuning on analyzing AWR/ADDM reports for faster application design and development.
- Involved in migrating Toplink to POJO, which improved the performance of the application considerably.
- Implemented system of tracking the bugs spotted in various clients and proactivily fixing the bugs in all the clients running the same version of Flexcube, which decreased number of issues raised clients and inturn improved customer satisfaction.
''')

txt('[HCL Technologies Ltd.](https://www.hcltech.com/) , **Software Engineer**','Chennai, India')
txt('12/2014 - 08/2016',' ')
st.markdown('''
- Application development with all stages of System Development Life Cycle (SDLC). Applied Database Tuning and Optimization, Normalization under tight schedules of development and implementation. 
- Development includes Tier upgrade/downgrade/association process where Customers are assigned to tiers according to sales made as per business rules.
- Automation of Scripts in Shell and Perl which replaced work of L1/L1.5 team in reports and Monitoring process. Further improved productivity with reduced cost to the company.
- Tuning the existing PL/SQL codes to run faster and perform better in a scaleble environment. Improved the performance of the critical daily sales process and reduced the run time by 30%.
- Created 6 value-adds worth $105,000 which brought new business to the Company and have satisfied the customer as it improved productivity. Obtained high acclaims for the same.
''')

txt('[C-Edge Tech.](https://cedge.in/) ( A TCS - SBI Enterprise ) , **Developer**','Chennai, India')
txt('10/2012 - 12/2014',' ')
st.markdown('''
- Managing a Center of `10` professors, OOOOO least `20+` research publications annually. 
- B@NCS - Core banking implementation for over `25` Banks which contained over 850+ Banks in them. Worked in Client location which involved direct interaction with clients to obtain the requirement.
- Extensive experience in development of modules in PL\SQL, COBOL. Development of automation scripts using UNIX Shell and Perl to improve productivity and enhance the existing scripts.
- Headed a Team of 2-4 members as Team lead of Reports, GL and Deposit Modules. Develop tool to automatically send reports and files which failed to deliver over ftp. This process reduced work of L1.5 and improved the productivity and improved client’s satisfaction with the available narrow band and obtain highest success rate of delivery in turn reduce the cost considerably.
''')
#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Oracle PLSQL`, `SQL`, `Python`')
txt3('Scripting', '`Python`, `Perl`, `Shell`,`API\'s`')
txt3('Domain', '`Banking`, `Retail`')
txt3('Banking Application', '`Oracle Flexcube`,`TCS B@NCS`')
txt3('Database', '`Oracle`,`Oracle RAC`, `OAD`, `Sybase`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `plotly`, `altair`, `ggplot2`')
# txt3('Machine Learning', '`scikit-learn`')
# txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`, `AWS` ')
txt3('Tools', '`Jenkins CICD`, `BitBucket`,`GitHub`,`JIRA`,`ServiceNow`')

txt3('SDLC', '`Agile`, `Waterfall`')

txt3('Data ETL', '`SQL*Loader`, `External Table`, `DataPump`')


#####################
st.markdown('''
## Education
''')

txt('**B.Tech** (Information Technology), *Anna University*, India',
'2002-2006')
st.markdown('''
- GPA: `7.61`
- Bachelors of Technology, Information Technology.
''')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/thiyaneshk')
# txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/Thiyaneshk')
# txt2('', 'https://github.com/chaninlab/')
# txt2('', 'https://github.com/dataprofessor')
# txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
# txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
# txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
# txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
# txt2('Publons', 'https://publons.com/a/303133/')



#####################
st.markdown('''
## Contact me
''')
txt2('Email', 'thiyaneshk@gmail.com')
txt2('Mobile', '+1 (782) 882 4409')

with open("dp.jpg", "rb") as file:
  btn = st.download_button(
    label="Download Resume",
    data=file,
    file_name="Thiyanesh_PLSQL.pdf",
    mime="application/pdf"
  )