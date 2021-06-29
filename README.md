[![Version](https://img.shields.io/badge/Version-1.0-blue.svg?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Python-3.4%2B-brightgreen.svg?style=for-the-badge)]()
[![Available](https://img.shields.io/badge/Available-%20Debian-red.svg?style=for-the-badge)]()
[![Available](https://img.shields.io/badge/Available-%20Windows-red.svg?style=for-the-badge)]()
[![Download](https://img.shields.io/badge/Size-410KO-brightgreen.svg?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-GPL%20v3%2B-red.svg?style=for-the-badge)](https://github.com/Herosbrine/trading_automate_binance/blob/main/LICENSE)

# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AUTOtradingMATE

### Author : Grégoire Bézier
### Contributor : Quentin Récolé
### Credit for an2linuxserver : github.com/rootkiwi

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Dependencies](#dependencies)
* [Setup](#setup)
* [License](#license)

## General info
This project is a trading tools based on "Signals", an application of trading signals.<br />
<br />
New signal available (type : High) : 1/20 of your wallet is placed on it.<br />
New signal available (type : Low) : 2/20 of your wallet is placed on it.<br />
Target 1 done : 60% of the money is converted back to USDT.<br />
Target 2 done : 20% of the money is converted back to USDT.<br />
Target 3 done : 20% of the money is converted back to USDT.<br />
Signal Closed : 100% of the money is converted back to USDT.<br />

## Technologies
Project is created with :
* Python version : 3.9.5
* MySQL version : 8.0.25
* Bash version : 5-1
* python-binance library version : 1.0.12

## Dependencies

* Python (3.4+)
```
Arch : python
Debian / Ubuntu : python3
```
* libnotify
```
Arch : libnotify
Debian / Ubuntu : libnotify4 gir1.2-notify-0.7 gir1.2-gdkpixbuf-2.0
```
* python-gobject
```
Arch : python-gobject
Debian / Ubuntu : python3-gi
```
* openssl (1.0.1+)

* MySQL

&nbsp;&nbsp;&nbsp;&nbsp;-Download MySQL : https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/

* Binance account and api key

&nbsp;&nbsp;&nbsp;&nbsp;-Create account : https://accounts.binance.com/en/register <br />
&nbsp;&nbsp;&nbsp;&nbsp;-Create Api Key : https://support.coinmatics.com/hc/en-us/articles/360015574417-How-to-create-an-API-key-on-Binance <br />
IMPORTANT! <br />
&nbsp;&nbsp;&nbsp;&nbsp;-All your money must be converted in "USDT" <br />

## Setup
* [On Linux/Windows](#on-linuxwindows)
* [On Phone](#on-phone)

### On Linux/Windows
```
$git clone https://github.com/Herosbrine/trading_automate_binance.git
$cd trading_automate_binance/trading_automation/
$pip3 install -r files/requirements.txt
```
Open `DataSql/my_sql_db.py` <br />
-Create Database `crypto_client` and table `clients` (commands are in the file)<br />
-Complete differents required variables : <br />
&nbsp;&nbsp;&nbsp;&nbsp;-name <br />
&nbsp;&nbsp;&nbsp;&nbsp;-api_key <br />
&nbsp;&nbsp;&nbsp;&nbsp;-api_secret <br />
&nbsp;&nbsp;&nbsp;&nbsp;-email <br />
&nbsp;&nbsp;&nbsp;&nbsp;-MoneyToTrade <br />
-Run this Script 1 time to create table, insert lines of the table. <br />
<br />
Open `AUTOtradingMATE.py` and complete differents required variables : <br />
&nbsp;&nbsp;&nbsp;&nbsp;-EMAIL_ADDRESS <br />
&nbsp;&nbsp;&nbsp;&nbsp;-EMAIL_PASSWORD <br />
&nbsp;&nbsp;&nbsp;&nbsp;-mydb <br />
<br />
Open `PythonScript/report_check.py` and complete differents required variables : <br />
&nbsp;&nbsp;&nbsp;&nbsp;-EMAIL_ADDRESS <br />
&nbsp;&nbsp;&nbsp;&nbsp;-EMAIL_PASSWORD <br />
&nbsp;&nbsp;&nbsp;&nbsp;-msg['to']<br />
&nbsp;&nbsp;&nbsp;&nbsp;-msg.set_content()<br />
<br>
After this just run `an2linuxserver.py` and follow the instructions. <br />
After everything configured correctly run in background this differents scripts :
```
$screen python AUTOtradingMATE.py (then : CTRL A, CTRL D)
$python an2linuxserver.py &
$screen python PythonScript/report_check.py (then : CTRL A, CTRL D)
$./parser.sh &
```


### On Phone

-Download `Signals` application. <br />
&nbsp;&nbsp;&nbsp;&nbsp;-Appstore : https://apps.apple.com/us/app/signals-crypto/id1502507178 <br />
&nbsp;&nbsp;&nbsp;&nbsp;-Playstore : https://play.google.com/store/apps/details?id=com.zyncas.signals&hl=en&gl=US <br />
-Download `an2linuxclient` application. <br />
&nbsp;&nbsp;&nbsp;&nbsp;-Github : https://github.com/rootkiwi/an2linuxclient/ <br />
<br />
Configurate `an2linuxclient` with the server and activate `Signals` and `AN2Linux`. <br />

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) for AUTOtradingMATE <br />
AUTHOR : @Herosbrine <br />
See [LICENSE](LICENSE) for more details.
<br />
