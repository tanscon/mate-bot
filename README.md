# mate-bot
This telegram bot counts how many mate each user has drunk 

# Origin 
This bot was mainly developed during the 35c3.So be aware the code quality should be low

# Commands  
/start -->  starts the bot and the bot will try to load the saved json file from the same directory.
            If the bot finds the file, he will restore the saved state.
            
/add *amount of mate* --> Add the given amount of bottles of mate to you own account. e.g /add 2 

/mate --> prints out how many mate you already has drunk 

/stop --> This command will stop the bot and write the current state to a file in the same directory as json formatted data.
