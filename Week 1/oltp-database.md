<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>OLTP Database</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>30</strong> minutes.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and MySQL running in a Docker container.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete these labs in a single session, to avoid losing your data.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MySQL as an OLTP database. You will be using MySQL to store the OLTP data.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will:</p>
    <ul>
      <li>design the schema for OLTP database.</li>
      <li>load data into OLTP database.</li>
      <li>automate admin tasks.</li>
    </ul>
    <h1>Tools / Software</h1>
    <ul>
      <li>MySQL 8.0.22</li>
      <li>phpMyAdmin 5.0.4</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h1>Exercise 1 - Check the lab environment</h1>
    <p>Before you proceed with the assignment :</p>
    <ul>
      <li>Start MySQL server.</li>
    </ul>
    <h1>Exercise 2 - Design the OLTP Database</h1>
    <h3>Task 1 - Create a database.</h3>
    <p>Create a database named sales.</p>
    <h3>Task 2 - Design a table named sales_data.</h3>
    <p>Design a table named sales_data based on the sample data given.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/sampledata.png" alt="">
    </p>
    <p>Create the sales_data table in <code>sales</code> database.</p>
    <p>Take a screenshot of the sql statement you used and the output.</p>
    <p>Name the screenshot as <code>createtable.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h1>Exercise 3 - Load the Data</h1>
    <h3>Task 3 - Import the data in the file oltpdata.csv</h3>
    <p>Download the file oltpdata.csv from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv</a></p>
    <p>Import the data from oltpdata.csv into sales_data table using phpMyAdmin.</p>
    <p>Take a screenshot of the phpMyAdmin import status.</p>
    <p>Name the screenshot as <code>importdata.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 4 - List the tables in the database <code>sales</code>.</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>listtables.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 5. Write a query to find out the count of records in the tables sales_data.</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>salesrows.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h1>Exercise 4 - Set up Admin tasks</h1>
    <h3>Task 6 - Create an index</h3>
    <p>Create an index named ts on the timestamp field.</p>
    <h3>Task 7 - List indexes</h3>
    <p>List indexes on the table sales_data.</p>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>listindexes.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 8 - Write a bash script to export data.</h3>
    <p>Write a bash script named <code>datadump.sh</code> that exports all the rows in the sales_data table to a file named sales_data.sql</p>
    <p>Take a screenshot of the contents of the <code>dailydump.sh</code> bash file command you used and the output.</p>
    <p>Name the screenshot as <code>exportdata.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <p>End of assignment.</p>
    <h2>Authors</h2>
    <p>Ramesh Sannareddy</p>
    <h3>Other Contributors</h3>
    <p>Rav Ahuja</p>
    <h2>Change Log</h2>
    <table>
      <thead>
        <tr>
          <th>Date (YYYY-MM-DD)</th>
          <th>Version</th>
          <th>Changed By</th>
          <th>Change Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2021-11-22</td>
          <td>0.1</td>
          <td>Ramesh Sannareddy</td>
          <td>Created initial version</td>
        </tr>
        <tr>
          <td>2022-10-17</td>
          <td>0.2</td>
          <td>Ramesh Sannareddy</td>
          <td>Updated version</td>
        </tr>
        <tr>
          <td>2022-10-24</td>
          <td>0.3</td>
          <td>Alison Woolford</td>
          <td>Updated version</td>
        </tr>
      </tbody>
    </table>
    <p>Copyright (c) 2022 IBM Corporation. All rights reserved.</p>
  </body>
</html>
