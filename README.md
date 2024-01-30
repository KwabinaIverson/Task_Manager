# TASK MANAGEMENT APP

## RESEARCH

#### What is Task Management Software?
By definition, task management tools are any digital platform that helps **individuals** and **teams** manage their tasks. These are more than just simple to-do-lists. Task management tools allow teams to collaborate digitally by **organizing**, **prioritizing**, and **assigning tasks** to each other.

#### So what exactly does task management software do?
As with most software, there is a range of complexity and technological advancement among different systems. With that being said, typical features include:
* **Task scheduling** to set deadlines in advance.
* **Task customization and editing** to update for specific situations.
* **Task assignment**, which may include internal coworkers, external partners, or both.
* **Notifications/Alerts** to remind users about upcoming tasks and responsibilities.
* **Recurring tasks or templates** to standardize repetitive steps in your workflow.
* **Sub-tasks or parent tasks** to create additional steps within a task.
* **Time Tracking** to record the amount of time spent on tasks.
* **Progress reporting** to track current positioning in regards to the overall goal.
* **Task organization** using tags, labels and channels to group by common team or project.
* **To-do-lists** for easy task visualization.

#### Benefits Of Using Task Management Systems
Whether you use task management systems as an individual or as part of a team, there are many benefits to your daily workflow. Three of the top benefits include:
**Streamlined workflow**. Task management software helps individuals and teams record, assign, and organize all of the processes of a given workflow. This is beneficial because it ultimately reveals where there are redundancies, inefficiencies, and bottlenecks to be fixed.

**Improved productivity**. Task management software reduces the number of time workers have to spend sifting through information and getting organized. It also helps workers prioritize tasks, stay on top of current responsibilities, and prevent things from slipping through the cracks. When all is said and done, task management software can significantly improve team productivity.

**More effective collaboration**. How many times have you discussed next steps during a meeting or over the phone, but then you forget to write them down. Or perhaps you have a new due date for a project you’ve been working on, but now you have to individually tell each member of your team. Task management software brings everyone together on one platform, which helps improve communication and ensures that everyone knows what tasks they are responsible for, and when they need to complete them by.

### CORE FEATURES OF THE TASK MANAGEMENT APP
* **Account creation**. Users should be able to create an account.
* **Task creation**. Users should be able to create tasks.
* **Task editing**. Users should be able to edit the task created.
* **Set due dates**. Users should be able to set the starting and ending date of each task.
* **Task deletion**. Users should be able to delete created tasks.
* **Task categorization**. Users should be able to group tasks.
* **User authentication**. Users should be authenticated.
* **Group/Team creation**. Users should be able to create groups, add or remove users. using tags, labels and channels to group by common team or project.
* **Time Tracking** to record the amount of time spent on tasks.

### PROGRAMMING LANGUAGES TO USE
Python is a versatile and widely used programming language, and there are several compelling reasons why it is a good choice for various applications. Here are some key reasons:
* **Readability and Simplicity:** Python is known for its clean and readable syntax. Its design philosophy emphasizes code readability, and its syntax allows developers to express concepts in fewer lines of code than languages like C++ or Java. This makes it easier to maintain and understand code.

* **Large Ecosystem of Libraries and Frameworks:** Python has a rich ecosystem of third-party libraries and frameworks that simplify development in various domains. For example, Flask and Django are popular web frameworks, while requests and Beautiful Soup are widely used for web scraping.

* **Rapid Development:** Python's simplicity and readability contribute to faster development cycles. This makes it an excellent choice for prototyping, building MVPs (Minimum Viable Products), and iterating quickly on software projects.

### GIT AS VERSION CONTROL SYSTEM
* **Master Branch (Main)**. This is where all the code for deployment would be.
* **Test Branch**. This is where we test all functions, documentation, and the app.
* **Feature Branch**. Create three branches for each developer. Implement features for the app.

### DATABASE SCHEMA (USING SQL)
1. **User:**
    * Attributes:
        * **user_id** (Primary Key)
        * **username**
        * **email**
        * **password** (Hashed for security)
        * **profile_picture** (Secondary)
    
    * Tasks:
        * **task_id** (Primary)
        * **title**
        * **description**
        * **start_date**
        * **due_date**
        * **completed**
        * **user_id** (foreign key)

2. **Group**:
    * Group Attributes:
        * **group_id**
        * **group_name**
        * **channel** (Channel to group by (e.g., project/channel name))
        * **unique_key**

    * User Group:
        * **user_group_id** (Primary)
        * **user_id**
        * **group_id**
        * **user_foreign_key** (user_id)
        * **group_foreign_key** (group_id)
