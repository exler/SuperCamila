<p align="center">
    <img src="logo.png" width="400">
    <p align="center">🦸 Discord music/helper bot for managing small and private servers</p>
</p>

## Requirements
* Python 3.6
* ffmpeg

## Usage
* Create a new bot on [Discord Developer Portal](https://discord.com/developers/applications) and generate a bot token
* Rename `.env.example` to `.env` and fill out the empty fields

### PM2 setup
Run the installation script to setup dependencies and `pm2` for process management

```bash
$ sudo scripts/setup-pm2.sh
```

### Docker setup
Create a container using `docker-compose`

```bash
$ docker-compose up -d
```


## Available commands
```
Miscellaneous:
  format       Format message of given ID with given syntax.
Music:
  join         Make the bot join your channel
  leave        Clears the queue and makes the bot leave the voice channel
  now          Displays the currently playing song
  pause        Pauses the currently playing song
  play         Plays a song.
  queue        Shows the player's queue.
  remove       Removes a song from the queue at a given index
  resume       Resumes the currently paused song
  skip         Skips the currently playing song
  volume       Sets the volume of the player
Plan:
  changeplan   Change the lesson plan for a given group with attached image
  plan         Display the lesson plan for the group represented by user's role
Randoms:
  randommember Choose a random member of given Discord role
  randomrange  Choose a random integer between given lower and upper bounds
​No Category:
  help         Shows this message

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```

## License

Copyright (c) 2020 by ***Kamil Marut***

`SuperCamila` is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file](LICENSE).