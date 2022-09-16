def exchange():
    bitcoin_rate = input('What is Bitcoin price today? \n')
    usd_amount = input('How much $ do you have? \n')
    try:
        result = float(usd_amount) / float(bitcoin_rate)
        return print(f'For {usd_amount} USD you can buy: {round(result, 7)} BTC!')
    except ValueError:
        print('Error, please enter an integer or floating point value!\n')
        exchange()


exchange()
