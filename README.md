# mate-bot
This is just a simple telegram bot that counts how many mate each user has drunk.

# Origin 
This bot was mainly developed during the 35c3.So be aware the code quality is shit because of to many tschunks 😉.

# Commands  
/start -->  starts the bot. While the bot is starting he will try to load the saved json file which must be located in the same directory.
If the bot succesfully finds the file, he will restore the saved state.
            
/add *amount of mate* --> Add the given amount of bottles of mate to you own account. e.g /add 2 

/mate --> prints out how many mate you already has drunk 

/stop --> This command will stop the bot and write the current state to a file in the same directory as json formatted data.
