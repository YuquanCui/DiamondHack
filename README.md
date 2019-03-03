## DiamondHack

“It’s not enough to be busy, so are the ants. The question is, what are we busy about?”

As students, we often have to fit tons of tasks into small-time fragments. And, many time management coaches suggest to take advantage of small pieces of free time to maximize our productivity. However, that is easier said than done. For instance, I had a 30-minute break between classes, but I just stared at my to-do list and my calendar not knowing what I can do in this 30 minutes and what should I do to use this time period efficiently. There are some productivity apps helping people to track tasks and appointments, but people still spend fairly a big chunk of their time to plan and layout tasks for everyday life. We wanted to combine different tools and integrate them with Machine Learning and AI to serve as a virtual personal assistant to everyone. We expected the virtual personal assistant to constantly analyse users’ calendar, to-do list and their preferred working styles to give specific, customized and practical suggestions on planning. We wanted to build a virtual personal assistant in your phone that:

    Analyzes users’ habits, expectations and preferences on how they want to spend their time efficiently
    Take over the task of planning and arrange specific time slots for tasks
    Help users to develop a clear understanding of what is coming and what to expect about each task
    Give positive reinforcements to encourage users to get more things done
    Provide customized suggestions based on users’ working styles

##What it does

First, import current schedule, tasks to do, and the historical data of the previous tasks: The current schedule includes time, repeated days, just like your google calendar. The tasks to do includes its category, deadline, priority, levels of experience, difficulty, and interest The historical data can include the task category, task priority, your levels of experience, difficulty, and interest. Then, trains the model using historical data and predicts the time needed to complete new tasks. Returns scheduling suggestion considering the preferred working range and a set of priority rules: The user can enter a preferred working range in a day, e.g. 8:00 to 20:00. Time Manager identifies free time blocks based on the user’s schedule and preferred working range. For each free time block, finds all candidate tasks by their deadline and sort these tasks by priority and ratio, which is the predicted task time/free time block Time Manager loops through each block to find the best combination of tasks that maximizes time usage

##Challenges

There was limited time to collect enough data to apply Machine Learning algorithms. We ended up using 200 rows of data that we collected and built a prediction model using linear regression. We did not have data for "bonus predictors" such as physical conditions, weather, mood, sleep quality, etc. We also had a two-hour discussion about the priority goal of the project: to maximize time utilization and fit in as many tasks as possible, or to maximize efficiency and find the best time block for each task. Due to data limitations, the second option would be not feasible in our demo. Besides, the first option would be very applicable to professions and businesses with scheduling challenges as well, so we decided to design our program to maximize time utilization as the top priority. We designed a closed-loop feedback model to use users’ data to improve the predictions and suggestions. We weren’t able to implement this idea due to the time constraints and limited user database. We look forward to push our concept into market and test our feedback model.

##What's next for Time Manager -- Your Virtual Personal Assistant

We start with a Time Manager App that fits your to-do list with your schedule. The next step is to integrate data from other Smart Devices (e.g. heart rate, mood, sleep quality, weather, etc.) to build a more extensive, accurate model to predict the user performance. In terms of accessibility, small hardware devices can be used to conveniently record task times (e.g. log in/off work). Multiple collaborators feature can also be added by sharing schedules. Our vision is to create an All-in-one Virtual Assistant that is connected to your Google Calendar, Alexa, smart phone, smart watch, etc. We look forward for a nearby future of Smart Devices, Smart Cities, and Smart Life.
