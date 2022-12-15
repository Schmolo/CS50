-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = "Humphrey Street";
-- "Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses
--  who were present at the time – each of their interview transcripts mentions the bakery."

SELECT name, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";
-- "Ruth: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame."

SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND activity = "exit" AND minute BETWEEN 15 AND 25;

-- "Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money."

SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = "withdraw";

-- "Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call,
-- I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket."

SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville");
SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration <= 60;


-- code to get the thief
-- looking for phone number with an outgoing call less or equal to 60seconds
-- look for passport number wich was an a flight from "Fiftyville" the next day and filter so you get the earlyest flight
-- look for the license plates that exited the bakery in an timeframe of 10 min after the theft
-- look for person who withdrew money that day on "Legget Street"
SELECT name
FROM people
WHERE phone_number IN
    (SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration <= 60
AND passport_number IN
    (SELECT passport_number
    FROM passengers
    WHERE flight_id IN
        (SELECT id
        FROM flights
        WHERE year = 2021
        AND month = 7
        AND day = 29
        AND origin_airport_id IN
            (SELECT id
            FROM airports
            WHERE city = "Fiftyville")
        ORDER BY hour, minute ASC
        LIMIT 1)))
AND license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND activity = "exit"
    AND minute BETWEEN 15 AND 25)
AND id IN
    (SELECT person_id
    FROM bank_accounts
    WHERE account_number IN
        (SELECT account_number
        FROM atm_transactions
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND transaction_type = "withdraw"
        AND atm_location = "Leggett Street"));

-- Bruce is the thief

-- code for "The city the thief ESCAPED TO"
-- look for the airport wich the peroson named "Bruce" flew to
SELECT city
FROM airports
WHERE id IN
    (SELECT destination_airport_id
    FROM flights
    WHERE id IN
        (SELECT flight_id
        FROM passengers
        WHERE passport_number IN
            (SELECT passport_number
            FROM people
            WHERE name = "Bruce")));

-- Bruce is in New York City

-- code for "The ACCOMPLICE is"
-- look who the person "Bruce" called the same day as the theft with the duration less than or equal to 60 seconds
SELECT name
FROM people
WHERE phone_number IN
    (SELECT receiver
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration <= 60
    AND caller IN
        (SELECT phone_number
        FROM people
        WHERE name = "Bruce"));

-- The Accomplice is Robin