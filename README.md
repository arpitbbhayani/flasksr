# FlaskSR

FlaskSR provides an easy way to add streaming HTTP Responses for Flask.

## Why should you use this?

When the user sees something happening on the screen; the site has begun to render in response to their request. This critical first step tells the user that the site is responding to their action.
This measure is called "Time to First Paint". Today most of the websites are trying to minimize this measure. In order to enable this it is necessary to not send the complete response in one go but to push partial responses multiple times.

## Comparison and Impact
![github-example-with-flasksr](https://cloud.githubusercontent.com/assets/4745789/19834915/7354d69a-9e9a-11e6-8ab6-b7b95146a25c.gif)


## Installation
Install the extension with the following command:

```
$ pip install flasksr
```

## Usage
Once installed, the FlaskSR is easy to use. Following examples will help you through the complete usage

 - [How to use FlaskSR](https://github.com/arpitbbhayani/flasksr/blob/master/examples/basicsr.py) : This is very basic top to down streaming of page components. Consider this to be the __Hello, World__ of FlaskSR.
 - [LayoutSR example](https://github.com/arpitbbhayani/flasksr/blob/master/examples/layoutsr.py) : The example shows how you can prioritize rendering of various components of your page.
 - [Advanced Usage: Github Profile Example](https://github.com/arpitbbhayani/flasksr/tree/master/examples/github-profile) : The example creates a Github Profile page of a user and renders different component of pages in different order so as to render the most important component first.

## Documentation

Complete documentation for FlaskSR is available on [FlaskSR's GitBook](https://arpitbbhayani.gitbooks.io/flasksr/).

## Contributing

We welcome contributions! If you would like to hack on FlaskSR, please follow these steps:

 - Fork this repository
 - Make your changes
 - Submit a pull request after running make check (ensure it does not error!)
 - Please give us adequate time to review your submission. Thanks!
