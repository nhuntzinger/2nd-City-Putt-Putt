Austin Galura

Jackson Miles

Nathan Huntzinger

Jacob Clawson

# Requirements Gathering Document

9/15/21

Our client XYZ is asking for an app that will facilitate put put golf tournaments which are sponsored by various companies. Through multiple meetings and a series of questions, we have found the requirements for the web app to be as follows:

## Client Description of Requirements

1. App should allow you to sign in as a user of 4 different types: Player, Sponsor, Bartender, and Manager
2. Players can sign up for a tournament. During the tournament, they can:
    1. Manually enter their score/stroke count for each hole they play
    2. Order drinks during play that will come to them from Bartenders at whatever hole they're on
    3. Keep track of the current leaderboard for their tournament and try to place at the top
3. Sponsors can hold the tournament. This includes:
    1. Reserving the days they would like to sponsor a tournament (Only once per tournament cycle, and only one company per tournament)
    2. Award prize money (set at their discretion) to the top 3 players in their tournament
4. Managers can officially start and end the tournaments. They can also edit drink options for the tournament and keep track of money allocation for players and sponsors.
5. Bartenders can fill in order drinks as they come in, making sure they are delivered to the right player and emptying their order queues as fast as they can.

Requirements rewritten to be Clear, Unambiguous, Consistent, Prioritized, Verifiable. (CUCPV)

1. A sponsor will be able to reserve a day for a tournament.
2. Sponsors cannot reserve a day that has already been reserved by the same or a different sponsor.
3. Sponsors will pay the required amount to reserve a day for a tournament.
4. Sponsors will fund the prize money for a tournament.
5. Users must be able to sign up for an account on the system.
6. All users, upon sign up, will be of type Player. Only managers may change users to any of the 4 user types
    1. Managers will enter credentials in order to sign up as manager account.
7. Players will be able to check in to their game on the day picked by their Sponsor
8. Player's scores will be kept for each individual hole and for the game as a whole.
9. Players can order drinks at any point during their game.
10. Players pay for their own drinks
11. Players will know at any time what hole they are at.
12. Players will enter the number of strokes per hole at each hole.
13. Upon entering the number of strokes a Player will be moved to the next hole or the end if the previous hole was the last hole.
14. Bartenders will be informed of newly placed orders by Players.
15. Bartenders can mark drinks as delivered.
16. Bartenders will be informed of Player's locations when a Player places a drink order
17. Managers will control when a tournament is started or ended.
18. Managers have administrative capabilities, i.e. override capabilities
19. Managers will add money to Sponsors or Player's accounts. i.e. they manage the register
20. Managers can 'cash out' the register and give it to the store owner.
21. At the end of each tournament there will be a leaderboard.
22. This leaderboard will have results for that day
23. There will also be an 'all time' leaderboard available at the end of a Tournament.
24. Players compete for a place on the leaderboard.
25. There are prizes given to the top 3 players of each Tournament.
26. Players will be informed of their place on the leaderboard at the end of the Tournament.
27. Drinks can only be ordered by Players
28. Bartenders are the only ones informed of drink orders
29. Drinks are not returnable. Upon payment acceptance the drink order is sent to the bartender and that is final.
30. Tournaments have a pre-determined number of holes
31. Tournaments will have a scheduled start time
32. Tournaments will have a sponsor or a game cannot be played.
33. User's will sign up using an email and password.
34. Basic authentication will assure security of user rights.
35. Players add money to their account in order to purchase drinks

## MOSCOW

1. MUST - A sponsor will be able to reserve a day for a tournament.
2. MUST - Sponsors cannot reserve a day that has already been reserved by the same or a different sponsor.
3. MUST - Sponsors will pay the required amount to reserve a day for a tournament.
4. MUST - Sponsors will fund the prize money for a tournament.
5. MUST - Users must be able to sign up for an account on the system.
6. MUST - All users, upon sign up, will be of type Player. Only managers may change users to any of the 4 user types
7. MUST - Players will be able to check in to their game on the day picked by their Sponsor
8. MUST - Player's scores will be kept for each individual hole and for the game as a whole.
9. MUST - Player's can order drinks at any point during their game.
10. MUST - Player's pay for their own drinks
11. SHOULD - Player's will know at any time what hole they are at.
12. MUST - Player's will enter the number of strokes per hole at each hole.
13. MUST - Upon entering the number of strokes a Player will be moved to the next hole or the end if the previous hole was the last hole.
14. MUST - Bartenders will be informed of newly placed orders by Players.
15. SHOULD - Bartenders can mark drinks as delivered.
16. SHOULD - Bartenders will be informed of Player's locations when a Player places a drink order
17. SHOULD - Managers will control when a tournament is started or ended.
18. MUST - Managers have administrative capabilities, i.e. override capabilities
19. MUST - Managers will add money to Sponsors or Player's accounts. i.e. they manage the register
20. COULD - Managers can 'cash out' the register and give it to the store owner.
21. MUST - At the end of each tournament there will be a leaderboard.
22. MUST - This leaderboard will have results for that day
23. COULD - There will also be an 'all time' leaderboard available at the end of a Tournament.
24. MUST - Players compete for a place on the leaderboard.
25. MUST - There are prizes given to the top 3 players of each Tournament.
26. MUST - Players will be informed of their place on the leaderboard at the end of the Tournament.
27. COULD - Drinks can only be ordered by Players
28. SHOULD - Bartenders are the only ones informed of drink orders
29. SHOULD - Drinks are not returnable. Upon payment acceptance the drink order is sent to the bartender and that is final.
30. MUST - Tournaments have a pre-determined number of holes
31. COULD - Tournaments will have a scheduled start time
32. MUST - Tournaments will have a sponsor or a game cannot be played.
33. MUST - User's will sign up using an email and password.
34. MUST - Basic authentication will assure security of user rights.
35. SHOULD - Players add money to their account in order to purchase drinks

To sum up all requirements into functional and non-functional categories, we have the following:

## AO / FURPS

### Audience Oriented

1. System requires all users to authenticate themselves before app use
    1. On first login, users will be prompted to create account
        1. Users provide username, email, and password. All users are created as account type Player until changed by the Manager
    2. Upon subsequent login, system will ask for username and password. If credentials don't match in system database, user will be asked to try again, no limit to retries
2. User Account Features
    1. Any logged in user should be able to see and modify their username, email, and password
    2. Only Manager can edit other users' account type
3. Player Features
    1. Player can sign up for a tournament.
        1. Player can choose from any tournament that is scheduled
        2. Player can only be part of one tournament at a time
        3. Player cant access playing activity until their selected tournament has started
    2. During tournament, player can keep track of own score
        1. Player enters own stroke count at each hole; this moves them to next hole automatically
        2. Player can view leaderboard for their tournament at any time during play
            1. Leaderboard holds all current stroke count and hole count for all players in tournament
    3. Player can order drink from drink menu
        1. Player can choose from list of possible drinks provided by sponsor
        2. Player enters drink order; if account has sufficient funds order will go through. Otherwise, user is prompted to add sufficient funds
        3. Player selects hole they want drink delivered to so Bartender can find them
        4. Player can view all their active/past drink orders
    4. Player can manage money in their account
        1. Player enters their own money amount in account. No authentication needed for now
4. Sponsor Features
    1. Sponsor can schedule to hold a tournament on any day during valid date range supplied by manager
        1. Sponsor can only schedule on day not selected by another sponsor
    2. Sponsor enters money amount for cash prizes for top 3 players to be added to their accounts after tournament ends
    3. Sponsor can view leaderboard for their tournament at any time
    4. Sponsor can create a menu of drinks for players to order from during their tournament
    5. Sponsor cannot cancel tournament after scheduling. Dates are final?\*\*
5. Manager Features
    1. Manager can change other user account types (Player, Sponsor, Bartender)
    2. Manager can add or remove user accounts
    3. Manager keeps track of 'register' from drink orders throughout tournament; gives all proceeds to sponsor at end of tournament?\*\* (Do managers take a cut of the proceeds?)
6. Bartender features
    1. Bartender can receive and view all drink orders in the tournament drink queue
        1. Each drink order has the drink type requested, name of player, and hole to be delivered to
        2. Bartender receives notification every time an order is added to the queue
    2. Bartender can mark drink as delivered which will remove it from the queue.
    3. Bartender does not have access to register; only the drink queue.

### FURP or FURPS+

1. The system will use a database
    1. Database will store account info for all users
        1. Username,
        2. Email,
        3. Password
        4. Account funds (for players only)
        5. Active drink orders (for players only)
    2. Database will store tournament info
        1. Date of tournament and if it is started or not
        2. Current leaderboard
        3. Drink menu
            1. Drink type
            2. Price
        4. Drink order queue
        5. Money Register

2. The team will use Git for version control, and host the app repository on GitHub

3. The team will deploy and host app using AWS

4. The app should be mobile friendly

## Workflow diagrams

### Actors and Their Goals

Figure 1 - User creates account

![](https://t18032048.p.clickup-attachments.com/t18032048/3df86314-248c-452e-ae89-af508a6dca99/User%20creates%20account.png)

Participating Actor: User

Entry Condition:

* User requests to create an account

Exit condition:

* Account is created
* User exits account creation activity

Event Workflow:

1. User requests to create account
2. System requests user's information
    1. If user fills in all requested information, system creates account type Player unless Manager credentials are supplied
    2. If user backs out of signup activity, account is not created

Figure 2 - Player Orders a Drink

![](https://t18032048.p.clickup-attachments.com/t18032048/9a5caf1f-639f-4eef-8196-28d3518b9d14/Player%20orders%20drink.png)

Participating Actors: Player

Entry Conditions:

* Player is logged in and participating in tournament
* Player accesses drink menu

Exit Condition:

* Player exits out of drink ordering activity
* Player completes drink order

Event Workflow:

1. Player opens drink menu on their page
2. Player selects drink type from menu and inputs the hole they want it delivered at
3. If player has sufficient funds:
    1. Drink order sent to queue
    2. Player brought to home page and their drink order history is updated
4. If player has insufficient funds:
    1. Warning shown on screen
    2. Player can exit activity to add funds to their account

Figure 3: Sponsor Workflow

![](https://t18032048.p.clickup-attachments.com/t18032048/f18303d2-cddd-4d16-a53d-e5a3d086cf69/sponsor-flow.png)

Participating Actors: Sponsor

Entry Conditions:

* Sponsor has just logged in.
* This is the first thing they will see upon login.

Exit Condition:

* Sponsor finishes setting up an event at checkout
* Or a Sponsor cancels and leaves

Event Workflow:

1. Sponsor logs into their account and is shown the calendar.
2. Sponsor selects a day
    1. Sponsor could be informed that the day they clicked on was already taken, which would return them to the calendar
    2. Sponsor's picked day was not taken and they get to proceed to 3.
3. Sponsor selects a time of the day to have their tournament
4. After they have picked a day the sponsor will be shown a payment / checkout screen
5. The sponsor finishes the checkout and the tournament is booked.

Extensions:

1. During steps 2 - 5 the Sponsor can cancel and return to step 1

Figure 4: Player Game Flow

![](https://t18032048.p.clickup-attachments.com/t18032048/cef40a79-3321-452d-a49e-2f1388bec80d/user-flow.png)

Participating Actors: Player

Entry Conditions:

* The player was previously logged in
* Their Sponsor already paid for and setup a game
* The player selected their game and entered at the selected time

Exit Condition:

* The user finishes their game

Event Workflow:

1. The player will continuously enter the strokes for their holes
2. Upon entering their strokes the player will be moved to the next hole
3. If the hole they are on is currently the last hole the Player will be informed of that
4. After the user has entered the final strokes count they will be shown the leaderboard for that tournament.

Extensions:

1. The Player can order drinks at anytime during their tournament.

Figure 5: Bartender fulfills order

* _The bartender fulfills order_

![](https://t18032048.p.clickup-attachments.com/t18032048/2f1d7673-9f81-4250-8b9d-b7efbd3ceae3/Untitled%20Diagram.drawio.png)

Participating actor: Bartender

Entry Conditions:

* Bartender is logged in.
* Bartender wants to complete an order.

Exit conditions:

* Bartender is done working / logs out

Event Flow:

1. Bartender requests to see orders
2. Query database for current drink data
3. System displays pending orders
4. Bartender fulfills and marks order complete
5. Database is updated
6. Updated info is displayed

Figure 6: User Logs In

* _The user logs into the app_

![](https://t18032048.p.clickup-attachments.com/t18032048/4bf1f832-394a-4b4a-afe5-03776979e87a/Untitled%20Diagram.drawio%20(1).png)

Participating actor: User (Generic)

Entry Conditions:

* User wants to log into the application
* User already has an account

Exit Conditions:

* User Logs into the app

Event Flow:

1. User requests to log in
2. System displays login page
3. Query database for users account
    1. User is found and logged in
    2. User is not found and not logged in

Figure 7: Website Deployment

* _A developer merges to master_

![](https://t18032048.p.clickup-attachments.com/t18032048/af3ba0a0-4181-47f5-a774-4a7dfd535357/deployment-flow.png)

Participating actors: Developer, User (Generic)

Entry Conditions:

* A developer merges to the master branch in GitHub

Exit Conditions (one of the two):

* Website is deployed to AWS ECS and a success is reported to developers
* Website is unable to be deployed and a failure is reported to the developers

Event Flow:

1. Developer merges branch to master
2. GitHub actions configures the AWS credentials and logs into an AWS as an IAM user
3. GitHub actions builds the application docker image and pushes it to an AWS ECR repository
4. GitHub actions deploys an ECS task definition to AWS ECS
    1. ECS pulls the image from the ECR repo and runs it in a container with the appropriate ports exposed
    2. Users can access the website on the exposed port
5. GitHub logs out of AWS (this always happens, even on failure in other steps)
6. A success or failure is reported back to the developers

Figure 8: Manager workflow

* _A manager initiates any of his available actions_

![](https://t18032048.p.clickup-attachments.com/t18032048/d6d76a57-9409-482c-8244-d77745793d7e/manager-flow.png)

Participating actors: User (Manager)

Entry Conditions:

* A user is logged in and has manager permissions

Exit Conditions:

* Manager logs out

Event Flow:

1. Manager assigns user type
    1. User permission group is updated
2. Manager starts a tournament
    1. Players can start checking in
    2. Players can begin to order drinks
    3. Players can progress from hole to hole
3. Manager ends a tournament
    1. Players can no longer check-in
    2. Players can no longer purchase drinks
    3. Player scores are checked and the top three receive prizes
4. Add/Remove drink options
    1. Drinks available for players to purchase are updated
5. Add money to player or sponsor accounts
    1. User account balances are updated to reflect new balance
6. Cash out register
    1. Register balance is set to zero

![](https://t18032048.p.clickup-attachments.com/t18032048/38bccab6-f449-4ef5-9762-9f4827b59a09/Sprint%201%20Burdown%20Chart.PNG)
