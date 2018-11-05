# Zepto Analytics

Currently Zepto Analytics is a work in progress, so don't expect much. 

It is aiming to become an application which helps you easily navigate and analyse data from numerous types of databases. 

For now, the core functionality of the application will be put into the blueprint called "public".

I will then add new features which will be structured into their own designated blueprints. So far I have made the following blueprints:

* Engine - Collects and displays data from Zepto Sensors
* Weather - Collects and displays data from forecastio
* Nordpool - Pulls energy data from nordpool

## How To Get Started

If you want to try it out. Download this repository, then make sure you have downloaded all its dependencies. Currently i would reccommend using "pip install PACKAGE-NAME". When i get time, I will make a script which automates this. 

You then need to create a copy of config-template.cfg, name it config.cfg and instert your personal api-keys. Currently only forecastio is supported, but it will be expanded to include user information etc. 

When ready, go into the Zepto Analytics root directory and issue the following command:
```
python app.py
```
Go into http://localhost:5000 in your browser and start playing about!

## License

This project is licensed under the [MIT License ](https://opensource.org/licenses/MIT)
