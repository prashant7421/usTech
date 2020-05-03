# usTech

1. Clone the repository git clone https://github.com/prashant7421/usTech.git
2. Create and activate virtual Environment 
3. Install all requirements from requirements.txt file in ustech folder
4. Collect All Statics of application python manage.py collectstatic (Not Necessary as statics are already collected)
5. dbsqlite is also available in application, super user is 
	user - ustech (Super User)
	password - usetech@4321

    I have also mentioned the credentials on Admin Dashboard just to ease your login

6. If you want create your own db ten delete the previous one and follow th below mentiond commands (Not Necessary as database with dummy data is already available)
	6.1 python manage.py makemigrations
	6.2 python manage.py migrate
	6.3 python manage.py createsuperuser


7. Running the application python manage.py runserver


Note -  Important models and their works are mentioned below. All The operations can be perform from the admin panel. To login in the admin panel click on Create Fixtures button in Navigation bar.

Model
1. Players - This is global table to add new players, After adding the player in this table we can attach him with any team according to the need

2. Match playerss -  In this model we need to select final list of players those are in the playing list. Entry in this table is possible once the match is created

3. Matchs - This table contains list of matches or fixtures, you can create any random match from this module

4. Player statisticss - This is the global table for all players Statistics (Runs, Wickets, Catches etc..)

5. Teams -  This Table containes the list of all teams available in the database, you can perform any operation CRUD in this table

