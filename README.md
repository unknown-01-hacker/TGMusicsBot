# Calls Music — The first Open TGMusicsbot

## Requirements

- FFmpeg
- NodeJS 15+
- Python 3.7+

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/unknown-01-hacker/TGMusicsBot)


## Credits







[![Redbull](https://img.shields.io/badge/Redbull-Support-orange?style=for-the-badge&logo=telegram)](https://telegram.dog/redbullfed)  

ㅤㅤㅤㅤㅤㅤㅤ  

[![Creator](https://img.shields.io/badge/ShamilHabeeb-red?style=flat&logo=telegram)](https://telegram.dog/shamilnelli)  

[![Bot Assistant](https://img.shields.io/badge/Shamil-BotAssistant-red?style=flat&logo=CodersRank)](https://t.me/shamilhelpbot)  

ㅤㅤㅤㅤㅤㅤㅤ  

#### You can call this as an Auto Filter Bot if you like :D

### Bot simply search for the files from provided channel according to given query and gives link to those files as buttons!

## How to use the bot

* Add bot to your group with admin rights.

* Add bot to all channels which you want to link with all admin rights!

## Bot Commands - Works in Group only

(You need to be a Auth User in order to use these commands)

* /add channelid  -  Links channel to your group.

or

* /add @channelusername - Links channel to your group.

 </i>

* /del channelid  -  Delinks channel from group

or

* /del @channelusername  -  Delinks channel from group

<i>NOTE : You can get connected channel details by /filterstats </i>

* /delall  -  Removes all connected channels and filters from group!

* /filterstats  -  Check connected channels and number of filters.

## You can check the video tutorial on how to deploy

Thanks to [MovieworldkdY](https://telegram.dog/movieworldkdy) and [Shamil Habeeb](https://telegram.dog/Shamilnelli) for the idea

## License

### GNU General Public License v3.0
[Read more](http://www.gnu.org/licenses/#GPL)
