# Solana Minting Bot

---

## Magic Eden NFT Minting Bot

This bot can **mint all Magic Eden NFT's projects**. It does not guarantee a successful mint but increases chances since it's much faster than human. It is also usefull when the mint time is not convenient.

Easy setup which uses ChromeDriver, it automate chrome instance and mint the nft you are looking for.

You can also **launch multiple instances of the bot to bypass minting limit / wallet**.

Please give a star ⭐

---

### Support

-   [x] Window
-   [x] Mac (Intel + m1)
-   [x] Linux (Not verified)

-   [x] MagicEden.io
-   [x] MonkeLabs.io

---

-   This bot uses ChromeDriver so on mac there is a possiblity that you will have to **allow the software to run in your privacy settings**. Check mac folder for more info.

-   The chrome window will appear **WITHOUT** loading the images, this is to ensure the fastest loading.

---

## Tutorial

1. Clone the repository / Download zip file

    `git clone https://github.com/SolanaNFTCollector/Solana-Minting-Bot.git`

    OR

    [Download Zip File](https://github.com/SolanaNFTCollector/Solana-Minting-Bot/archive/refs/heads/main.zip)
    

2. Be sure you have Python installed, [here is a link to download](https://www.python.org/downloads/)

2. Open command prompt

3. Install all python module

   `pip install selenium requests webdriver-manager`
   

4. Replace Phantom Passphrase and password in `config.json`

    `launchpadLink` --> Launchpad link on magic eden

    `seedPhrase` --> your phantom wallet passphrase (Careful do not share this key)

    `password` --> A password for your wallet

5. Open CMD and go to directory

    `cd /path/to/directory/magiceden-mint-bot/windows`

6. Run the python file

    for windows : `python main.py`

    for mac : `python3 main.py`
