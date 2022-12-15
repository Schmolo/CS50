import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get uid from session
    uid = session["user_id"]

    # Query Database for all Shares a User owns
    shares = db.execute("SELECT * FROM shares WHERE id = ? AND shares > 0", uid)

    # Query Database for Cash User has
    cash = db.execute("SELECT cash FROM users WHERE id = ? ", uid)

    # init sum price var for the whole value of all shares
    sum_price = 0

    # For Shares a User owns
    for share in shares:

        # Call lookup
        look = lookup(share['symbol'])

        # Calculate Total Value per Share
        total = look['price'] * share['shares']

        # Add Total Value to Sum Var
        sum_price += total

        # Add Total Value, Company Name and Share price to Dict
        share['total'] = usd(total)
        share['name'] = look['name']
        share['price'] = usd(look['price'])

    # Calculate Total Value for User portfolio
    total_cash = usd(cash[0]['cash'] + sum_price)

    # Render main Page with owned Shares, owned Cash and total Value
    return render_template("index.html", sum_price=sum_price, shares=shares, cash=usd(cash[0]['cash']), total_cash=total_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If POST request
    if request.method == "POST":

        # Get uid from session
        uid = session["user_id"]

        # Get User input from form
        symbol = request.form.get("symbol")
        shares_raw = request.form.get("shares")

        # Get current Time for transactions
        time = datetime.now()
        time_string = time.strftime("%d/%m/%Y %H:%M:%S")

        # Call lookup
        look = lookup(symbol)

        # Try to convert input to int
        try:
            shares = int(shares_raw)
        except:
            return apology("not a number", 400)

        # Check if lookup return Somethig
        if look == None:
            return apology("non valid symbol", 400)

        # Ensure User Input is not a float
        if not shares % 1 == 0:
            return apology("number is not an int", 400)

        # Ensure that Input is greater than 0
        if not shares > 0:
            return apology("a minimum of 1 share is required", 400)

        # Get Price per Share
        price = look["price"]

        # Query Database for User with uid
        user = db.execute("SELECT * FROM users WHERE id = ?", uid)

        # Query Database for Shares with Symbol and uid
        has_shares = db.execute("SELECT shares FROM shares WHERE id = ? AND symbol = ?", uid, symbol)

        # Calculate cost for the buy
        cost = price * shares

        # Ensure User has enough Cash
        if cost > user[0]["cash"]:
            return apology("not enough balance", 400)

        # Calculate Money after Buy
        div = user[0]["cash"] - cost

        # Ensure Share Database entry exist else create
        if len(has_shares) != 0:

            # Calculate Shares after Buy
            end_shares = has_shares[0]["shares"] + shares

            # Update Database with new amount of Shares
            db.execute("UPDATE shares SET shares = ? WHERE id = ? AND symbol = ?", end_shares, uid, symbol)

        else:

            # Create new Database entry for Share
            db.execute("INSERT INTO shares (id, symbol, shares) VALUES (?, ?, ?)", uid, symbol, shares)

        # Update Cash for User
        db.execute("UPDATE users SET cash = ? WHERE id = ?", div, uid)

        # Create new transaction entry
        db.execute("INSERT INTO transactions (id, time, shares, price, symbol) VALUES (?, ?, ?, ?, ?)",
                   uid, time_string, shares, price, symbol)

        # Redirect to main Page with message
        flash('Bought!')
        return redirect("/")

    # If GET request
    else:

        # Render buy Page
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Get uid from session
    uid = session["user_id"]

    # Query Database for all transactions for user
    history = db.execute("SELECT * FROM transactions WHERE id = ?", uid)

    # Render history site with transactions
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    # If POST request
    if request.method == "POST":

        # Get User Input from form
        symbol = request.form.get("symbol")

        # Call lookup
        look = lookup(symbol)

        # Ensure that lookup return something
        if look == None:
            return apology("this symbol does not match to any stock", 400)

        # Convert number to string for usd
        look['price'] = usd(look['price'])

        # Render quoted Site
        return render_template("quoted.html", look=look)

    else:

        # Render quote Site
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    # If POST request
    if request.method == "POST":

        # Get User Input from form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Query Database with Input Username
        check = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure Username is not already taken
        if len(check) != 0:
            return apology("username already taken", 400)

        # Ensure Username was submitted
        elif not username:
            return apology("must provide username", 400)

        # Ensure Password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure confirmation Password was submitted
        elif not confirmation:
            return apology("must provide password confirmation", 400)

        # Ensure Password and confirmation Password is the same
        elif not password == confirmation:
            return apology("password and password confirmation dont match", 400)

        else:
            # Generate Hash for Password
            password_hash = generate_password_hash(password)

            # Inser new User into Database and get uid
            session_check = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)

            # Set session id
            session["user_id"] = session_check

            # Redirect to main Page with message
            flash('Registered!')
            return redirect("/")

    # If GET request
    else:

        # Render Register Page
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Get uid form session
    uid = session["user_id"]

    # If POST request
    if request.method == "POST":

        # Get user input from form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Try to convert input to int
        try:
            shares = int(shares)
        except:
            return apology("input is not a number", 400)

        # Get current Time for transactions
        time = datetime.now()

        # Format Time
        time_string = time.strftime("%d/%m/%Y %H:%M:%S")

        # Query Database for Shares with matching Symbol from Input
        share = db.execute("SELECT * FROM shares WHERE id = ? AND symbol = ?", uid, symbol)

        # Query Database for User Cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", uid)

        # Call lookup with Symbol from Input
        look = lookup(symbol)

        # Ensure lookup return something
        if look == None:
            return apology("there is no stock with this symbol", 400)

        # Ensure that User has given Symbol in Database
        if len(share) == 0:
            return apology("you dont own any of this stock", 400)

        # Ensure user has the number of Shares he likes to sell
        if shares >= share[0]['shares'] or shares < 1:
            return apology("invalid amount of shares", 400)

        # Ensure User Input is not a float
        if not shares % 1 == 0:
            return apology("invalid number of shares", 400)

        # Calculate number of Shares the User will have after selling
        end_shares = share[0]['shares'] - shares

        # Init Var and turn Input negative
        negative_shares = 0
        negative_shares -= shares

        # Calculate total Cash the User gets after selling
        price = shares * look['price']

        # Calculate total Cash the User has after selling
        div = cash[0]['cash'] + price

        # Update Database with new number of Shares the User has
        db.execute("UPDATE shares SET shares = ? WHERE id = ? AND symbol = ?", end_shares, uid, symbol)

        # Update Database with new number of Cash the User has
        db.execute("UPDATE users SET cash = ? WHERE id = ?", div, uid)

        # Add a new transaction entry in Database
        db.execute("INSERT INTO transactions (id, time, shares, price, symbol) VALUES (?, ?, ?, ?, ?)",
                   uid, time_string, negative_shares, price, symbol)

        # Redirect User to main Page with message
        flash('Sold!')
        return redirect("/")

    # If GET request
    else:

        # Get all owned Shares per Stock for User thats greater than 0
        shares = db.execute("SELECT symbol FROM shares WHERE id = ? AND shares > 0", uid)

        # Render Sell page with Share Symbol drop down
        return render_template("sell.html", shares=shares)


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    # Get uid from session
    uid = session["user_id"]

    # If POST request
    if request.method == "POST":

        # If Password Change form submitted
        if "change_password" in request.form:

            # Get all Passwords from Form
            old = request.form.get("current")
            old_confirm = request.form.get("again")
            new = request.form.get("new")

            # Query Database for Password for current user
            rows = db.execute("SELECT hash FROM users WHERE id = ?", uid)

            # Ensure current Password was submitted
            if not old:
                return apology("missing old password", 400)

            # Ensure current Password confirmation was submitted
            if not old_confirm:
                return apology("missing conformation password", 400)

            # Ensure new Password was submitted
            if not new:
                return apology("missing new password", 400)

            # Ensure that current and confirmation Password are the same
            if not old == old_confirm:
                return apology("passwords dont match", 400)

            # Ensure that current Password is correct
            if not check_password_hash(rows[0]["hash"], old):
                return apology("wrong password", 400)

            # Generate a new hash for new password
            new_hash = generate_password_hash(new)

            # Update Database with new Password Hash
            db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, uid)

            # Redirect User to main Page with flash message
            flash("Password Changed!")
            return redirect("/")

        # If Add Cash form was submitted
        elif "add_cash" in request.form:

            # Get Amount of Cash that the User wants to Add from form
            add = request.form.get("add")

            # Ensure Input is a number
            try:
                add_float = float(add)
            except:
                return apology("not a valid number", 400)

            # Query Database for the current Cash that the user has
            curr_cash = db.execute("SELECT cash FROM users WHERE id = ?", uid)

            # Calculate new Cash amount user will have after adding Cash
            new_cash = curr_cash[0]['cash'] + add_float

            # Update Database with new Cash amount for the user
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, uid)

            # Redirect User to main page with flash message
            flash("Cash added!")
            return redirect("/")

    # If GET request
    else:

        # Render Settings site
        return render_template("settings.html")